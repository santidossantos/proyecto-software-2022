from flask import Blueprint
from flask import render_template, flash
from src.core import payment
from src.core import associates
from flask import url_for
from flask import redirect

payment_blueprint = Blueprint("payment", __name__, url_prefix="/payment")


@payment_blueprint.get("/")
@payment_blueprint.get("/<int:page_num>")
def payment_index(page_num=1, per_page=4):
    paginated_users = associates.list_associate(page_num=page_num, per_page=per_page)
    return render_template("payment/index.html", users=paginated_users)


@payment_blueprint.route("/show/<id>")
def show(id):
    associate = associates.get_associate(id)
    pending_payments = payment.pending_payments(id)
    costo_disciplines = associates.cost_disciplines(id)
    costo_total = payment.costo_total(costo_disciplines)
    return render_template(
        "payment/show.html",
        pending=pending_payments,
        user=associate,
        costo_total=costo_total,
    )


@payment_blueprint.route("/result/<id>/<id_pago>")
def result(id, id_pago):
    pending_payments = payment.pending_payments(id)
    associate = associates.get_associate(id)
    costo_disciplines = associates.cost_disciplines(id)
    costo_total = payment.costo_total(costo_disciplines)
    pago = payment.get_payment(id_pago)
    if pago.mes.value == pending_payments[0].mes.value:
        return render_template(
            "payment/report.html", associate=associate, costo_total=costo_total
        )

    else:
        flash("Debe pagar las cuotas vencidas", "error")
    return render_template(
        "payment/show.html",
        pending=pending_payments,
        user=associate,
        costo_total=costo_total,
    )
