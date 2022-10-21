from src.core.database import db
from src.core.config.config import Config


def create(**kwargs):
    config = Config(**kwargs)
    db.session.add(config)
    db.session.commit()
    return config


def get_config():
    config = Config.query.first()
    return config


def update_config(**kwargs):
    get_config().update(**kwargs)
    db.session.commit()
    return True


def get_per_page():
    return int(get_config().per_page)


def get_pay_table_status():
    return get_config().is_pay_table_active


def get_displayable_contact_info():
    return get_config().contact_information


def get_payment_voucher_description():
    return get_config().payment_voucher_text


def get_month_value():
    return get_config().month_value


def get_recharge_percentaje():
    return get_config().recharge_percentaje
