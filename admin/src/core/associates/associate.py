import uuid
from src.core.database import db
import datetime
import enum
from random import randint
from sqlalchemy.orm import relationship
from werkzeug.security import generate_password_hash, check_password_hash


class Genero(enum.Enum):
    """Enumerative type which defines gender for an user"""
    
    M = "Masculino"
    F = "Femenino"
    O = "Otro"


class DocumentType(enum.Enum):
    """Enumerative which defines document type for an user"""

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
    db.Column(
        "inscriptionDate",
        db.DateTime,
        default=datetime.datetime.now(),
        onupdate=datetime.datetime.now(),
    ),
)


class Associate(db.Model):
    """A Class to represent an associated"""

    __tablename__ = "associates"
    id = db.Column(db.Integer, primary_key=True, unique=True)
    member_number = db.Column(
        db.String(20), default=random_integer, unique=True, nullable=False
    )
    name = db.Column(db.String(100), nullable=False)
    last_name = db.Column(db.String(100), nullable=False)
    dni = db.Column(db.String(255), unique=True, nullable=False)
    address = db.Column(db.String(100), nullable=False)
    active = db.Column(db.Boolean(), default=True, nullable=False)
    defaulter = db.Column(db.Boolean(), default=False, nullable=False)
    mobile_number = db.Column(db.String(255))
    email = db.Column(db.String(50))
    create_at = db.Column(
        db.DateTime, default=datetime.datetime.now(), onupdate=datetime.datetime.now()
    )
    update_at = db.Column(db.DateTime, default=datetime.datetime.now())
    genero = db.Column(db.Enum(Genero), default="O", nullable=False)
    document_type = db.Column(db.Enum(DocumentType), default="DNI", nullable=False)
    disciplines = db.relationship("Discipline", secondary=associates_disciplines)
    profile_picture = db.Column(db.LargeBinary, nullable=True)
    user_name = db.Column(db.String(50), unique=True)
    password = db.Column(db.String(256))

    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            if key == "password":
                self.set_password(kwargs["password"])
            else:
                setattr(self, key, value)

    def set_password(self, password):
        self.password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password, password)

    def update(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)