import re
from src.core import associates
from flask import Blueprint, jsonify, make_response, request
from src.core import disciplines, payment, config
from flask import (
    Blueprint,
    jsonify,
    make_response,
    request,
)
from flask_jwt_extended import (
    create_access_token,
    get_jwt_identity,
    jwt_required,
    set_access_cookies,
    unset_jwt_cookies,
)
from src.core import associates, auth, disciplines, payment
from src.core.serializer.discipline import DisciplineSchema
from src.core.serializer.payment import PaymentSchema
from src.core.serializer.paymentinfo import PaymentInfoSchema
from src.core.serializer.license import LicenseSchema
from src.core.serializer.user import UserSchema
import base64
from src.core.serializer.disciplineCant import DisciplineCantSchema
import os
from os import listdir


api_blueprint = Blueprint("api", __name__, url_prefix="/api/")
club_blueptint = Blueprint("club", __name__, url_prefix="/club")
me_blueprint = Blueprint("me", __name__, url_prefix="/me")

api_auth_blueprint = Blueprint("token", __name__, url_prefix="/auth")
auth_blueprint = Blueprint("auth", __name__, url_prefix="/auth")

# Nested Blueprints
api_blueprint.register_blueprint(club_blueptint)
api_blueprint.register_blueprint(me_blueprint)
api_blueprint.register_blueprint(api_auth_blueprint)


def JSON_serialized_response(records, serializer):
    """Returns a JSON response of the records given and the serializer schema specified

    Args:
        records (db.model): Model to serializer
        serializer (Schema): Marshmallow Schema serializer

    Returns:
        string: JSON Formatted String
    """

    resp = make_response(jsonify(serializer.dump(records)))
    resp.headers["Content-Type: application/json"] = "*"
    return resp


@club_blueptint.get("/disciplines")  # La url seria /api/club/disciplines
def get_all_disciplines():
    records = disciplines.list_disciplines_plain()
    serializer = DisciplineSchema(many=True)
    return JSON_serialized_response(records, serializer)


@club_blueptint.get("/cantMorosos")  # La url seria /api/club/cantMorosos
def get_defaulters():
    records = associates.cantMorosos()
    return records


@me_blueprint.get("/disciplines")
@jwt_required()
def get_disciplines_by_id():
    """This API returns an JSON Formatted string given an access token of all
    the disciplines that an associated has been enrolled"""
    current_user_id = get_jwt_identity()
    records = associates.associated_disciplines(current_user_id)
    serializer = DisciplineSchema(many=True)
    return JSON_serialized_response(records, serializer)


@club_blueptint.get("/disciplinesCant")  # La url seria /api/club/disciplinesCant
def disciplinesCantAssociates():
    records = disciplines.disciplinesCantInscriptions()
    return records


@club_blueptint.get("/generosCant")  # La url seria /api/club/generosCant
def generosCant():
    records = associates.getCantGeneros()
    return records


# obtiene cantidad de inscripciones nuevas por mes
@club_blueptint.get("/asociadosMesCant")  # La url seria /api/club/asociadosMesCant
def asociadosMesCant():
    records = associates.cantidadInscripcionesPorMes()
    return records


@me_blueprint.get("/payments")
@jwt_required()
def get_payments_by_id():
    """Get all the payments from an associated

    Returns:
        string: JSON Formatted String
    """
    current_user_id = get_jwt_identity()
    user = associates.get_associate(current_user_id)
    records = payment.list_assoc_payments_order(user.id)
    serializer = PaymentSchema(many=True)
    if config.get_pay_table_status():
        return JSON_serialized_response(records, serializer), 200
    return jsonify({"status": "desactivada"}), 200


@me_blueprint.get("/paymentsinfo")
@jwt_required()
def get_paymentsinfo_by_id():
    current_user_id = get_jwt_identity()
    user = associates.get_associate(current_user_id)
    records = payment.list_assoc_payments_order(user.id)
    serializer = PaymentInfoSchema(many=True)
    if config.get_pay_table_status():
        return JSON_serialized_response(records, serializer), 200
    return jsonify({"status": "desactivada"}), 200


@me_blueprint.get("/payments/total")
@jwt_required()
def get_payments_total():
    current_user_id = get_jwt_identity()
    pending_payments = payment.pending_payments(current_user_id)
    total = 0
    for pending_payment in pending_payments:
        mes = mesToInt(pending_payment.mes)
        costo_disciplines = associates.cost_disciplines(current_user_id, mes)
        costo_total = payment.costo_total_sin_recargo(costo_disciplines)
        total = total + costo_total
    return jsonify({"total": total}), 200


@me_blueprint.post("/payments")
@jwt_required()
def register_payment_by_id():
    current_user_id = get_jwt_identity()
    user = associates.get_associate(current_user_id)
    month = request.json.get("month", None)
    total = request.json.get("total", None)
    payment.create_payment(user.id, month, total)

    resp = make_response(jsonify({"result": "Success"}))
    resp.headers["Content-Type: application/json"] = "*"
    return resp


@me_blueprint.get("license")
@jwt_required()
def get_license():
    current_user = get_jwt_identity()
    user = associates.get_associate(current_user)

    defaulter = associates.esMoroso(user.id)
    # agrego a user el campo defaulter
    user.defaulter = defaulter
    if user.profile_picture:
        user.profile_picture.decode()
    serializer = LicenseSchema()
    return JSON_serialized_response(user, serializer)


@api_blueprint.post("auth")
def create_token():
    """Creates JSON Web Token from a post request

    Returns:
        string: JSON Formatted String
    """
    username = request.json.get("username", None)
    password = request.json.get("password", None)
    user = auth.find_user_by_user_name(
        username
    ) or associates.get_associate_by_user_name(username)
    if user and (user.check_password(password)):
        access_token = create_access_token(identity=user.id)
        set_access_cookies(jsonify(), access_token)
        return jsonify({"token": access_token}), 200
    return jsonify({"msg": "Usuario o contraseña incorrecta"}), 401


@me_blueprint.get("profile")
@jwt_required()
def user_jwt():
    current_user = get_jwt_identity()
    user = auth.get_user(current_user) or associates.get_associate(current_user)
    serializer = UserSchema()
    response = JSON_serialized_response(user, serializer)
    return response, 200


@api_blueprint.get("logout")
@jwt_required()
def logout():
    response = jsonify()
    unset_jwt_cookies(response)
    return response, 200


def mesToInt(mesPago):
    """This function asign an integer value for each month enumerative"""

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


@api_blueprint.post("/SaveArchivo")
@jwt_required()
def uploader():
    """This function allows file uploading from a post request"""
    file = request.files["file"]
    file.save(os.path.join("public/archivos", file.filename))
    return jsonify({"msg": "ok"}), 200


@api_blueprint.get("/listar")
def listar_archivos_un_dir():
    """List all files saved in a directory"""
    files_str = listdir("public/archivos")
    return jsonify({"msg": files_str}), 200


@api_blueprint.get("/config")
def get_all_datos_contacts():
    """Get all active contact information from config module"""
    records = config.get_displayable_contact_info()
    return jsonify({"contacts": records}), 200


@api_blueprint.get("/config/porcentaje")
def get_porcentaje():
    """Get payment recharge percentaje from config module"""
    records = config.get_recharge_percentaje()
    return jsonify({"porcentaje": records}), 200
