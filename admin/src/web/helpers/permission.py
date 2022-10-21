from flask import session, Response
from flask import abort
from werkzeug.exceptions import Unauthorized
from src.core.permissions.role import Role
from src.core.permissions.permission import Permission
from src.core.auth.user import User
from functools import wraps


def has_permission(permission):
    user = User.query.filter_by(email=session["user"]).first()

    permiso = Permission.query.filter_by(nombre=permission).first()
    for rol in user.roles:
        if permiso in rol.permisos:
            return True
    return False


def has_role(rol):
    user = User.query.filter_by(email=session["user"]).first()
    res = Role.query.filter_by(nombre=rol).first()

    if res in user.roles:
        return True
    return False


def role_required(role_name):
    def decorator(func):
        @wraps(func)
        def authorize(*args, **kwargs):
            if not session or not has_role(role_name):
                abort(401)
            return func(*args, **kwargs)

        return authorize

    return decorator