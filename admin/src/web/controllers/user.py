from flask import Blueprint
from flask import render_template
from flask import request
from flask import flash
from flask import url_for
from flask import redirect
from src.core import auth
from src.core.auth.user import User

users_blueprint = Blueprint("users", __name__, url_prefix="/users")


@users_blueprint.get("/")
@users_blueprint.get("/<int:page_num>")
def user_index(page_num=1, per_page=1):
    paginated_users = auth.list_users(page_num=page_num, per_page=per_page)
    return render_template("users/users_list.html", users=paginated_users)


@users_blueprint.get("/create")
def render():
    return render_template("users/create.html")


@users_blueprint.post("/create")
def create():
    email = request.form.get("email")
    password = request.form.get("password")
    auth.create_user(email=email, password=password)
    flash("Usuario Creado Correctamente", "success")
    return redirect((url_for("users.user_index")))
