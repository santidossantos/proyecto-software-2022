from src.core.auth.user import User
from src.core.database import db


def list_users(page_num, per_page):
    return User.query.paginate(page_num, per_page, True)


def create_user(**kwargs):
    user = User(**kwargs)
    db.session.add(user)
    db.session.commit()

    return user


def find_user_by_email_and_pass(email, password):
    return User.query.filter_by(email=email, password=password).first()
