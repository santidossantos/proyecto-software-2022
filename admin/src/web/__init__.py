from flask import Flask
from flask import render_template
from src.web.helpers import handlers
from src.web.helpers.auth import is_authenticated
from src.core import database
from src.web.config import config
from src.core import seeds
from src.web.controllers.user import users_blueprint
from src.web.controllers.associate import associates_blueprint
from src.web.controllers.auth import auth_blueprint
from src.web.controllers.discipline import discipline_blueprint
from src.web.controllers.pagos import payment_blueprint
from src.web.controllers.config import config_blueprint
from src.web.controllers.inscription import inscription_blueprint
from src.web.controllers.api import api_blueprint
from flask import url_for
from flask import redirect
from src.core import auth
from src.web.helpers import permission as helper_permission
from datetime import datetime 
from src.web.helpers import discipline as helper_discipline
from flask_cors import CORS
from flask_qrcode import QRcode
from flask_jwt_extended import JWTManager


def create_app(env="development", static_folder="static"):
    """Creates the Flask APP and establish its configuration

    Args:
        env (str, optional): Env Config. Defaults to "development".
        static_folder (str, optional): Static Folder Location. Defaults to "static".

    Returns:
        __any__: Flask APP
    """

    app = Flask(__name__, static_folder=static_folder)
  

    app.config.from_object(config[env])

    if app.config['CORS']:
        CORS(app)

    JWTManager(app)

    database.init_app(app)

    app.register_blueprint(users_blueprint)
    app.register_blueprint(auth_blueprint)
    app.register_blueprint(associates_blueprint)
    app.register_blueprint(discipline_blueprint)
    app.register_blueprint(payment_blueprint)
    app.register_blueprint(config_blueprint)
    app.register_blueprint(inscription_blueprint)
    app.register_blueprint(api_blueprint)

    app.register_error_handler(401, handlers.unauthorized)
    app.register_error_handler(404, handlers.not_found_error)
    app.register_error_handler(500, handlers.internal_server_error)

    # Jinja
    app.jinja_env.globals.update(is_authenticated=is_authenticated)
    app.jinja_env.globals.update(has_permission=helper_permission.has_permission)
    app.jinja_env.globals.update(datetime=datetime)
    app.jinja_env.globals.update(find_inscription_by_associate_and_discipline=helper_discipline.find_inscription_by_associate_and_discipline)

    QRcode(app)

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
