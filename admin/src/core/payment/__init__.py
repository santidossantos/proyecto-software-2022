from src.core.payment.payment import Payment
from src.core.database import db
from src.core.config.config import Config
from datetime import datetime
from sqlalchemy import asc
from sqlalchemy import desc


def list_payment(page_num, per_page):
    return Payment.query.paginate(page_num, per_page, True)


def list_assoc_payments(id):
    return Payment.query.filter(Payment.associated_id == id)


def list_assoc_payments_order(id):
    return Payment.query.filter(Payment.associated_id == id).order_by(
        asc(Payment.create_at)
    )


def get_payment(id):
    payment = Payment.query.get(id)
    return payment


def get_payment_by_assoc_id_and_month(id_assoc, mes):
    return (
        Payment.query.filter(Payment.associated_id == id_assoc)
        .filter(Payment.mes == mes)
        .first()
    )


def pending_payments(id):
    return Payment.query.filter_by(associated_id=id).order_by(asc(Payment.id))


def payments_impagos(id):
    # filtrar aquellos pagos que esten impagos ordenados descendentemente por año y mes
    return Payment.query.filter_by(associated_id=id).filter_by(state="I").order_by(desc(Payment.AnioNum)).order_by(desc(Payment.mesNum)).first()

def costo_total(costo_disciplines,mes,anio):
    now = datetime.now()
    config = Config.query.first()
    total = config.month_value + costo_disciplines
    if ((now.day >= 1 and now.day <= 10 and mes == now.month and anio==now.year)):
        return total
    else:
        return total + (int(total * (config.recharge_percentaje / 100)))

def costo_total_sin_recargo(costo_disciplines):
    config = Config.query.first()
    total = config.month_value + costo_disciplines
    return total


def update_Payment(id_pago, total):
    payment = get_payment(id_pago)
    print(payment)
    setattr(payment, "state", "P")
    setattr(payment, "total", total)
    db.session.commit()
    return payment


def create_payment(id_associate, mes, total):
    payment = get_payment_by_assoc_id_and_month(id_associate, mes)
    setattr(payment, "state", "P")
    setattr(payment, "total", total)
    db.session.commit()
    return True


def esMoroso(id):
    # verificar si el socio está al dia con las cuotas
    pending_payments = payments_impagos(id)
    if pending_payments:
        return True
    else:
        return False


def mesToInt(mesPago):
    mes = str(mesPago)
    if mes == "Mes.E":
        return 1
    elif mes == "Mes.F":
        return 2
    elif mes == "Mes.M":
        return 3
    elif mes == "Mes.A":
        return 4
    elif mes == "Mes.May":
        return 5
    elif mes == "Mes.Jun":
        return 6
    elif mes == "Mes.Jul":
        return 7
    elif mes == "Mes.Ago":
        return 8
    elif mes == "Mes.S":
        return 9
    elif mes == "Mes.O":
        return 10
    elif mes == "Mes.N":
        return 11
    elif mes == "Mes.D":
        return 12
