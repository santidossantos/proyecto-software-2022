from functools import wraps
from textwrap import wrap
from flask import abort
from flask import session

#No se le está dando uso
def is_authenticated(session):
    return session.get("user") != None

def login_required(f):
    """Function to manage permissions"""
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if session.get("user") is None:
            return abort(401)
        return f(*args, **kwargs)

    return decorated_function