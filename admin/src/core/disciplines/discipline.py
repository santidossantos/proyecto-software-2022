from src.core.database import db


class Discipline(db.Model):
    """A class to represent a discipline"""

    __tablename__ = "disciplines"
    id = db.Column(db.Integer, primary_key=True, unique=True)
    name = db.Column(db.String(50))
    category = db.Column(db.String(50))
    nameInstructors = db.Column(db.String(100))
    daysAndHours = db.Column(db.String(100))
    monthlyCost = db.Column(db.Integer)
    active = db.Column(db.Boolean(), default=True)
