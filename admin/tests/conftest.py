import pytest
from app import create_app
from src.core import auth


@pytest.fixture
def app():
    app = create_app()
    app.config.update({
        "TESTING": True
    })

    # other setup can go here

    yield app

    # clean up / reset resources here


@pytest.fixture()
def client(app):
    return app.test_client()


@pytest.fixture()
def fixture_auth(app):
    with app.app_context():
        user = auth.create_user(name="Matias")
        yield user
        auth.delete_user(user.id)


     