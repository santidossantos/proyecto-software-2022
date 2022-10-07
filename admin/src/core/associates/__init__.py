from src.core.associates.associate import Associate
from src.core.database import db


def list_associate(page_num, per_page):
    return Associate.query.paginate(page_num, per_page, True)


def create_user(**kwargs):
    associate = Associate(**kwargs)
    db.session.add(associate)
    db.session.commit()
    return associate


def get_associate(id):
    associate = Associate.query.get(id)
    return associate


def update_associate(id, email, name, last_name, dni, mobile_number, address):
    associate = get_associate(id)
    associate.email = email
    associate.name = name
    associate.last_name = last_name
    associate.dni = dni
    associate.mobile_number = mobile_number
    associate.address = address
    db.session.commit()
    return associate


def usWithUserEmail(email):
    return Associate.query.filter_by(email=email).first()
