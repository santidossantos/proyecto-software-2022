from flask_weasyprint import HTML, render_pdf
from flask import render_template


def generate_pdf_file(records):
    """Generates a PDF file given the records from the parameter"""

    html = render_template("associates/report.html", associates=records)
    return render_pdf(
        HTML(string=html),
        automatic_download=False,
        download_filename="listado_socios.pdf",
    )


def generate_pdf_file_payment(
    associate, costo_total, month, fecha, id, texto, nroComprobante
):

    """Generates a PDF File as a voucher from a Payment"""

    html = render_template(
        "payment/certificado-pdf.html",
        texto=texto,
        associate=associate,
        costo_total=costo_total,
        month=month,
        fecha=fecha,
        id=id,
        nroComprobante=nroComprobante,
    )
    return render_pdf(
        HTML(string=html),
        automatic_download=False,
        download_filename="comprobate_pago.pdf",
    )


def generate_pdf_license(associate, qr_url):
    """Generates a PDF file with associated license data"""
    html = render_template(
        "associates/export-license.html", associate=associate, qr_url=qr_url
    )
    return render_pdf(
        HTML(string=html),
        automatic_download=False,
        download_filename="carnet_digital.pdf",
    )
