from random import randint
import uuid
from src.core.payment.payment import Payment

def random_integer():
    min_ = 100000
    max_ = 600000
    rand = randint(min_, max_)

    while Payment.query.filter(uuid == rand).limit(1).first() is not None:
        rand = randint(min_, max_)

    return str(rand)