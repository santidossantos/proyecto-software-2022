from flask import Blueprint, jsonify, make_response
from src.core import disciplines
from src.core.serializer.discipline import DisciplineSchema

api_blueprint = Blueprint("api", __name__, url_prefix="/api/")
club_blueptint = Blueprint("club", __name__, url_prefix="/club")
me_blueprint = Blueprint("me", __name__, url_prefix="/me")

# Nested Blueprints
api_blueprint.register_blueprint(club_blueptint)
api_blueprint.register_blueprint(me_blueprint)



@club_blueptint.get("/disciplines")  # La url seria /api/club/disciplines
def get_all_disciplines():
    discipline_schema = DisciplineSchema(many=True)

    output = discipline_schema.dump(disciplines.list_disciplines_plain())


    #schema = [
    #        "$schema : http://json-schema.org/draft-04/schema#",
    #        "type : array",
    #]
    #output = schema + output

    resp = make_response(jsonify(output))
    resp.headers["Content-Type: application/json"]  = '*'
    return resp


