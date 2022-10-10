from flask_weasyprint import HTML, render_pdf
from flask import render_template
from src.core import auth # vuela


def generate_pdf_file(records):
    
    users = paginated_users = auth.list_users(page_num=1, per_page=4)  # solo para probar

    html = render_template("users/users_list.html", users=users)
    return render_pdf(HTML(string=html))
