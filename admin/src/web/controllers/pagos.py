from flask import Blueprint, request
from flask import render_template, flash
from core import config
from src.core import payment
from src.core import associates
from flask import url_for
from flask import redirect
from src.web.helpers.permission import permisson_required

payment_blueprint = Blueprint("payment", __name__, url_prefix="/payment")


@payment_blueprint.get("/")
@payment_blueprint.get("/<int:page_num>")
@permisson_required("payment_index")
def payment_index(page_num=1):
    search = request.args.get("search_field")
    paginated_users = associates.list_associate(page_num=page_num, per_page=config.get_per_page(), search=search, active=True, nroSocio=True)
    return render_template("payment/index.html", users=paginated_users)


@payment_blueprint.route("/show/<id>")
@permisson_required("payment_show")
def show(id):
    associate = associates.get_associate(id)
    pending_payments = payment.pending_payments(id)
    costo_disciplines = associates.cost_disciplines(id,1)
    costo_total = payment.costo_total(costo_disciplines)
    return render_template(
        "payment/show.html",
        pending=pending_payments,
        user=associate,
        costo_total=costo_total,
    )


@payment_blueprint.route("/result/<id>/<id_pago>")
@permisson_required("payment_show")
def result(id, id_pago):
    pending_payments = payment.pending_payments(id)
    associate = associates.get_associate(id)
    pago = payment.get_payment(id_pago)
    mes = mesToInt(pago.mes)
    costo_disciplines = associates.cost_disciplines(id,mes)
    costo_total = payment.costo_total(costo_disciplines)
    todasDisciplinas=associates.getDisciplinas(id,mes)
    if pending_payments:
        if pago.mes.value == pending_payments[0].mes.value:
            return render_template(
                "payment/report.html",
                associate=associate,
                costo_total=costo_total,
                month=pago.mes.value,
                id_pago=id_pago,
                todasDisciplinas=todasDisciplinas,
            )
        else:
            flash("Error! Debe pagar las cuotas vencidas en orden", "error")
            return redirect(url_for("payment.show", id=id))
    return redirect(url_for("payment.show", id=id))

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


@payment_blueprint.route("/updatePayment/<id>/<id_pago>/<total>")
@permisson_required("payment_show")
def updatePayment(id, id_pago, total):
    payment.update_Payment(id_pago, total)
    flash("Pago realizado con éxito", "success")

    associate = associates.get_associate(id)
    month = payment.get_payment(id).mes.value

    #generate_pdf_file_payment(associate, total, month)

    return redirect(url_for("payment.show", id=id))
