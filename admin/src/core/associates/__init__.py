from src.core.associates.associate import Associate
from src.core.database import db


def list_associate(page_num, per_page):
    return Associate.query.paginate(page_num, per_page, True)


def create_user(**kwargs):
    associate = Associate(**kwargs)
    db.session.add(associate)
    db.session.commit()
    return associate
