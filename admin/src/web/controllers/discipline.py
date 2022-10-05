from flask import Blueprint
from flask import render_template
from flask import request
from flask import flash
from flask import url_for
from flask import redirect
from src.core import disciplines

discipline_blueprint = Blueprint("disciplines", __name__, url_prefix="/disciplines")

@discipline_blueprint.get("/")
@discipline_blueprint.get("/<int:page_num>")
def discipline_index(page_num=1, per_page=1):
    paginated_disciplines = disciplines.list_disciplines(page_num=page_num, per_page=per_page)
    return render_template("disciplines/disciplines_list.html", disciplines=paginated_disciplines)


@discipline_blueprint.route("/create", methods=("GET", "POST"))
def create():
    if request.method == "POST":
        nombre = request.form.get("nombre")
        categoria = request.form.get("categoria")
        disciplines.create_discipline(nombre=nombre, categoria=categoria)
        flash("Categoria creada correctamente", "success")
        return redirect((url_for("disciplines.discipline_index")))

    return render_template("disciplines/create.html")

@discipline_blueprint.route("/delete/<id>")
def delete(id):
    disciplines.delete_discipline(id=id)
    flash("Disciplina Eliminada Correctamente", "success")
    return redirect((url_for("disciplines.discipline_index")))

@discipline_blueprint.route("/update/<id>", methods=["POST", "GET"])
def update(id):
    if request.method == "POST":
        nombre=request.form["nombre"]
        categoria=request.form["categoria"]
        disciplines.update_discipline(id=id,nombre=nombre,categoria=categoria)
        return redirect((url_for("disciplines.discipline_index")))

    discipline = disciplines.get_discipline(id=id)  
    return render_template('disciplines/update.html', discipline=discipline)