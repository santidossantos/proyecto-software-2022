from flask import Flask
from flask import render_template
from src.web.helpers import handlers
from src.core import database
from src.web.config import config
from src.core import seeds
from src.web.controllers.user import users_blueprint
from src.web.controllers.associate import associates_blueprint
from src.web.controllers.auth import auth_blueprint
from src.web.controllers.discipline import discipline_blueprint
from flask import url_for
from flask import redirect
from src.core import auth


def create_app(env="development", static_folder="static"):
    app = Flask(__name__, static_folder=static_folder)

    app.config.from_object(config[env])

    database.init_app(app)

    app.register_blueprint(users_blueprint)
    app.register_blueprint(auth_blueprint)
    app.register_blueprint(associates_blueprint)
    app.register_blueprint(discipline_blueprint)

    app.register_error_handler(404, handlers.not_found_error)
    app.register_error_handler(500, handlers.internal_server_error)

    @app.get("/")
    def entry_point():
        return redirect(url_for("auth.login"))

    @app.cli.command(name="resetdb")
    def resetdb():
        database.reset_db()

    @app.cli.command(name="seeds")
    def seedsdb():
        seeds.run()

    return app
