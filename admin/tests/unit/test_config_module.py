from src.core import config


def test_create_config(app, fixture_config):
    config_obj = fixture_config
    assert config_obj.per_page == 1
    assert config_obj.is_pay_table_active == True
    assert config_obj.contact_information == "Twitter"
    assert config_obj.payment_voucher_text == "Texo Recibo de Pago"
    assert config_obj.month_value == 2500
    assert config_obj.recharge_percentaje == 5
