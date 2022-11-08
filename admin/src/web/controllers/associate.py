from core.payment import Payment
from src.core.associates.associate import DocumentType, Genero
from flask import Blueprint
from flask import render_template
from flask import request
from flask import flash
from flask import url_for
from flask import redirect
from src.core import associates
from src.web.utils.validations import CampoVAcio
from src.web.utils import exporters
from src.web.utils.validations import CampoVAcio, validationEmail, isInteger
from src.web.helpers.permission import permisson_required
from src.core import config
from base64 import b64encode

associates_blueprint = Blueprint("associates", __name__, url_prefix="/associates")


@associates_blueprint.get("/")
@associates_blueprint.get("/<int:page_num>")
@associates_blueprint.get("<int:page_num>/<search>/<active>/")
@permisson_required("member_index")
def associate_index(page_num=1):

    search = request.args.get("search_field")
    active = request.args.get("active_filter")

    paginated_associates = associates.list_associate(
        page_num=page_num,
        per_page=config.get_per_page(),
        search=search,
        active=active,
        nroSocio=False,
    )
    return render_template(
        "associates/associates_list.html", associates=paginated_associates
    )


@associates_blueprint.route("/create", methods=("GET", "POST"))
@permisson_required("member_new")
def create():
    if request.method == "POST":
        name = request.form.get("name")
        last_name = request.form.get("last_name")
        document_type = request.form.get("document_type")
        dni = request.form.get("dni")
        genero = request.form.get("genero")
        mobile_number = request.form.get("mobile_number")
        email = request.form.get("email")
        address = request.form.get("address")
        genero = request.form.get("genero")
        profile_picture = b64encode(request.files["profile_picture"].read())

        if CampoVAcio(name, last_name, document_type, dni, genero, address):
            if not isInteger(request.form.get("dni")):
                flash("el dni no es valido", "error")
                return redirect(url_for("associates.create"))
            if not request.form.get("email") == "" and not validationEmail(
                request.form.get("email")
            ):
                return redirect(url_for("associates.create"))
            if not request.form.get("email") == "" and associates.usWithUserEmail(
                email
            ):
                flash("el email ingresado está ocupado", "error")
                return redirect(url_for("associates.create"))
            associate = associates.create_user(
                name=name,
                last_name=last_name,
                document_type=document_type,
                dni=dni,
                genero=genero,
                mobile_number=mobile_number,
                email=email,
                address=address,
                profile_picture=profile_picture,
            )
            associates.generar_pagos(id=associate.id)
            flash("Asociado Creado Correctamente", "success")
            return redirect((url_for("associates.associate_index")))

    document_type = DocumentType

    genero = Genero

    return render_template(
        "associates/create.html", document_type=document_type, genero=genero
    )


@associates_blueprint.route("/update/<id>", methods=["POST", "GET"])
@permisson_required("member_update")
def update(id):
    if request.method == "POST":
        email = request.form.get("email")
        name = request.form.get("name")
        last_name = request.form.get("last_name")
        document_type = request.form.get("document_type")
        dni = request.form.get("dni")
        mobile_number = request.form.get("mobile_number")
        address = request.form.get("address")
        genero = request.form.get("genero")
        if CampoVAcio(name, last_name, document_type, dni, genero, address):
            user_edit = associates.get_associate(id)
            if not isInteger(request.form.get("dni")):
                flash("el dni no es valido", "error")
                return redirect(url_for("associates.update", id=id))
            if not request.form.get("email") == "" and not validationEmail(
                request.form.get("email")
            ):
                return redirect(url_for("associates.update", id=id))
            if (
                associates.usWithUserDni(dni)
                and associates.usWithUserDni(dni).id != user_edit.id
            ):
                flash("el dni ingresado ya existe", "error")
                return redirect(url_for("associates.update", id=id))
            associates.update_associate(
                id=id,
                email=email,
                name=name,
                last_name=last_name,
                document_type=document_type,
                dni=dni,
                mobile_number=mobile_number,
                address=address,
                genero=genero,
            )

            if request.files["profile_picture"] != None:
                profile_picture = b64encode(request.files["profile_picture"].read())
                associates.update_associate(id=id, profile_picture=profile_picture)


            flash("Asociado Modificado Correctamente", "success")
            return redirect((url_for("associates.associate_index")))

    associate = associates.get_associate(id=id)
    document_type = DocumentType
    genero = Genero
    return render_template(
        "associates/update.html",
        associate=associate,
        document_type=document_type,
        genero=genero,
    )


@associates_blueprint.route("/show/<id>")
@permisson_required("member_show")
def show(id):
    associate = associates.get_associate(id=id)
    return render_template("associates/show.html", associate=associate)


@associates_blueprint.route("/delete/<id>")
@permisson_required("member_destroy")
def delete(id):
    associates.delete_user(id=id)
    flash("Asociado Eliminado Correctamente", "success")
    return redirect((url_for("associates.associate_index")))


@associates_blueprint.get("/export/csv")
def call_csv_exporter():
    search_filter = request.args.get("search_field")
    active_filter = request.args.get("active_filter")
    return call_some_exporter("csv", search_filter, active_filter)


@associates_blueprint.get("/export/pdf")
def call_pdf_exporter():
    search_filter = request.args.get("search_field")
    active_filter = request.args.get("active_filter")
    return call_some_exporter("pdf", search_filter, active_filter)


def call_some_exporter(doc_type, search_filter, active_filter):
    records = associates.list_associate_filtered(search_filter, active_filter)
    return exporters.choose_exporter(records, doc_type)
