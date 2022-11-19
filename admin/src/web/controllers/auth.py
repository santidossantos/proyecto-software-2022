from flask import (
    Blueprint,
    flash,
    jsonify,
    redirect,
    render_template,
    request,
    session,
    url_for,
)
from flask_jwt_extended import get_jwt_identity, jwt_required, unset_jwt_cookies
from src.core import auth
from src.core.auth.user import User
from src.web.utils.validations import validationEmail
from src.web.controllers.api import JSON_serialized_response
from src.core.serializer.user import UserSchema

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


@auth_blueprint.get("/user_jwt")
@jwt_required()
def user_jwt():
    current_user = get_jwt_identity()
    user = auth.get_user(current_user)
    serializer = UserSchema()
    response = JSON_serialized_response(user, serializer)
    return response, 200


@auth_blueprint.get("/logout_jwt")
@jwt_required()
def logout_jwt():
    response = jsonify()
    unset_jwt_cookies(response)
    return response, 200
