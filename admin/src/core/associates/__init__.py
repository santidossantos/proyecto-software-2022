import datetime
from sqlite3 import DatabaseError

from click import DateTime
from core.payment import Payment
from src.core.associates.associate import Associate
from src.core.associates.associate import associates_disciplines
from src.core.database import db
from sqlalchemy import or_
from src.web.utils.math import random_integer


def list_associate(page_num, per_page, search, active, nroSocio):

    def activeFilter(active):
        if active:
            return (Associate.active == active)
        return True
    
    def searchFilter(search):
        if search and nroSocio:
            return (or_(Associate.last_name.ilike(f"%{search}%"), Associate.member_number.ilike(f"%{search}%")))
        elif search:
            return Associate.last_name.ilike(f"%{search}%")
        return True

    return Associate.query.filter(activeFilter(active)).filter(searchFilter(search)).paginate(page_num, per_page, True)

def list_associateActiveAndInactive(page_num, per_page, search, nroSocio):
    def searchFilter(search):
        if search and nroSocio:
            return (or_(Associate.last_name.ilike(f"%{search}%"), Associate.member_number.ilike(f"%{search}%")))
        elif search:
            return Associate.last_name.ilike(f"%{search}%")
        return True

    return Associate.query.filter(searchFilter(search)).paginate(page_num, per_page, True)


    return Associate.query.filter(Associate.active == True).paginate(
        page_num, per_page, True
    )


def list_associate_filtered(search_filter, active_filter):

    def activeFilter(active):
        if active:
            return (Associate.active == active)
        return True
    
    def searchFilter(search):
        if search:
            return Associate.last_name.ilike(f"%{search}%")
        return True


    return Associate.query.filter(activeFilter(active_filter)).filter(searchFilter(search_filter)).all()



def create_user(**kwargs):
    associate = Associate(**kwargs)
    db.session.add(associate)
    db.session.commit()
    return associate


def get_associate(id):
    associate = Associate.query.get(id)
    return associate


def get_associate_by_user_name(user_name):
    return Associate.query.filter_by(user_name=user_name).first()


def update_associate(**kwargs):
    associate = get_associate(kwargs["id"])
    associate.update(**kwargs)
    db.session.commit()
    return associate


def usWithUserEmail(email):
    return Associate.query.filter_by(email=email).first()

def usWithUserDni(dni):
    return Associate.query.filter_by(dni=dni).first()


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


def cost_disciplines(id,mesPago):
    associate = get_associate(id)
    #recupero aquellas disciplinas de user_disciplines
    total_cost = 0
    for disciplina in associate.disciplines:
                consulta = (
                     db.session.query(associates_disciplines)
                    .filter_by(associate_id=id, discipline_id=disciplina.id)
                    .first()
                 )
                datetime=consulta.inscriptionDate.month
                if mesPago >= datetime:
                     total_cost += disciplina.monthlyCost
    return total_cost

def getDisciplinas(id,mesPago):
    associate = get_associate(id)
    total_cost = 0
    disciplinas = []
    for disciplina in associate.disciplines:
                consulta = (
                     db.session.query(associates_disciplines)
                    .filter_by(associate_id=id, discipline_id=disciplina.id)
                    .first()
                 )
                datetime=consulta.inscriptionDate.month
                #retornar un vector de disciplinas cuyo mesPago sea mayor a datetime
                if mesPago >= datetime:
                    disciplinas.append(disciplina)
    return disciplinas

def generar_pagos(id):
    mes = ["E", "F", "M", "A", "May", "Jun", "Jul", "Ago", "S", "O", "N", "D"]
    i = datetime.datetime.now().month - 1
    for i in range(i, 12):
        payment = Payment(associated_id=id, mes=mes[i], total=0)
        payment.nroComprobante = random_integer()
        db.session.add(payment)
        db.session.commit()
    return payment

def associates_filtered_payment(nro_or_lastname):
    return Associate.query.filter(Associate.active == True).filter(
        or_(Associate.last_name.ilike(f"%{nro_or_lastname}%"), Associate.member_number.ilike(f"%{nro_or_lastname}%"))
    )


def associated_disciplines(id_assoc):
    return get_associate(id_assoc).disciplines

def setDefaulter(id):
    associate = get_associate(id)
    associate.defaulter = True
    db.session.commit()
    return associate

def setNotDefaulter(id):
    associate = get_associate(id)
    associate.defaulter = False
    db.session.commit()
    return associate


def activate(id):
    associate = get_associate(id)
    associate.active = True
    db.session.commit()
    return associate