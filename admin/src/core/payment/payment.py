from src.core.database import db
from src.core.associates import associate
import datetime
import enum


class Mes(enum.Enum):
    E = "Enero"
    F = "Febrero"
    M = "Marzo"
    A = "Abril"
    May = "Mayo"
    Jun = "Junio"
    Jul = "Julio"
    Ago = "Agosto"
    S = "Septiembre"
    O = "Ocutubre"
    N = "Noviembre"
    D = "Diciembre"




class State(enum.Enum):
    P = "Pagado"
    I = "Impago"


class Payment(db.Model):

    __tablename__ = "payments"
    id = db.Column(db.Integer, primary_key=True, unique=True)
    associated_id = db.Column(db.Integer, db.ForeignKey("associates.id"))
    mes = db.Column(db.Enum(Mes), nullable=False)
    total = db.Column(db.Integer)
    state = db.Column(db.Enum(State), default="I", nullable=False)

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
    mes = ["E", "F", "M", "A", "May", "Jun", "Jul", "Ago", "S", "O", "N", "D"]
    for i in mes:
        payment = Payment(associated_id=id_user, mes=i, total=0)
        db.session.add(payment)
        db.session.commit()
