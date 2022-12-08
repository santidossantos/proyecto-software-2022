from flask import Blueprint
from flask import render_template
from flask import request
from flask import flash
from flask import url_for
from flask import redirect
from src.core import associates
from src.core import disciplines
from src.core import config
from src.core import payment
import datetime
from src.web.helpers.permission import permisson_required

inscription_blueprint = Blueprint("inscription", __name__, url_prefix="/inscription")


@inscription_blueprint.get("/")
@inscription_blueprint.get("<int:id>")
@inscription_blueprint.get("<int:page_num>/<int:id>")
@permisson_required("inscription_index")
def inscription(page_num=1, id=1):

    if not disciplines.isActive(id):
        flash("La disciplina no esta activa", "error")
        return redirect((url_for("disciplines.discipline_index")))
    search = request.args.get("search_field")

    paginated_associates = associates.list_associateActiveAndInactive(
        page_num=page_num,
        per_page=config.get_per_page(),
        search=search,
        nroSocio=False,
    )
    return render_template(
        "disciplines/inscriptions.html",
        associates=paginated_associates,
        idDisciplina=id,
    )


@inscription_blueprint.route("/doInscription/<id>/<idDisciplina>")
@permisson_required("inscription_create")
def doInscription(id, idDisciplina):
    inscription = disciplines.find_inscription_by_associate_and_discipline(
        idAssociate=id, idDiscipline=idDisciplina
    )
    if not inscription:
        # verificar si el socio está al dia con las cuotas
        if payment.esMoroso(id):
            flash("Error! el asociado es moroso", "error")
            # poner asociado en defaulter
            associates.setDefaulter(id)
            return redirect((url_for("inscription.inscription", id=idDisciplina)))
        else:
            associates.setNotDefaulter(id)
        if not associates.is_active(id):
            flash("El asociado no es activo", "error")
            return redirect((url_for("disciplines.discipline_index")))
        disciplines.createInscription(idAsociado=id, idDisciplina=idDisciplina)
        flash("Inscripcion realizada", "success")
    else:
        flash("El asociado ya se encuentra inscripto a la disciplina", "error")
    return redirect((url_for("disciplines.discipline_index")))


@inscription_blueprint.post("/search/<id>")
def search(id):
    params = request.form
    search = params["search_field"]

    paginated_associates = associates.list_associateActiveAndInactive(
        page_num=1,
        per_page=config.get_per_page(),
        search=search,
        nroSocio=False,
    )
    return render_template(
        "disciplines/inscriptions.html",
        associates=paginated_associates,
        idDisciplina=id,
    )
