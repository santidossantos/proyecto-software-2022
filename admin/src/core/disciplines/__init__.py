from src.core.disciplines.discipline import Discipline
from src.core.associates.associate import associates_disciplines
from src.core.database import db
from src.core.payment.payment import Payment
from sqlalchemy import asc

def list_disciplines(page_num, per_page):
    return Discipline.query.order_by(asc(Discipline.id)).paginate(page_num, per_page, True)


def list_disciplines_plain():
    """List all disciplines, but do not paginate them"""
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


def update_discipline(id, name, category, nameInstructors, daysAndHours, monthlyCost):
    discipline = Discipline.query.get(id)
    discipline.name = name
    discipline.category = category
    discipline.nameInstructors = nameInstructors
    discipline.daysAndHours = daysAndHours
    discipline.monthlyCost = monthlyCost
    db.session.commit()
    return discipline

def setStatus(id):
    discipline = get_discipline(id)
    discipline.active = not discipline.active
    db.session.commit()
    return discipline

def isActive(id):
    return get_discipline(id).active


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


def generar_pagos(id):
    mes = ["E", "F", "M"]
    if not (Payment.query.filter_by(associated_id=id).first()):
        for i in mes:
            payment = Payment(associated_id=id, mes=i, total=0)
            db.session.add(payment)
            db.session.commit()
        return payment

    return 1


def IsErasable(id):
    resul = db.session.query(associates_disciplines).filter_by(discipline_id=id).first()
    if resul:
        return False

    return True

def disciplinesCantInscriptions():
    disciplinas = list_disciplines_plain()
    #defino diccionario vacio
    array = []
    #para cada disiciplina cuento cuantos inscriptos tiene
    for dis in disciplinas:
        dic = {}
        cant = db.session.query(associates_disciplines).filter_by(discipline_id=dis.id).count()
        #agrego a dic el id de la disciplina y la cantidad de inscriptos
        dic["disciplina"] = dis.name
        dic["inscriptos"] = cant
        #agrego dic al array
        array.append(dic)
    print(array)
    return array

