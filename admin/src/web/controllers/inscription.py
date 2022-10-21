from flask import Blueprint
from flask import render_template
from flask import request
from flask import flash
from flask import url_for
from flask import redirect
from src.core import associates
from src.core import disciplines

inscription_blueprint = Blueprint("inscription", __name__, url_prefix="/inscription")


@inscription_blueprint.get("/")
@inscription_blueprint.get("/<int:page_num>")
@inscription_blueprint.get("/<int:id>")
def inscription(id, page_num=1, per_page=4):
    paginated_associates = associates.list_associateActive(
        page_num=page_num, per_page=per_page
    )
    return render_template(
        "disciplines/inscriptions.html",
        associates=paginated_associates,
        idDisciplina=id,
    )


@inscription_blueprint.route("/doInscription/<id>/<idDisciplina>")
def doInscription(id, idDisciplina):
    inscription = disciplines.find_inscription_by_associate_and_discipline(
        idAssociate=id, idDiscipline=idDisciplina
    )
    if not inscription:
        if associates.is_defaulter(id):
            flash(
                "El asociado esta moroso, no se puede inscribir a la disciplina",
                "error",
            )
            return redirect((url_for("disciplines.discipline_index")))
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
    search_filter = params["search_field"]

    paginated_associates = associates.list_associate_filtered(
        search_filter, True
    ).paginate(1, 2)
    return render_template(
        "disciplines/inscriptions.html",
        associates=paginated_associates,
        idDisciplina=id,
    )
