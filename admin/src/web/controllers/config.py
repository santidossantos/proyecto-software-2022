from flask import Blueprint
from flask import render_template
from flask import flash
from flask import url_for
from flask import redirect
from flask import request
from src.core import config
from distutils.util import strtobool

config_blueprint = Blueprint("config", __name__, url_prefix="/config")


@config_blueprint.get("/")
def config_form():
    return render_template("config/config.html", config=config.get_config())


@config_blueprint.post("/update-config")
def update_config():

    params = request.form
    per_page = params["per_page"]
    month_value = params["month_value"]
    recharge_percentaje = params["recharge_percentaje"]

    contact_information = ""

    if "phone" in request.form:
        contact_information += params["phone"] + " "
    
    if "email" in request.form:
        contact_information += params["email"] + " "

    if "twitter" in request.form:
        contact_information += params["twitter"] + ""

    payment_voucher_text = params["payment_voucher_text"]
    is_pay_table_active = strtobool(params["is_pay_table_active"])

    config.update_config(
        per_page=per_page,
        month_value=month_value,
        recharge_percentaje=recharge_percentaje,
        contact_information=contact_information,
        payment_voucher_text=payment_voucher_text,
        is_pay_table_active=is_pay_table_active,
    )

    flash("Configuración actualizada", "success")
    return redirect(url_for("users.user_index"))
