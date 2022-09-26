from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


def init_app(app):
    db.init_app(app)


def config_db(app):
    @app.before_first_request
    def init_database():
        db.create_all()

    @app.teardown_request
    def close_session(exception=None):
        db.session.remove()


def reset_db():
    db.drop_all()
    db.create_all()
    print("Done")
