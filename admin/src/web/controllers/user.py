from flask import Blueprint
from flask import render_template

users_blueprint = Blueprint("users", __name__, url_prefix="/users")


@users_blueprint.get("/")
def user_index():
    return render_template("users/users_list.html")
