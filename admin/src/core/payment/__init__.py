from src.core.payment.payment import Payment
from src.core.database import db


def list_payment(page_num, per_page):
    return Payment.query.paginate(page_num, per_page, True)

def list_assoc_payments(id):
    return Payment.query.filter(Payment.associated_id == id)


def create_payment(**kwargs):
    payment = Payment(**kwargs)
    db.session.add(payment)
    db.session.commit()
    return payment


def get_payment(id):
    payment = Payment.query.get(id)
    return payment
