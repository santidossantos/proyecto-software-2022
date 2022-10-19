from src.core.database import db
from src.core.associates.associate import Associate

class Discipline(db.Model):

    __tablename__ = "disciplines"
    id = db.Column(db.Integer, primary_key=True, unique=True)
    name = db.Column(db.String(50))
    category = db.Column(db.String(50))
    nameInstructors = db.Column(db.String(100))
    daysAndHours = db.Column(db.String(100))
    monthlyCost = db.Column(db.String(20))
    active = db.Column(db.Boolean(), default=False)

UserDiscipline = db.Table(
    "user_discipline",
    db.Column("associate_id", db.Integer, db.ForeignKey("associates.id"), primary_key=True),
    db.Column("discipline_id", db.Integer, db.ForeignKey("disciplines.id"), primary_key=True),
)