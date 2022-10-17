from src.core.database import db
from src.core.auth.user import User

class Discipline(db.Model):

    __tablename__ = "discipline"
    id = db.Column(db.Integer, primary_key=True, unique=True)
    name = db.Column(db.String(50), unique=True)
    category = db.Column(db.String(50), unique=True)
    nameInstructors = db.Column(db.String(100))
    daysAndHours = db.Column(db.String(100))
    monthlyCost = db.Column(db.String(20))
    active = db.Column(db.Boolean(), default=False)

UserDiscipline = db.Table(
    "user_discipline",
    db.Column("user_id", db.Integer, db.ForeignKey("users.id")),
    db.Column("discipline_id", db.Integer, db.ForeignKey("discipline.id")),
)