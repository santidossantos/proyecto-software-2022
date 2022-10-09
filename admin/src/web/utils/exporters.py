from re import search
from flask import Blueprint
from flask import Response
from flask import request
from src.core import associates
from src.core.associates.associate import Associate
from src.core.database import db
from src.core.associates import list_associate_filtered
import io
import csv

exporters_blueprint = Blueprint("exporters", __name__, url_prefix="/exporters")


@exporters_blueprint.post("/csv")
def generate_csv_file():

    params = request.form
    active_filter = params["active_filter"]
    search_filter = params["search_field"]

    records = list_associate_filtered(search_filter, active_filter)

    columns = ["Apellido, Nombre, Email, DNI, Dirección, Teléfono, Género"]
    output = io.StringIO()
    writer = csv.writer(output)
    writer.writerow(columns)

    for row in records:
        content = f"{row.last_name},{row.name},{row.email},{row.dni},{row.address},{row.mobile_number}"
        line = [content]
        writer.writerow(line)

    output.seek(0)

    return Response(
        response=output,
        headers={"Content-Disposition": "attachment;filename=report.csv"},
        mimetype="text/csv",
    )
