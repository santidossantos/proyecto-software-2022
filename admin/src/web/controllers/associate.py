from flask import Blueprint
from flask import render_template
from flask import request
from flask import flash
from flask import url_for
from flask import redirect
from src.core import associates

associates_blueprint = Blueprint("associates", __name__, url_prefix="/associates")


@associates_blueprint.get("/")
@associates_blueprint.get("/<int:page_num>")
def user_index(page_num=1, per_page=1):
    paginated_associates = associates.list_associate(
        page_num=page_num, per_page=per_page
    )
    return render_template(
        "associates/associates_list.html", associates=paginated_associates
    )
