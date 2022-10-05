from src.core.database import db

class Discipline(db.Model):

    __tablename__ = "discipline"
    id = db.Column(db.Integer, primary_key=True, unique=True)
    nombre = db.Column(db.String(50), unique=True)
    categoria = db.Column(db.String(50), unique=True)