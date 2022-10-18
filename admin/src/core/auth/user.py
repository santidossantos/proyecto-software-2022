from src.core.database import db
from src.core.permissions import role # Importante este import



users_roles = db.Table(
    "users_roles",
    db.Column("user_id", db.Integer, db.ForeignKey("users.id"), primary_key=True),
    db.Column("role_id", db.Integer, db.ForeignKey("roles.id"), primary_key=True),
)


class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True, unique=True)
    name = db.Column(db.String(50), unique=True)
    last_name = db.Column(db.String(50), unique=True)
    email = db.Column(db.String(50), unique=True)
    user_name = db.Column(db.String(50), unique=True)
    password = db.Column(db.String(100))
    active = db.Column(db.Boolean(), default=True, nullable=False)
    roles = db.relationship("Role", secondary=users_roles)

    def update(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)
