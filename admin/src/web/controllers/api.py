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
@jwt_required()
def get_all_disciplines():
    records = disciplines.list_disciplines_plain()
    serializer = DisciplineSchema(many=True)
    return JSON_serialized_response(records, serializer)


@me_blueprint.get("/disciplines/<id>")
def get_disciplines_by_id(id):
    records = associates.associated_disciplines(id)
    serializer = DisciplineSchema(many=True)
    return JSON_serialized_response(records, serializer)


@me_blueprint.get("/payments/<id>")
def get_payments_by_id(id):
    records = payment.list_assoc_payments(id)
    serializer = PaymentSchema(many=True)
    return JSON_serialized_response(records, serializer)


@me_blueprint.post("/payments")
def register_payment_by_id():
    data = request.get_json()
    month = data["month"]
    total = data["total"]
    associated_id = data["associated_id"]

    payment.create_payment(associated_id, month, total)

    resp = make_response(jsonify({"result": "Success"}))
    resp.headers["Content-Type: application/json"] = "*"
    return resp


@api_auth_blueprint.post("/token")
def create_token():
    useremail = request.json.get("email", None)
    password = request.json.get("password", None)
    user = auth.find_user_by_email(useremail)
    if user and (user.check_password(password)):
        access_token = create_access_token(identity=user.id)
        set_access_cookies(jsonify(), access_token)
        return jsonify({"token": access_token}), 200
    return jsonify({"msg": "Bad email or password"}), 401


@auth_blueprint.get("/user_jwt")
@jwt_required()
def user_jwt():
    current_user = get_jwt_identity()
    user = auth.get_user(current_user)
    response = jsonify(user)
    return response, 200


@auth_blueprint.get("/logout_jwt")
@jwt_required()
def logout_jwt():
    response = jsonify()
    unset_jwt_cookies(response)
    return response, 200
