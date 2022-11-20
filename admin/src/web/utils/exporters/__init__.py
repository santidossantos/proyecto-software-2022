from src.web.utils.exporters.csv import generate_csv_file
from src.web.utils.exporters.pdf import generate_pdf_file
from src.web.utils.exporters.pdf import generate_pdf_license

def choose_exporter(records, doc_type, qr_url=""):
    if(doc_type == "csv"):
        return generate_csv_file(records)
    elif(doc_type == "pdf"):
        return generate_pdf_file(records)
    elif(doc_type == "pdf-license"):
        return generate_pdf_license(records, qr_url)

