from src.web.utils.exporters.csv import generate_csv_file
from src.web.utils.exporters.pdf import generate_pdf_file

def choose_exporter(records, doc_type):
    if(doc_type == "csv"):
        return generate_csv_file(records)
    elif(doc_type == "pdf"):
        return generate_pdf_file(records)
