from src.core.database import db


class Role(db.Model):

    __tablename__ = "roles"
    id = db.Column(db.Integer, primary_key=True, unique=True)
    name = db.Column(db.String(255), unique=True)
