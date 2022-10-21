from flask import Blueprint
from flask import render_template
from flask import request
from flask import flash
from flask import url_for
from flask import redirect
from src.core import auth
from src.core.permissions.role import Role
from src.web.utils.validations import CampoVAcio, validationMailAndPass
from sqlalchemy import or_
from src.core import config

users_blueprint = Blueprint("users", __name__, url_prefix="/users")


@users_blueprint.get("/")
@users_blueprint.get("/<int:page_num>")
def user_index(page_num=1):
    paginated_users = auth.list_users(page_num=page_num, per_page=config.get_per_page())
    return render_template("users/users_list.html", users=paginated_users)


@users_blueprint.route("/create", methods=("GET", "POST"))
def create():
    if request.method == "POST":
        user_name = request.form.get("user_name")
        name = request.form.get("name")
        last_name = request.form.get("last_name")
        email = request.form.get("email")
        password = request.form.get("password")
        if CampoVAcio(name,last_name,email,password) and validationMailAndPass(email, password):
            rolesSelected=[]
            for rolId in request.form.getlist('rol'):
                unRol = Role.query.filter_by(id=rolId).first()
                rolesSelected.append(unRol)
            if not rolesSelected:
                flash("No se puede crear un usuario sin rol", "error")
                return redirect(url_for("users.create"))
            if (auth.usWithUserEmail(email)):
                flash("el email ingresado está ocupado", "error")
                return redirect(url_for("users.create"))
            if (auth.usWithUsername(user_name)):
                flash("el nombre de usuario ingresado está ocupado", "error")
                return redirect(url_for("users.create"))

            user = auth.create_user(email=email, password=password, name=name, last_name=last_name, user_name=user_name)
            auth.assigned_roles(user=user,rolesSelected=rolesSelected)
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
        user_name = request.form.get("user_name")
        name = request.form.get("name")
        last_name = request.form.get("last_name")
        email = request.form.get("email")
        password = request.form.get("password")
        if CampoVAcio(name,last_name,email,password) and validationMailAndPass(email, password):
            rolesSelected=[]
            for rolId in request.form.getlist('rol'):
                unRol = Role.query.filter_by(id=rolId).first()
                rolesSelected.append(unRol)
            if not rolesSelected:
                flash("No se puede elimiar todos los roles de un usuario", "error")
                return redirect(url_for("users.update",id=id))

            if (auth.usWithUsername(user_name)):
                flash("el nombre de usuario ingresado está ocupado", "error")
                return redirect(url_for("users.update",id=id))
            
            if (auth.usWithUserEmail(email)):
                flash("el email ingresado está ocupado", "error")
                return redirect(url_for("users.update", id=id))

            user = auth.update_user(id=id, email=email, password=password,user_name=user_name,name=name,last_name=last_name)
            for rol in rolesSelected:
                print(rol.id)
            auth.update_roles(user=user,rolesSelected=rolesSelected)
            return redirect((url_for("users.user_index")))

    user = auth.get_user(id=id)
    roles = Role.query.filter(or_(Role.nombre == 'Admin', Role.nombre == 'Operador'))
    return render_template("users/update.html", user=user, roles=roles)

@users_blueprint.route("/show/<id>")
def show(id):
    user = auth.get_user(id=id)
    return render_template("users/show.html", user=user)

@users_blueprint.route("/setStatus/<id>/<desactivado>")
def setStatus(id, desactivado):
    auth.setStatus(id=id)
    if auth.NoEsAdmin(id):
        if (desactivado == '1'):
            flash("Usuario Bloqueado Correctamente", "success")
        else:
            flash("Usuario Activado Correctamente", "success")
    else:
        flash("No se puede Bloquear un usuario Admin", "error")
    return redirect((url_for("users.user_index")))

@users_blueprint.post("/search")
def search():
    params = request.form
    active_filter = params["active_filter"]
    search_filter = params["search_field"]

    paginated_users = auth.list_users_filtered(search_filter, active_filter).paginate(1, config.get_per_page())

    return render_template("users/users_list.html", users=paginated_users)