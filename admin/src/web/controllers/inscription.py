from flask import Blueprint
from flask import render_template
from flask import request
from flask import flash
from flask import url_for
from flask import redirect

from src.core import associates
from src.core import inscription

inscription_blueprint = Blueprint("inscription", __name__, url_prefix="/inscription")

@inscription_blueprint.get("/")
@inscription_blueprint.get("/<int:page_num>")
def inscription(page_num=1, per_page=4):
    paginated_associates = associates.list_associate(
        page_num=page_num, per_page=per_page
    )
    return render_template("disciplines/inscriptions.html", associates=paginated_associates)
    

inscription_blueprint.route("/inscription2/<id>")
def inscription2(id):
    print("Hola")

