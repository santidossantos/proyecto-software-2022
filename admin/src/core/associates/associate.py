from email.policy import default
from src.core.database import db
import datetime


class Associate(db.Model):

    __tablename__ = "associates"
    id = db.Column(db.Integer, primary_key=True, unique=True)
    name = db.Column(db.String(100))
    last_name = db.Column(db.String(100))
    member_number = db.Column(db.Integer, unique=True)
    dni = db.Column(db.Integer, unique=True)
    address = db.Column(db.String(100))
    active = db.Column(db.Boolean(), default=False)
    mobile_number = db.Column(db.String(10), unique=True)
    email = db.Column(db.String(50), unique=True)
    create_at = db.Column(db.DateTime, default=datetime.datetime.now(), onupdate=datetime.datetime.now())
    update_at = db.Column(db.DateTime, default=datetime.datetime.now())

    def update(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)
