import datetime
from sqlite3 import DatabaseError
from click import DateTime
from src.core import payment
from src.core.payment import Payment
from src.core.associates.associate import Associate
from src.core.associates.associate import associates_disciplines
from src.core.database import db
from sqlalchemy import or_
from src.web.utils.math import random_integer


def list_associate(page_num, per_page, search, active, nroSocio):
    """List all asociates and return them paginated

    Args:
        page_num (int): actual page
        per_page (int): number of registers to show
        search (string): search filters from url
        active (string): active filter from url
        nroSocio (int): associated number
    """

    def activeFilter(active):
        if active:
            return Associate.active == active
        return True

    def searchFilter(search):
        if search and nroSocio:
            return or_(
                Associate.last_name.ilike(f"%{search}%"),
                Associate.member_number.ilike(f"%{search}%"),
            )
        elif search:
            return Associate.last_name.ilike(f"%{search}%")
        return True

    return (
        Associate.query.filter(activeFilter(active))
        .filter(searchFilter(search))
        .paginate(page_num, per_page, True)
    )


def list_associateActiveAndInactive(page_num, per_page, search, nroSocio):
    """List all asociates, even if they are inactive.
    The function returns the records paginated"""

    def searchFilter(search):
        if search and nroSocio:
            return or_(
                Associate.last_name.ilike(f"%{search}%"),
                Associate.member_number.ilike(f"%{search}%"),
            )
        elif search:
            return Associate.last_name.ilike(f"%{search}%")
        return True

    return Associate.query.filter(searchFilter(search)).paginate(
        page_num, per_page, True
    )

    return Associate.query.filter(Associate.active == True).paginate(
        page_num, per_page, True
    )


def list_associate_filtered(search_filter, active_filter):
    """List plain records from the associate model,
    filtered by url fields search field and active filter"""

    def activeFilter(active):
        if active:
            return Associate.active == active
        return True

    def searchFilter(search):
        if search:
            return Associate.last_name.ilike(f"%{search}%")
        return True

    return (
        Associate.query.filter(activeFilter(active_filter))
        .filter(searchFilter(search_filter))
        .all()
    )


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


def cost_disciplines(id, mesPago):
    associate = get_associate(id)
    # recupero aquellas disciplinas de user_disciplines
    total_cost = 0
    for disciplina in associate.disciplines:
        consulta = (
            db.session.query(associates_disciplines)
            .filter_by(associate_id=id, discipline_id=disciplina.id)
            .first()
        )
        datetime = consulta.inscriptionDate.month
        if mesPago >= datetime:
            total_cost += disciplina.monthlyCost
    return total_cost


def getDisciplinas(id, mesPago):
    """Get all disciplines from an associated

    Args:
        id (int): Associated Identifier
        mesPago (int): Payed Month

    Returns: List of disciplines model

    """
    associate = get_associate(id)
    total_cost = 0
    disciplinas = []
    for disciplina in associate.disciplines:
        consulta = (
            db.session.query(associates_disciplines)
            .filter_by(associate_id=id, discipline_id=disciplina.id)
            .first()
        )
        datetime = consulta.inscriptionDate.month
        # retornar un vector de disciplinas cuyo mesPago sea mayor a datetime
        if mesPago >= datetime:
            disciplinas.append(disciplina)
    return disciplinas


def generar_pagos(id):
    mes = ["E", "F", "M", "A", "May", "Jun", "Jul", "Ago", "S", "O", "N", "D"]
    i = datetime.datetime.now().month - 1
    for i in range(i, 12):
        payment = Payment(associated_id=id, mes=mes[i], total=0)
        payment.nroComprobante = random_integer()
        # guardo en payment el numero de mes y de año
        payment.mesNum = i + 1
        payment.AnioNum = datetime.datetime.now().year
        db.session.add(payment)
        db.session.commit()
    return payment


def associates_filtered_payment(nro_or_lastname):
    return Associate.query.filter(Associate.active == True).filter(
        or_(
            Associate.last_name.ilike(f"%{nro_or_lastname}%"),
            Associate.member_number.ilike(f"%{nro_or_lastname}%"),
        )
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


def cantMorosos():
    """This function obtains all defaulter associates"""
    # obtener todos los asociados y guardarlos
    asociados = Associate.query.all()
    # recorrer el vector de asociados, si es moroso aumento cantMorosos, sino aumento cantNoMorosos
    cantMorosos = 0
    cantNoMorosos = 0
    for asociado in asociados:
        if payment.esMoroso(asociado.id):
            cantMorosos += 1
        else:
            cantNoMorosos += 1
    dic = {"morosos": cantMorosos, "noMorosos": cantNoMorosos}
    return dic


def esMoroso(id):
    return payment.esMoroso(id)


def getCantGeneros():
    """
        Counts total associates, distinguished by gender
    Returns:
        int[]: List of total associates, distinguished by gender
    """
    # obtener todos los asociados que sean activos
    asociados = Associate.query.filter(Associate.active == True).all()
    # para cada asociado, obtener su genero y contar cuantos hay de cada uno
    cantHombres = 0
    cantMujeres = 0
    cantOtros = 0
    for asociado in asociados:
        if asociado.genero.value == "Femenino":
            cantMujeres = cantMujeres + 1
        elif asociado.genero.value == "Masculino":
            cantHombres = cantHombres + 1
        elif asociado.genero.value == "Otro":
            cantOtros = cantOtros + 1

    total = []
    dic = {}
    dic["hombres"] = cantHombres
    dic["mujeres"] = cantMujeres
    dic["otros"] = cantOtros
    total.append(dic)
    return total


# obtiene cantidad de inscripciones nuevas por mes
def cantidadInscripcionesPorMes():
    """This function calculate and count total inscriptions in a month,
        it only count active associates. It will be used by the
        statistics API

    Returns:
        int[]:  List of total month inscriptions
    """
    # defino todos los meses en un array
    meses = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    # obtengo todos los asociados que sean activos
    asociados = Associate.query.filter(Associate.active == True).all()
    # recorro asociados y para cada uno obtengo el numero de mes de su fecha de inscripcion
    for asociado in asociados:
        # obtengo el numero de mes de la fecha de inscripcion
        mes = asociado.create_at.month
        # agrego el numero de mes al array
        meses[mes-1] = meses[mes-1] + 1
        # defino array con el nomrbe de cada mes
        nombresMeses = [
            "Enero",
            "Febrero",
            "Marzo",
            "Abril",
            "Mayo",
            "Junio",
            "Julio",
            "Agosto",
            "Septiembre",
            "Octubre",
            "Noviembre",
            "Diciembre",
        ]
    # recorro nombre de meses y asigno a cada uno la cantidad de inscripciones
    total = []
    for i in range(0, 12):
        dic = {}
        dic["mes"] = nombresMeses[i]
        dic["cantidad"] = meses[i]
        total.append(dic)
    return total
