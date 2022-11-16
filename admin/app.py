from src.web import create_app
from pathlib import Path
from flask_jwt_extended import JWTManager

static_folder = Path(__file__).parent.joinpath("public")

# Invoca a la funcion del modulo src web
app = create_app(static_folder=static_folder)


def main():
    app.run()  # llama a app de src.web


# "cuando ejecuten este archivo (__name__) llama a la funcion name"
if __name__ == "__main__":
    main()


app.config["JWT_SECRET_KEY"] = "super-secret"
app.config["JWT_TOKEN_LOCATION"] = ["cookies"]
jwt = JWTManager(app)
app.config["PROPAGATE_EXCEPTIONS"] = True
