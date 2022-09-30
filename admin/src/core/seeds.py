from src.core import auth


def run():

    user1 = auth.create_user(email="santi@gmail.com", password="1234")
    user2 = auth.create_user(email="juan@gmail.com", password="1234")
    user3 = auth.create_user(email="pedro@gmail.com", password="1234")
    user4 = auth.create_user(email="sofi@gmail.com", password="1234")
    user5 = auth.create_user(email="lore@gmail.com", password="1234")
    user5 = auth.create_user(email="tincho@gmail.com", password="1234")
    user4 = auth.create_user(email="cata@gmail.com", password="1234")

    print("Seeds cargados!")
