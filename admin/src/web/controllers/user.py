from flask import Blueprint
from flask import render_template
from src.core import auth

users_blueprint = Blueprint("users", __name__, url_prefix="/users")


@users_blueprint.get("/")
def user_index():
    users = auth.list_users()
    return render_template("users/users_list.html", users=users)


@users_blueprint.get("/create")
def create():
    return render_template("users/create.html")
