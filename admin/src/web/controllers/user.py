from flask import Blueprint
from flask import render_template
from flask import request
from flask import flash
from flask import url_for
from flask import redirect
from src.core import auth
from src.web.utils.validations import NotExistingEmail, validationMailAndPass

users_blueprint = Blueprint("users", __name__, url_prefix="/users")


@users_blueprint.get("/")
@users_blueprint.get("/<int:page_num>")
def user_index(page_num=1, per_page=4):
    paginated_users = auth.list_users(page_num=page_num, per_page=per_page)
    return render_template("users/users_list.html", users=paginated_users)


@users_blueprint.route("/create", methods=("GET", "POST"))
def create():

    if request.method == "POST":
        email = request.form.get("email")
        password = request.form.get("password")
        auth.create_user(email=email, password=password)
        flash("Usuario Creado Correctamente", "success")
        return redirect((url_for("users.user_index")))

    return render_template("users/create.html")

@users_blueprint.route("/delete/<id>")
def delete(id):
    auth.delete_user(id=id)
    flash("Usuario Eliminado Correctamente", "success")
    return redirect((url_for("users.user_index")))


@users_blueprint.route("/update/<id>", methods=["POST", "GET"])
def update(id):
    if request.method == "POST":
        email = request.form["email"]
        password = request.form["password"]
        if validationMailAndPass(email, password) and NotExistingEmail(email):
            auth.update_user(id=id, email=email, password=password)
            return redirect((url_for("users.user_index")))

    user = auth.get_user(id=id)
    return render_template("users/update.html", user=user)
