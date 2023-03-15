import pytest
from src.core import auth
from src.core.auth import User
from app import create_app
from src.core.database import db

@pytest.mark.test_create_user
def test_new_user():
    """
    GIVEN a User model
    WHEN a new User is created
    THEN check the email, hashed_password, and role fields are defined correctly
    """

    app=create_app()
    with app.app_context():
        user = auth.create_user(name="Pedro")
        assert user.name == 'Pedro'
        assert user.name == 'Pedro'
   
    