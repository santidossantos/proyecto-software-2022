from calendar import month
from src.core.payment import costo_total
from flask import Blueprint, request
from flask import render_template, flash
from core import config
from src.core import payment
from src.core import associates
from flask import url_for
from flask import redirect
from src.web.helpers.permission import permisson_required
import datetime
from src.web.utils.exporters.pdf import generate_pdf_file_payment

payment_blueprint = Blueprint("payment", __name__, url_prefix="/payment")


@payment_blueprint.get("/")
@payment_blueprint.get("/<int:page_num>")
@permisson_required("payment_index")
def payment_index(page_num=1):
    """Returns the payment template"""

    search = request.args.get("search_field")
    paginated_users = associates.list_associate(
        page_num=page_num,
        per_page=config.get_per_page(),
        search=search,
        active=True,
        nroSocio=True,
    )
    return render_template("payment/index.html", users=paginated_users)


@payment_blueprint.route("/show/<id>")
@permisson_required("payment_show")
def show(id):
    """Shows the specific template for do a payment

    Args:
        id (int): Associated Identifier
    """
    associate = associates.get_associate(id)
    pending_payments = payment.pending_payments(id)
    # para cada pending_payments se debe calcular el costo total
    total = 0
    for pending_payment in pending_payments:
        print(pending_payment.state.value)
        if pending_payment.state.value == "Impago":
            mes = mesToInt(pending_payment.mes)
            costo_disciplines = associates.cost_disciplines(id, mes)
            costo_total = payment.costo_total(costo_disciplines, mes, pending_payment.AnioNum)
            total = total + costo_total
    disciplines = associates.getDisciplinas(id, datetime.datetime.now().month)
    return render_template(
        "payment/show.html",
        pending=pending_payments,
        user=associate,
        total=total,
        disciplines=disciplines,
    )


@payment_blueprint.route("/result/<id>/<id_pago>")
@permisson_required("payment_show")
def result(id, id_pago):
    """Given an user id and a payment, this function register a payment for the
        specified user, and validates that the payments are payed in order

    Args:
        id (int): User Identifier
        id_pago (int): Payment Identifier form the template

    """
    pending_payments = payment.payments_impagos(id)
    associate = associates.get_associate(id)
    pago = payment.get_payment(id_pago)
    mes = mesToInt(pago.mes)
    costo_disciplines = associates.cost_disciplines(id, mes)
    costo_total = payment.costo_total(costo_disciplines, mes, pago.AnioNum)
    todasDisciplinas = associates.getDisciplinas(id, mes)
    mesActual = datetime.datetime.now().month
    anioActual = datetime.datetime.now().year
    #chequear si el pago que se quiere pagar es del mes anterior o del mismo mes, sino no se puede pagar
    if (pago.mesNum > mesActual and pago.AnioNum >= anioActual):
            flash("Error! No se puede pagar una cuota siguiente al mes actual", "error")
            return redirect(url_for("payment.show", id=id))
    elif pago == pending_payments:
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
@permisson_required("payment_update")
def updatePayment(id, id_pago, total):
    payment.update_Payment(id_pago, total)
    flash("Pago realizado con éxito", "success")

    return redirect(url_for("payment.show", id=id))


@payment_blueprint.get("/emitir-certificado/")
def generate_voucher():
    """Generates a payment voucher given a Payment Model"""

    id = request.args.get("id")
    id_pago = request.args.get("id_pago")

    associado = associates.get_associate(id)
    pago = payment.get_payment(id_pago)
    texto = config.get_payment_voucher_description()
    nroComprobante = pago.nroComprobante

    return generate_pdf_file_payment(
        texto=texto,
        id=id_pago,
        associate=associado,
        month=pago.mes.value,
        costo_total=pago.total,
        fecha=pago.update_at,
        nroComprobante=nroComprobante,
    )
