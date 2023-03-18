from src.core import auth


def test_new_user(app, fixture_auth):
    assert fixture_auth.name == 'Matias'


    