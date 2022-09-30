from flask import Blueprint
from flask import render_template
from src.core import auth

users_blueprint = Blueprint("users", __name__, url_prefix="/users")


@users_blueprint.get("/")
@users_blueprint.get("/<int:page_num>")
def user_index(page_num=1, per_page=3):
    paginated_users = auth.list_users(page_num=page_num, per_page=per_page)
    return render_template("users/users_list.html", users=paginated_users)


@users_blueprint.get("/create")
def create():
    return render_template("users/create.html")
