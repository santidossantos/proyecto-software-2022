from src.core.auth.user import User
from src.core.database import db


def list_users():
    return User.query.all()  # Le pedimos al modelo que resuelva


def create_user(**kwargs):
    user = User(**kwargs)
    db.session.add(user)  # Agrega a la bd el objeto user
    db.session.commit()  # Confirma la transaccion

    return user