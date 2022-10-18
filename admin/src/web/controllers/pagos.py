from flask import Blueprint
from flask import render_template
from flask import request
from flask import flash
from flask import url_for
from flask import redirect
from src.core import payment

payment_blueprint = Blueprint("payment", __name__, url_prefix="/payment")


@payment_blueprint.route("/", methods=("GET", "POST"))
def payment_index(page_num=1, per_page=1):
    paginated_payment = payment.list_payment(page_num=page_num, per_page=per_page)
    return render_template("payment/show.html", payment=paginated_payment)
