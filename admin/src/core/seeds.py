from src.core import auth


def run():

    user1 = auth.create_user(email="santi@gmail.com", password="1234")
    user2 = auth.create_user(email="juan@gmail.com", password="1234")
    user3 = auth.create_user(email="pedro@gmail.com", password="1234")

    print("Seeds cargados!")
