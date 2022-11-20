from src.core.payment.payment import Payment
from src.core.database import db
from src.core.config.config import Config
from datetime import datetime
from sqlalchemy import desc
from sqlalchemy import asc


def list_payment(page_num, per_page):
    return Payment.query.paginate(page_num, per_page, True)


def list_assoc_payments(id):
    return Payment.query.filter(Payment.associated_id == id)


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
    return Payment.query.filter_by(associated_id=id).order_by(asc(Payment.id)).all()


def payments_impagos(id):
    # filtrar aquellos pagos que esten impagos
    return Payment.query.filter_by(associated_id=id).filter_by(state="I").all()


def costo_total(costo_disciplines):
    now = datetime.now()
    config = Config.query.first()
    total = config.month_value + costo_disciplines
    if now.day >= 1 and now.day <= 10:
        return total
    else:
        return total + (int(total * (config.recharge_percentaje / 100)))


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

    if len(pending_payments) == 0:
        return False

    pago = get_payment(pending_payments[0].id)
    mes = mesToInt(pago.mes)
    if mes <= datetime.now().month:
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
