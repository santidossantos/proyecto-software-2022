from flask import Blueprint, jsonify, make_response, request
from src.core import disciplines, payment
from src.core.serializer.discipline import DisciplineSchema
from src.core.serializer.payment import PaymentSchema

api_blueprint = Blueprint("api", __name__, url_prefix="/api/")
club_blueptint = Blueprint("club", __name__, url_prefix="/club")
me_blueprint = Blueprint("me", __name__, url_prefix="/me")

# Nested Blueprints
api_blueprint.register_blueprint(club_blueptint)
api_blueprint.register_blueprint(me_blueprint)


def JSON_serialized_response(records, serializer):
    resp = make_response(jsonify(serializer.dump(records)))
    resp.headers["Content-Type: application/json"] = "*"
    return resp


@club_blueptint.get("/disciplines")  # La url seria /api/club/disciplines
def get_all_disciplines():
    records = disciplines.list_disciplines_plain()
    serializer = DisciplineSchema(many=True)
    return JSON_serialized_response(records, serializer)


@me_blueprint.get("/disciplines/<id>")
def get_disciplines_by_id(id):
    return "Implementar... falta tabla users_disciplines"


@me_blueprint.get("/payments/<id>")
def get_payments_by_id(id):
    records = payment.list_assoc_payments(id)
    serializer = PaymentSchema(many=True)
    return JSON_serialized_response(records, serializer)


@me_blueprint.post("/payments")
def register_payment_by_id():
    data = request.get_json()
    date = data["date"]
    total = data["total"]
    associated_id = data["associated_id"]

    payment.create_payment(total=total, date=date, associated_id=associated_id)

    resp = make_response(jsonify({"result": "Success"}))
    resp.headers["Content-Type: application/json"] = "*"
    return resp