from flask import session, Response
from flask import abort
from werkzeug.exceptions import Unauthorized
from src.core.permissions.role import Role
from src.core.permissions.permission import Permission
from src.core.auth.user import User
from functools import wraps


def has_permission(permission):
    """Determines if an user has the permission specified in the given parameter


    Args:
        permission (int): Permission Identifier

    Returns:
        bool: True if the user has the permission, otherwise returns False.
    """
    user = User.query.filter_by(email=session["user"]).first()

    permiso = Permission.query.filter_by(nombre=permission).first()
    for rol in user.roles:
        if permiso in rol.permisos:
            return True
    return False


def has_role(rol):
    """Determines if an user has the specified role

    Args:
        rol (int): Rol Model Identifier

    Returns:
        bool: True if the user has the role, otherwise returns False.
    """
    user = User.query.filter_by(email=session["user"]).first()
    res = Role.query.filter_by(nombre=rol).first()

    if res in user.roles:
        return True
    return False


def permisson_required(*argumentos):
    def decorator(func):
        @wraps(func)
        def authorize(*args, **kwargs):
            if not session:
                abort(401)

            contador = 0
            for arg in argumentos:
                if has_permission(arg):
                    contador += 1
            if contador == 0:
                abort(401)

            return func(*args, **kwargs)

        return authorize

    return decorator
