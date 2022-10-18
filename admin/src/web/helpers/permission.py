from flask import session
from src.core.permissions.role import Role
from src.core.permissions.permission import Permission
from src.core.auth.user import User

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