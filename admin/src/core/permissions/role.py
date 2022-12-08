from src.core.database import db
from src.core.permissions import permission # Muy importante estos import para las tablas intermedias

roles_permissions = db.Table('roles_permissions',
    db.Column('role_id', db.Integer, db.ForeignKey('roles.id'), primary_key=True),
    db.Column('permision_id', db.Integer, db.ForeignKey('permissions.id'), primary_key=True)
)

class Role(db.Model):
    """A class to represent roles used by the users"""

    __tablename__ = 'roles'

    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(255), unique=True, nullable=False)
    permisos = db.relationship("Permission", secondary=roles_permissions)