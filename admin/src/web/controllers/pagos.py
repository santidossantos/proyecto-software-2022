from flask import Blueprint
from flask import render_template
from src.core import payment
from src.core import associates

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
    return render_template("payment/show.html", pending=pending_payments, user=associate)
