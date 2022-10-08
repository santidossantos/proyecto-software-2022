import bdb
from operator import truediv
import re
from flask import flash
from src.core import auth
from src.core.database import db
from src.core.auth.user import User


def validationEmail(email):
    if re.match(
        "^[(a-z0-9\_\-\.)]+@[(a-z0-9\_\-\.)]+\.[(a-z)]{2,15}$",
        email.lower(),
    ):
        return True
    else:
        flash("Email inválido", "error")
        return False


def validationPassword(password):
    if re.match(
        "^(((?=.*[a-z])(?=.*[A-Z]))|((?=.*[a-z])(?=.*[0-9]))|((?=.*[A-Z])(?=.*[0-9])))(?=.{6,})",
        password,
    ):
        return True
    else:
        flash(
            "contraseña debe tener mayúsculas, minúsculas, números y longitud 6...",
            "error",
        )
        return False


def validationMailAndPass(email, password):
    return validationEmail(email) and validationPassword(password)

# Falta que un usuario pueda modificar solo su contrasenia - LORE
def NotExistingEmail(newEmail):
    try:
        user = db.session.query(User).filter(User.email == newEmail ).first().email
        flash(
            "Ya existe ese email registrado",
            "error",
        )
        return False
    except:
        return True
