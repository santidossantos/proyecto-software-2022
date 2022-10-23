import uuid
from src.core.database import db
import datetime
import enum
from random import randint

# from src.core.associates import Associate
from sqlalchemy.orm import relationship


class Genero(enum.Enum):
    M = "Masculino"
    F = "Femenino"
    O = "Otro"


class DocumentType(enum.Enum):
    DNI = "Documento Nacional de Identidad"
    LE = "Libreta de Enrolamiento"
    LC = "Librera Civica"


def random_integer():
    min_ = 100000
    max_ = 600000
    rand = randint(min_, max_)

    while Associate.query.filter(uuid == rand).limit(1).first() is not None:
        rand = randint(min_, max_)

    return str(rand)


associates_disciplines = db.Table(
    "user_discipline",  # le quiero poner como nombre "associates_disciplines" pero se rompe todo
    db.Column(
        "associate_id", db.Integer, db.ForeignKey("associates.id"), primary_key=True
    ),
    db.Column(
        "discipline_id", db.Integer, db.ForeignKey("disciplines.id"), primary_key=True
    ),
)


class Associate(db.Model):

    __tablename__ = "associates"
    id = db.Column(db.Integer, primary_key=True, unique=True)
    member_number = db.Column(
        db.String(20), default=random_integer, unique=True, nullable=False
    )
    name = db.Column(db.String(100), nullable=False)
    last_name = db.Column(db.String(100), nullable=False)
    dni = db.Column(db.String(), unique=True, nullable=False)
    address = db.Column(db.String(100), nullable=False)
    active = db.Column(db.Boolean(), default=True, nullable=False)
    defaulter = db.Column(db.Boolean(), default=False, nullable=False)
    mobile_number = db.Column(db.String(10), unique=True)
    email = db.Column(db.String(50), unique=True)
    create_at = db.Column(
        db.DateTime, default=datetime.datetime.now(), onupdate=datetime.datetime.now()
    )
    update_at = db.Column(db.DateTime, default=datetime.datetime.now())
    genero = db.Column(db.Enum(Genero), default="O", nullable=False)
    document_type = db.Column(db.Enum(DocumentType), default="DNI", nullable=False)
    disciplines = db.relationship("Discipline", secondary=associates_disciplines)

    def update(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)
