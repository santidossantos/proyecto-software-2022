from src.core.auth.user import User
from src.core.database import db


def list_users(page_num, per_page):
    return User.query.paginate(page_num, per_page, True)


def create_user(**kwargs):
    user = User(**kwargs)
    db.session.add(user)
    db.session.commit()
    return user

def delete_user(id):
    user = User.query.get(id)
    db.session.delete(user)
    db.session.commit()
    return user

def get_user(id):
    user = User.query.get(id)
    return user

#en futuro va haber que implementar lo de kwargs xq sino se va a tener que recibir muchos parametros
def update_user(id,email,password):
    user = User.query.get(id)
    user.email=email
    user.password=password
    db.session.commit()
    return user


def find_user_by_email_and_pass(email, password):
    return User.query.filter_by(email=email, password=password).first()
