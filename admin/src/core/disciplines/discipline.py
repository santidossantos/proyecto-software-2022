from src.core.database import db

class Discipline(db.Model):

    __tablename__ = "disciplines"
    id = db.Column(db.Integer, primary_key=True, unique=True)
    name = db.Column(db.String(50), unique=True)
    category = db.Column(db.String(50), unique=True)
    nameInstructors = db.Column(db.String(100))
    daysAndHours = db.Column(db.String(100))
    monthlyCost = db.Column(db.String(20))
    active = db.Column(db.Boolean(), default=False)