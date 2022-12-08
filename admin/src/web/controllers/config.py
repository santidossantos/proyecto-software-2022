from crypt import methods
from distutils.log import error
from flask import Blueprint
from flask import render_template
from flask import flash
from flask import url_for
from flask import redirect
from flask import request
from src.core import config
from distutils.util import strtobool
from src.web.helpers.permission import permisson_required
from src.web.utils import validations

config_blueprint = Blueprint("config", __name__, url_prefix="/config")


@config_blueprint.route("/")
@permisson_required("config_index")
def config_form():
    return render_template("config/config.html", config=config.get_config())



@config_blueprint.route("/update-config", methods=["POST", "GET"])
@permisson_required("config_update")
def update_config():
    """Returns the view of config update and do the update in the database"""

    params = request.form
    per_page = params["per_page"]
    month_value = params["month_value"]
    recharge_percentaje = params["recharge_percentaje"]

    if not validations.CampoVAcio(per_page, month_value, recharge_percentaje):
        return redirect(url_for("config.config_form"))
    
    #maximo de entradas por pagina en 100
    if not validations.rangeInteger(per_page, 0, 100):
        return redirect(url_for("config.config_form"))
    
    #maximo valor de cuota de mes en 20000, en un futuro se puede cambiar pero mientras prevenimos errores
    if not validations.rangeInteger(month_value, 0, 20000):
        return redirect(url_for("config.config_form"))

    #porcentaje de recarga maximmo en 100%
    if not validations.rangeInteger(recharge_percentaje, 0, 100):
        return redirect(url_for("config.config_form"))

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
