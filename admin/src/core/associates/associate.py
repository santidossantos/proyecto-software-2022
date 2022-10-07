from src.core.database import db


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
