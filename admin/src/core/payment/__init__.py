from src.core.payment.payment import Payment
from src.core.database import db
from src.core.config.config import Config
from datetime import datetime


def list_payment(page_num, per_page):
    return Payment.query.paginate(page_num, per_page, True)


def get_payment(id):
    payment = Payment.query.get(id)
    return payment


def pending_payments(id):
    return Payment.query.filter_by(associated_id=id).filter_by(state="I").all()


def costo_total(costo_disciplines):
    now = datetime.now()
    config = Config.query.first()
    total = config.month_value + costo_disciplines
    if now.day >= 1 and now.day <= 10:
        return total
    else:
        return total + config.recharge_percentaje
