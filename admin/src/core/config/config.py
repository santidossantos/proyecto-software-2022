from src.core.database import db


class Config(db.Model):

    __tablename__ = "configuration"
    id = db.Column(db.Integer, primary_key=True, unique=True)
    per_page = db.Column(db.Integer, default=5)
    is_pay_table_active = db.Column(db.Boolean, default=True)
    contact_information = db.Column(db.String(100), default="phone, twitter")
    payment_voucher_text = db.Column(
        db.String(200), default="date, username, assoc_numer, description"
    )
    month_value = db.Column(db.Integer, default=5000)
    recharge_percentaje = db.Column(db.Integer, default=5)

    def update(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)
