from flask import Blueprint
from flask import render_template
from flask import request
from flask import flash
from flask import url_for
from flask import redirect
from src.core import config
from src.core import disciplines
from src.web.helpers.permission import permisson_required
from src.web.utils.validations import CampoVAcio, isInteger

discipline_blueprint = Blueprint("disciplines", __name__, url_prefix="/disciplines")


@discipline_blueprint.get("/")
@discipline_blueprint.get("/<int:page_num>")
@permisson_required("discipline_index")
def discipline_index(page_num=1):
    """List all disciplines paginated"""
    paginated_disciplines = disciplines.list_disciplines(page_num=page_num, per_page=config.get_per_page())
    return render_template("disciplines/disciplines_list.html", disciplines=paginated_disciplines)


@discipline_blueprint.route("/create", methods=("GET", "POST"))
@permisson_required("discipline_new")
def create():
    if (
        request.method == "POST"
        and CampoVAcio(
            request.form.get("name"),
            request.form.get("category"),
            request.form.get("nameInstructors"),
            request.form.get("daysAndHours"),
            request.form.get("monthlyCost"),
        )
        and isInteger(request.form.get("monthlyCost"))
    ):
        name = request.form.get("name")
        category = request.form.get("category")
        nameInstructors = request.form.get("nameInstructors")
        daysAndHours = request.form.get("daysAndHours")
        monthlyCost = request.form.get("monthlyCost")
        disciplines.create_discipline(
            name=name,
            category=category,
            nameInstructors=nameInstructors,
            daysAndHours=daysAndHours,
            monthlyCost=monthlyCost,
        )
        flash("Disciplina creada correctamente", "success")
        return redirect((url_for("disciplines.discipline_index")))
    else:
        return render_template("disciplines/create.html")


@discipline_blueprint.route("/delete/<id>")
@permisson_required("discipline_destroy")
def delete(id):
    if disciplines.IsErasable(id):
        disciplines.delete_discipline(id=id)
        flash("Disciplina Eliminada Correctamente", "success")
        return redirect((url_for("disciplines.discipline_index")))
    else:
        flash(
            "No se puede eliminar la disciplina ya que tiene asociados inscriptos",
            "error",
        )
        return redirect((url_for("disciplines.discipline_index")))


@discipline_blueprint.route("/update/<id>", methods=["POST", "GET"])
@permisson_required("discipline_update")
def update(id):
    if (
        request.method == "POST"
        and CampoVAcio(
            request.form.get("name"),
            request.form.get("category"),
            request.form.get("nameInstructors"),
            request.form.get("daysAndHours"),
            request.form.get("monthlyCost"),
        )
        and isInteger(request.form.get("monthlyCost"))
    ):
        name = request.form["name"]
        category = request.form["category"]
        nameInstructors = request.form["nameInstructors"]
        daysAndHours = request.form["daysAndHours"]
        monthlyCost = request.form["monthlyCost"]
        disciplines.update_discipline(
            id=id,
            name=name,
            category=category,
            nameInstructors=nameInstructors,
            daysAndHours=daysAndHours,
            monthlyCost=monthlyCost,
        )
        flash("Disciplina editada correctamente", "success")
        return redirect((url_for("disciplines.discipline_index")))

    discipline = disciplines.get_discipline(id=id)
    return render_template("disciplines/update.html", discipline=discipline)


@discipline_blueprint.route("/show/<id>")
@permisson_required("discipline_show")
def show(id):
    discipline = disciplines.get_discipline(id=id)
    return render_template("disciplines/show.html", discipline=discipline)

@discipline_blueprint.route("/setStatus/<id>/<desactivado>")
def setStatus(id, desactivado):
    if not disciplines.IsErasable(id):
        flash("No se puede desactivar la disciplina ya que tiene asociados inscriptos", "error")
        return redirect((url_for("disciplines.discipline_index")))
    else:
        disciplines.setStatus(id=id)
        if (desactivado == '1'):
            flash("Disciplina desactivada correctamente", "success")
        else:
            flash("Disciplina activada correctamente", "success")
        return redirect((url_for("disciplines.discipline_index")))
