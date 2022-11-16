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
    O = "Octubre"
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
    #pasar mes actual a numero integer
    i = datetime.datetime.now().month
    mes = ["E", "F", "M", "A", "May", "Jun", "Jul", "Ago", "S", "O", "N", "D"]
    #crear registro de pago para cada mes desde el mes actual hasta diciembre
    for i in range(i, 12):
        payment = Payment(associated_id=id_user, mes=mes[x], total=0)
        db.session.add(payment)
        db.session.commit()