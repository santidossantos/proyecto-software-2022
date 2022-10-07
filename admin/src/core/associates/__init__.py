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


def update_associate(**kwargs):
    associate = get_associate(kwargs["id"])
    associate.update(**kwargs)
    db.session.commit()
    return associate


def usWithUserEmail(email):
    return Associate.query.filter_by(email=email).first()
