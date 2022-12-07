from src.core.database import db


class Permission(db.Model):
    """A class to represent permission modeling"""

    __tablename__ = 'permissions'
    
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(255), unique=True, nullable=False)
