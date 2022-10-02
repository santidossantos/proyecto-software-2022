# from urllib import request
from flask import Blueprint
from flask import render_template
from flask import request
from src.core import auth
from flask import flash
from flask import redirect
from flask import url_for
from flask import session


auth_blueprint = Blueprint("auth", __name__, url_prefix="/auth")


@auth_blueprint.get("/")
def login():
    return render_template("auth/login.html")


@auth_blueprint.post("/authenticate")
def authenticate():
    params = request.form
    user = auth.find_user_by_email_and_pass(params["email"], params["password"])

    if not user:
        flash("Email o clave incorrecta", "error")
        return redirect(url_for("auth.login"))

    session["user"] = user.email
    flash("Sesión iniciada", "success")
    return redirect(url_for("home"))


@auth_blueprint.get("/logout")
def logout():
    del session["user"]
    session.clear()
    flash("La session se cerró correctamene", "success")

    return redirect(url_for("auth.login"))
