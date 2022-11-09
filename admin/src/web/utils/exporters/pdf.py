from flask_weasyprint import HTML, render_pdf
from flask import render_template

def generate_pdf_file(records):

    html = render_template("associates/report.html", associates=records)
    return render_pdf(
        HTML(string=html),
        automatic_download=False,
        download_filename="listado_socios.pdf",
    )


def generate_pdf_file_payment(associate, costo_total, month, fecha, id, texto):

    html = render_template("payment/certificado-pdf.html", texto=texto, associate=associate, costo_total=costo_total, month=month, fecha=fecha, id=id)
    return render_pdf(
        HTML(string=html),
        automatic_download=False,
        download_filename="comprobate_pago.pdf",
    )


def generate_pdf_license(associate):
    html = render_template("associates/export-license.html", associate=associate)
    return render_pdf(
        HTML(string=html),
        automatic_download=False,
        download_filename="carnet_digital.pdf",
    )
