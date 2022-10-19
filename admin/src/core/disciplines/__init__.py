from src.core.disciplines.discipline import Discipline
from src.core.database import db


def list_disciplines(page_num, per_page):
    return Discipline.query.paginate(page_num, per_page, True)


def list_disciplines_plain():
    return Discipline.query.all()


def create_discipline(**kwargs):
    discipline = Discipline(**kwargs)
    db.session.add(discipline)
    db.session.commit()
    return discipline


def delete_discipline(id):
    discipline = Discipline.query.get(id)
    db.session.delete(discipline)
    db.session.commit()
    return discipline


def get_discipline(id):
    discipline = Discipline.query.get(id)
    return discipline


# en futuro va haber que implementar lo de kwargs xq sino se va a tener que recibir muchos parametros
def update_discipline(id, name, category, nameInstructors, daysAndHours, monthlyCost):
    discipline = Discipline.query.get(id)
    discipline.name = name
    discipline.category = category
    discipline.nameInstructors = nameInstructors
    discipline.daysAndHours = daysAndHours
    discipline.monthlyCost = monthlyCost
    db.session.commit()
    return discipline
