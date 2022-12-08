from src.web.utils.exporters.csv import generate_csv_file
from src.web.utils.exporters.pdf import generate_pdf_file
from src.web.utils.exporters.pdf import generate_pdf_license


def choose_exporter(records, doc_type, qr_url=""):
    """This function selects which exporter should be called, it uses
    the doc_type parameter tho make the decision

    Args:
        records (db.Model): Records to export
        doc_type (str): Type of the file to be generated
        qr_url (str, optional): Used only in generate_pdf_license. Defaults to "".

    Returns:
        _type_: _description_
    """
    if doc_type == "csv":
        return generate_csv_file(records)
    elif doc_type == "pdf":
        return generate_pdf_file(records)
    elif doc_type == "pdf-license":
        return generate_pdf_license(records, qr_url)
