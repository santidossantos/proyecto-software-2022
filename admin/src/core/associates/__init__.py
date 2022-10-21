from src.core.associates.associate import Associate
from src.core.associates.associate import associates_disciplines
from src.core.database import db


def list_associate(page_num, per_page):
    return list_associateActive(page_num, per_page)


def list_associateActive(page_num, per_page):
    return Associate.query.filter(Associate.active == True).paginate(
        page_num, per_page, True
    )


def list_associate_filtered(search_filter, active_filter):
    return Associate.query.filter(Associate.active == active_filter).filter(
        Associate.last_name.ilike(f"%{search_filter}%")
    )


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


def delete_user(id):
    user = Associate.query.get(id)
    user.active = not user.active
    db.session.commit()
    return user


def usWithUserEmail(email):
    return Associate.query.filter_by(email=email).first()


def searchByStatus(search_filter, page_num, per_page):
    return Associate.query.filter(Associate.active == search_filter).paginate(
        page_num, per_page, True
    )


def searchBySurname(surname, page_num, per_page):
    return Associate.query.filter(Associate.last_name == surname).paginate(
        page_num, per_page, True
    )


def is_defaulter(id):
    associate = Associate.query.get(id)
    return associate.defaulter


def is_active(id):
    associate = Associate.query.get(id)
    return associate.active


def cost_disciplines(id):
    associate = get_associate(id)
    total_cost = 0
    for disciplina in associate.disciplines:
        total_cost = total_cost + disciplina.monthlyCost
    return total_cost
