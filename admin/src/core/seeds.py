from src.core import auth
from src.core import associates
from src.core import disciplines


def run():

    user1 = auth.create_user(email="santi@gmail.com", password="1234")
    user2 = auth.create_user(email="juan@gmail.com", password="1234")
    user3 = auth.create_user(email="pedro@gmail.com", password="1234")
    user4 = auth.create_user(email="sofi@gmail.com", password="1234")
    user5 = auth.create_user(email="lore@gmail.com", password="1234")
    user5 = auth.create_user(email="tincho@gmail.com", password="1234")
    user4 = auth.create_user(email="cata@gmail.com", password="1234")

    asociado1 = associates.create_user(email="asociado@gmail.com")
    disciplina1 = disciplines.create_discipline(name="futbol", category="primera")

    print("Seeds cargados!")
