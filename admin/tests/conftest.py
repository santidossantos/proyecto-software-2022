import pytest
from app import create_app
from src.core import auth
from src.core import disciplines
from src.core import permissions
from src.core import config


@pytest.fixture
def app():
    app = create_app()
    app.config.update({
        "TESTING": True
    })

    yield app
    

@pytest.fixture()
def client(app):
    return app.test_client()


@pytest.fixture()
def fixture_auth(app):

    with app.app_context():
        user = auth.create_user(
            id = 80,
            name ='Matias',
            last_name = 'Robles',
            email = 'matias@gmail.com',
            active = True,
            password = '1234'
        )

        role_admin = permissions.get_role_by_name("admin")
        auth.update_roles(user, [role_admin])

        yield user

        auth.delete_user(user.id)


@pytest.fixture()
def fixture_disciplines(app):

    with app.app_context():
       discipline = disciplines.create_discipline(
            name = "Hockey",
            category = "Categoria 1",
            nameInstructors = "Juan, Pedro, Martina",
            daysAndHours = "Lunes 10AM",
            monthlyCost = 3500,
            active = True,
       )

       yield discipline

       disciplines.delete_discipline(discipline.id)



@pytest.fixture()
def fixture_config(app):

    with app.app_context():
        config_obj = config.create(
            per_page=1, 
            is_pay_table_active = True,
            contact_information = "Twitter",
            payment_voucher_text = "Texo Recibo de Pago",
            month_value =  2500,
            recharge_percentaje = 5,
        )

        yield config_obj

        config.delete(config_obj.id)
    
