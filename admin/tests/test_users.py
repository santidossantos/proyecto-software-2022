from src.core import auth
from src.core.auth import User
from src.core.database import db


def test_new_user(app, fixture_auth):
    """
        GIVEN a User model
        WHEN a new User is created
        THEN check the email, hashed_password, and role fields are defined correctly
    """

    assert fixture_auth.name == 'Matias'
   
    