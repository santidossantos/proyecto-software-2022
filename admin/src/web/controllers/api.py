from src.core import associates
from flask import Blueprint, jsonify, make_response, request
from src.core import disciplines, payment
from src.core.serializer.discipline import DisciplineSchema
from src.core.serializer.payment import PaymentSchema
from src.core.serializer.disciplineCant import DisciplineCantSchema

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
    serializer = DisciplineCantSchema(many=True)
    return JSON_serialized_response(records, serializer)

@club_blueptint.get("/disciplinesCant")  # La url seria /api/club/disciplinesCant
def disciplinesCantAssociates():
    records = disciplines.disciplinesCantInscriptions()
    return records


@me_blueprint.get("/disciplines/<id>")
def get_disciplines_by_id(id):
    records =  associates.associated_disciplines(id)
    return True


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

    payment.create_payment(associated_id , month, total)

    resp = make_response(jsonify({"result": "Success"}))
    resp.headers["Content-Type: application/json"] = "*"
    return resp


