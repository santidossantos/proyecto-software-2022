import re
from src.core import associates
from flask import Blueprint, jsonify, make_response, request
from src.core import disciplines, payment
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
from src.core.serializer.license import LicenseSchema
from src.core.serializer.user import UserSchema
import base64

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
    current_user_id = get_jwt_identity()
    records = associates.associated_disciplines(current_user_id)
    serializer = DisciplineSchema(many=True)
    return JSON_serialized_response(records, serializer)


@me_blueprint.get("/payments")
@jwt_required()
def get_payments_by_id():
    current_user_id = get_jwt_identity()
    user = associates.get_associate(current_user_id)
    records = payment.list_assoc_payments(user.id)
    serializer = PaymentSchema(many=True)
    return JSON_serialized_response(records, serializer)


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
    #agrego a user el campo defaulter
    user.defaulter = defaulter
    if user.profile_picture:
        user.profile_picture.decode()
    serializer = LicenseSchema()
    return JSON_serialized_response(user, serializer)






@api_blueprint.post("auth")
def create_token():
    username = request.json.get("username", None)
    password = request.json.get("password", None)
    user = auth.find_user_by_user_name(
        username
    ) or associates.get_associate_by_user_name(username)
    if user and (user.check_password(password)):
        access_token = create_access_token(identity=user.id)
        set_access_cookies(jsonify(), access_token)
        return jsonify({"token": access_token}), 200
    return jsonify({"msg": "Bad email or password"}), 401


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
