from src.core.auth.user import User
from src.core.permissions.role import Role
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


def update_user(**kwargs):
    user = get_user(kwargs["id"])
    user.update(**kwargs)
    db.session.commit()
    return user


def find_user_by_email(email):
    return User.query.filter_by(email=email).first()



def assigned_roles(user, rolesSelected):
    for rol in rolesSelected:
        user.roles.append(rol)
    db.session.add(user)
    db.session.commit()
    return user


def update_roles(user, rolesSelected):
    user.roles = []
    db.session.commit()
    assigned_roles(user, rolesSelected)
    return user


def usWithUserEmail(email):
    return User.query.filter_by(email=email).first()


def usWithUsername(user_name):
    return User.query.filter_by(user_name=user_name).first()


def setStatus(id):
    user = get_user(id)
    user.active = not user.active
    db.session.commit()
    return user


def NoEsAdmin(id):
    user = get_user(id)
    res = Role.query.filter_by(nombre="Admin").first()

    if res in user.roles:
        return False
    return True


def is_active(id):
    user = get_user(id)
    return not user.active


def list_users_filtered(search_filter, active_filter):
    return User.query.filter(User.active == active_filter).filter(
        User.email.ilike(f"%{search_filter}%")
    )
