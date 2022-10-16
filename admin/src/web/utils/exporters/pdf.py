#from flask_weasyprint import HTML, render_pdf
from flask import render_template


def generate_pdf_file(records):

    html = render_template("associates/report.html", associates=records)
    return render_pdf(
        HTML(string=html),
        automatic_download=False,
        download_filename="listado_socios.pdf",
    )
