from src.core.database import db
from src.core.associates import associate
import datetime
import enum


class Mes(enum.Enum):
    """A class to represent months as enums.They are used in Payment model"""

    E = "Enero"
    F = "Febrero"
    M = "Marzo"
    A = "Abril"
    May = "Mayo"
    Jun = "Junio"
    Jul = "Julio"
    Ago = "Agosto"
    S = "Septiembre"
    O = "Octubre"
    N = "Noviembre"
    D = "Diciembre"



class State(enum.Enum):
    """A class to represent Payment state. Used in Payment model"""
    P = "Pagado"
    I = "Impago"


class Payment(db.Model):
    """A class to represent a Payment from an associated"""

    __tablename__ = "payments"
    id = db.Column(db.Integer, primary_key=True, unique=True)
    associated_id = db.Column(db.Integer, db.ForeignKey("associates.id"))
    mes = db.Column(db.Enum(Mes), nullable=False)
    mesNum = db.Column(db.Integer)
    AnioNum = db.Column(db.Integer)
    total = db.Column(db.Integer)
    state = db.Column(db.Enum(State), default="I", nullable=False)
    nroComprobante = db.Column(db.Integer, unique=True)

    update_at = db.Column(
        db.DateTime, default=datetime.datetime.now(), onupdate=datetime.datetime.now()
    )
    create_at = db.Column(
        db.DateTime, default=datetime.datetime.now(), onupdate=datetime.datetime.now()
    )


def update(self, **kwargs):
    for key, value in kwargs.items():
        setattr(self, key, value)


def create_month_registers(id_user):
    """
    Creates all the initial registers from the actual date to the end of the year,
    those registers represents the months that an associated should pay

    Args:
        id_user (int): associated identifier
    """
    
    i = datetime.datetime.now().month
    mes = ["E", "F", "M", "A", "May", "Jun", "Jul", "Ago", "S", "O", "N", "D"]
    for i in range(i, 12):
        payment = Payment(associated_id=id_user, mes=mes[x], total=0)
        db.session.add(payment)
        db.session.commit()