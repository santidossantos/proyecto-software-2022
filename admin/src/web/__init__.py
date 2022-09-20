from flask import Flask
from flask import render_template


def create_app(static_folder):  # Esta funcion es llamada en app.py

    # Instancio Flask con el nombre de este modulo y
    # la ruta a la carpeta static folder
    app = Flask(__name__, static_folder=static_folder)

    @app.get("/")
    def home():
        return render_template("home.html")

    return app
