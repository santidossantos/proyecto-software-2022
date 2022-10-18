from src.core.database import db
from src.core.associates import associate
import datetime


class Payment(db.Model):

    __tablename__ = "payments"
    id = db.Column(db.Integer, primary_key=True, unique=True)
    total = db.Column(db.Integer)
    date = db.Column(
        db.DateTime, default=datetime.datetime.now(), onupdate=datetime.datetime.now()
    )
    create_at = db.Column(
        db.DateTime, default=datetime.datetime.now(), onupdate=datetime.datetime.now()
    )

    associated_id = db.Column(db.Integer, db.ForeignKey("associates.id"))
