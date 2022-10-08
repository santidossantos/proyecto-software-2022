from flask import Blueprint
from flask import render_template
from flask import request
from flask import flash
from flask import url_for
from flask import redirect
from src.core import associates

associates_blueprint = Blueprint("associates", __name__, url_prefix="/associates")


@associates_blueprint.get("/")
@associates_blueprint.get("/<int:page_num>")
def associate_index(page_num=1, per_page=4):
    paginated_associates = associates.list_associate(
        page_num=page_num, per_page=per_page
    )
    return render_template(
        "associates/associates_list.html", associates=paginated_associates
    )


@associates_blueprint.route("/create", methods=("GET", "POST"))
def create():

    if request.method == "POST":
        name = request.form.get("name")
        last_name = request.form.get("last_name")
        dni = request.form.get("dni")
        genero = request.form.get("genero")
        mobile_number = request.form.get("mobile_number")
        email = request.form.get("email")
        address = request.form.get("address")
        if associates.usWithUserEmail(email):
            flash("el email ingresado está ocupado", "error")
            return redirect(url_for("associates.create"))
        associates.create_user(
            name=name,
            last_name=last_name,
            dni=dni,
            genero=genero,
            mobile_number=mobile_number,
            email=email,
            address=address,
        )
        flash("Asociado Creado Correctamente", "success")
        return redirect((url_for("associates.associate_index")))

    return render_template("associates/create.html")


@associates_blueprint.route("/update/<id>", methods=["POST", "GET"])
def update(id):
    if request.method == "POST":
        email = request.form.get("email")
        name = request.form.get("name")
        last_name = request.form.get("last_name")
        dni = request.form.get("dni")
        mobile_number = request.form.get("mobile_number")
        address = request.form.get("address")
        associates.update_associate(
            id=id,
            email=email,
            name=name,
            last_name=last_name,
            dni=dni,
            mobile_number=mobile_number,
            address=address,
        )
        flash("Asociado Modificado Correctamente", "success")
        return redirect((url_for("associates.associate_index")))

    associate = associates.get_associate(id=id)
    return render_template("associates/update.html", associate=associate)


@associates_blueprint.route("/show/<id>")
def show(id):
    associate = associates.get_associate(id=id)
    return render_template("associates/show.html", associate=associate)


@associates_blueprint.route("/delete/<id>")
def delete(id):
    associates.delete_user(id=id)
    flash("Asociado Eliminado Correctamente", "success")
    return redirect((url_for("associates.associate_index")))
