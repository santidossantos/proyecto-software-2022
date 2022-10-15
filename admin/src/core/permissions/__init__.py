from admin.src.core.permissions.permission import Permission
from flask import session
from src.core.database import db
from src.core.auth.user import User

# Recibe un modelo (User o Asoc) 
# y determina si tiene permiso para
def has_permission(permission):
    user_roles = User.query.filter_by(email=session.get('email')).all()


    

    permissions = User.query.filter_by(permission=permission)).first()

