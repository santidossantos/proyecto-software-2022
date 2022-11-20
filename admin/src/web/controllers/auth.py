from flask import (
    Blueprint,
    flash,
    redirect,
    render_template,
    request,
    session,
    url_for,
)
from src.core import auth, associates
from src.core.auth.user import User
from src.web.utils.validations import validationEmail

auth_blueprint = Blueprint("auth", __name__, url_prefix="/auth")


@auth_blueprint.get("/")
def login():

    if session:
        return redirect(url_for("users.user_index"))

    return render_template("auth/login.html")


@auth_blueprint.post("/authenticate")
def authenticate():
    params = request.form
    email = params["email"]
    password = params["password"]

    if validationEmail(params["email"]):
        user = auth.find_user_by_email(email)

        if user:
            if not user.check_password(password):
                flash("Email o clave incorrecta", "error")
                return render_template("auth/login.html")

       
        if not user:
            flash("Email o clave incorrecta", "error")
            return render_template("auth/login.html")

    else:
        flash("Email no válido", "error")
        return render_template("auth/login.html")

    if auth.is_active(user.id):
        flash("Su cuenta actualmente se encuentra bloqueada", "error")
        return render_template("auth/login.html")

    session["user"] = user.email
    flash("Sesión iniciada", "success")
    return redirect(url_for("users.user_index"))


@auth_blueprint.get("/logout")
def logout():
    if not session:
        return render_template("auth/login.html")
    else:
        del session["user"]
        session.clear()
        flash("La sessión se cerró correctamente", "success")

    return render_template("auth/login.html")