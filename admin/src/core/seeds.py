from src.core import auth
from src.core import associates
from src.core import disciplines
from src.core import payment
from src.core import config


def run():

    user1 = auth.create_user(email="santi@gmail.com", password="1234")
    user2 = auth.create_user(email="juan@gmail.com", password="1234")
    user3 = auth.create_user(email="pedro@gmail.com", password="1234")
    user4 = auth.create_user(email="sofi@gmail.com", password="1234")
    user5 = auth.create_user(email="lore@gmail.com", password="1234")
    user5 = auth.create_user(email="tincho@gmail.com", password="1234")
    user4 = auth.create_user(email="cata@gmail.com", password="1234")

    asociado1 = associates.create_user(
        name="sofi",
        last_name="raciti",
        dni="123456",
        address="6 y 62",
        email="asociado@gmail.com",
    )

    disciplines.create_discipline(name="futbol", category="primera")

    payment.create_payment(total=2000)

    config.create()

    print("Seeds cargados!")
