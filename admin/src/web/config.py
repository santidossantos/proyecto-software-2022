from os import environ


class Config:
    """Base Configuration."""

    SECRET_KEY = "secret"
    DEBUG = False
    TESTING = False
    JWT_SECRET_KEY = "super-secret"
    JWT_TOKEN_LOCATION = "headers"
    PROPAGATE_EXCEPTIONS = True
    JWT_ACCESS_TOKEN_EXPIRES = False


class ProductionConfig(Config):
    """Production configuration"""

    CORS = False
    DB_USER = environ.get("DB_USER")
    DB_PASS = environ.get("DB_PASS")
    DB_HOST = environ.get("DB_HOST")
    DB_NAME = environ.get("DB_NAME")
    SQLALCHEMY_DATABASE_URI = (
        f"postgresql://{DB_USER}:{DB_PASS}@{DB_HOST}:5432/{DB_NAME}"
    )


class DevelopmentConfig(Config):
    """Development configuration"""

    DEBUG = True
    CORS = True
    DB_USER = "postgres"
    DB_PASS = "password"
    DB_HOST = "localhost"
    DB_NAME = "grupo02"
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    SQLALCHEMY_DATABASE_URI = (
        f"postgresql://{DB_USER}:{DB_PASS}@{DB_HOST}:5432/{DB_NAME}"
    )


config = {
    "development": DevelopmentConfig,
    "production": ProductionConfig,
}
