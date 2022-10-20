from src.core.payment.payment import Payment
from src.core.database import db


def list_payment(page_num, per_page):
    return Payment.query.paginate(page_num, per_page, True)


def get_payment(id):
    payment = Payment.query.get(id)
    return payment


def pending_payments(id):
    return Payment.query.filter_by(associated_id=id).filter_by(state="I").all()
