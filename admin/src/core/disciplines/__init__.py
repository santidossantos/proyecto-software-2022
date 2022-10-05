from src.core.disciplines.discipline import Discipline
from src.core.database import db


def list_disciplines(page_num, per_page):
    return Discipline.query.paginate(page_num, per_page, True)


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

#en futuro va haber que implementar lo de kwargs xq sino se va a tener que recibir muchos parametros
def update_discipline(id,nombre,categoria):
    discipline = Discipline.query.get(id)
    discipline.nombre=nombre
    discipline.categoria=categoria
    db.session.commit()
    return discipline
