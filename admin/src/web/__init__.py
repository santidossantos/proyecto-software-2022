from flask import Flask
from flask import render_template

from src.web.helpers import handlers

# Esta funcion es llamada en app.py
def create_app(env="development", static_folder="static"):

    # Instancio Flask con el nombre de este modulo y
    # la ruta a la carpeta static folder
    app = Flask(__name__, static_folder=static_folder)

    @app.get("/")
    def home():
        return render_template("index.html")

    app.register_error_handler(404, handlers.not_found_error)
    app.register_error_handler(500, handlers.internal_server_error)

    return app
