from src.core.disciplines.discipline import Discipline
from src.core.associates.associate import associates_disciplines
from src.core.database import db
from src.core.payment.payment import Payment


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


def createInscription(idAsociado, idDisciplina):
    user_Discipline = associates_disciplines.insert().values(
        associate_id=idAsociado, discipline_id=idDisciplina
    )
    db.session.execute(user_Discipline)
    db.session.commit()
    return user_Discipline


def find_inscription_by_associate_and_discipline(idAssociate, idDiscipline):
    return (
        db.session.query(associates_disciplines)
        .filter_by(associate_id=idAssociate, discipline_id=idDiscipline)
        .first()
    )


# def generar_pagos(id):
#     mes = ["E", "F", "M"]
#     if not (Payment.query.filter_by(associated_id=id).first()):
#         for i in mes:
#             payment = Payment(associated_id=id, mes=i, total=0)
#             db.session.add(payment)
#             db.session.commit()
#         return payment

#     return 1
