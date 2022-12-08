from src.core.database import db
from src.core import config

class Config(db.Model):
    """A class to represent the configuration table, it would contains global
    values to be called all arround the system"""

    __tablename__ = "configuration"
    id = db.Column(db.Integer, primary_key=True, unique=True)
    per_page = db.Column(db.Integer, default=5)
    is_pay_table_active = db.Column(db.Boolean, default=True)
    contact_information = db.Column(db.String(100), default="phone, twitter")
    payment_voucher_text = db.Column(
        db.String(200), default="Texto a mostrar en el recibo de pago... (editar)"
    )
    month_value = db.Column(db.Integer, default=5000)
    recharge_percentaje = db.Column(db.Integer, default=5)

    def update(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)
