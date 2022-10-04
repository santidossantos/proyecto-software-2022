# from urllib import request
from flask import Blueprint
from flask import render_template
from flask import request
from src.core import auth
from flask import flash
from flask import redirect
from flask import url_for
from flask import session
import re


auth_blueprint = Blueprint("auth", __name__, url_prefix="/auth")


@auth_blueprint.get("/")
def login():
    return render_template("auth/login.html")


@auth_blueprint.post("/authenticate")
def authenticate():
    params = request.form
    if regex(params["email"]):
        user = auth.find_user_by_email_and_pass(params["email"], params["password"])

        if not user:
            flash("Email o clave incorrecta", "error")
            return redirect(url_for("auth.login"))

        session["user"] = user.email
        flash("Sesión iniciada", "success")
        return redirect(url_for("home"))
    else:
        return redirect(url_for("auth.login"))


@auth_blueprint.get("/logout")
def logout():
    del session["user"]
    session.clear()
    flash("La session se cerró correctamene", "success")

    return redirect(url_for("auth.login"))


def regex(email):
    return re.match(
        "^[(a-z0-9\_\-\.)]+@[(a-z0-9\_\-\.)]+\.[(a-z)]{2,15}$", email.lower()
    )
