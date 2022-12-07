from flask import Response
import io
import csv


def generate_csv_file(records):
    """Generates a response from the given records in .csv format"""

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
