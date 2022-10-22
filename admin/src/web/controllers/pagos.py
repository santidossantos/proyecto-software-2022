from flask import Blueprint, request
from flask import render_template, flash
from core import config
from src.core import payment
from src.core import associates
from flask import url_for
from flask import redirect
from src.web.utils.exporters.pdf import generate_pdf_file_payment

payment_blueprint = Blueprint("payment", __name__, url_prefix="/payment")


@payment_blueprint.get("/")
@payment_blueprint.get("/<int:page_num>")
def payment_index(page_num=1, per_page=4):
    paginated_users = associates.list_associate(page_num=page_num, per_page=per_page)
    return render_template("payment/index.html", users=paginated_users)


@payment_blueprint.route("/show/<id>")
#@permisson_required("payment_show")
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
#@permisson_required("payment_show")
def result(id, id_pago):
    pending_payments = payment.pending_payments(id)
    associate = associates.get_associate(id)
    costo_disciplines = associates.cost_disciplines(id)
    costo_total = payment.costo_total(costo_disciplines)
    pago = payment.get_payment(id_pago)
    if pending_payments:
        if pago.mes.value == pending_payments[0].mes.value:
            return render_template(
                "payment/report.html",
                associate=associate,
                costo_total=costo_total,
                month=pago.mes.value,
                id_pago=id_pago,
            )
        else:
            flash("Debe pagar las cuotas vencidas", "error")
            return redirect(url_for("payment.show", id=id))
    return redirect(url_for("payment.show", id=id))


@payment_blueprint.route("/updatePayment/<id>/<id_pago>/<total>")
#@permisson_required("payment_show")
def updatePayment(id, id_pago, total):
    payment.update_Payment(id_pago, total)
    flash("Pago realizado con éxito", "success")

    associate = associates.get_associate(id)
    month = payment.get_payment(id).mes.value

    #generate_pdf_file_payment(associate, total, month)

    return redirect(url_for("payment.show", id=id))

@payment_blueprint.post("/search")
def search():
    params = request.form
    nro_or_lastaname = params["search_field"]
    print(nro_or_lastaname)

    paginated_associates = associates.associates_filtered_payment(nro_or_lastaname).paginate(1, config.get_per_page())

    return render_template("payment/index.html", users=paginated_associates)
