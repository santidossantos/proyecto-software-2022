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

inscription_blueprint = Blueprint("inscription", __name__, url_prefix="/inscription")


@inscription_blueprint.get("/")
@inscription_blueprint.get("/<int:page_num>")
@inscription_blueprint.get("/<int:id>")
def inscription(id, page_num=1):
    if(not disciplines.isActive(id)):
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
def doInscription(id, idDisciplina):
    inscription = disciplines.find_inscription_by_associate_and_discipline(
        idAssociate=id, idDiscipline=idDisciplina
    )
    if not inscription:
        #verificar si el socio está al dia con las cuotas
        pending_payments = payment.payments_impagos(id)
        pago = payment.get_payment(pending_payments[0].id)
        mes = mesToInt(pago.mes)
        if mes <= datetime.datetime.now().month:
            flash("Error! el asociado es moroso", "error")
            return redirect((url_for("inscription.inscription", id=idDisciplina)))
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

def mesToInt(mesPago):
    mes = str(mesPago)
    if mes == "Mes.E":
        return 1
    elif mes == "Mes.F":
        return 2
    elif mes == "Mes.M":
        return 3
    elif mes == "Mes.A":
        return 4
    elif mes == "Mes.May":
        return 5
    elif mes == "Mes.Jun":  
        return 6
    elif mes == "Mes.Jul":
        return 7
    elif mes == "Mes.Ago":
        return 8
    elif mes == "Mes.S":
        return 9
    elif mes == "Mes.O":
        return 10
    elif mes == "Mes.N":
        return 11
    elif mes == "Mes.D":
        return 12



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
