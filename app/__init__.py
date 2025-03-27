from flask import Flask
import configs
import routes


def create_app():
    app = Flask(__name__)

    configs.init_app(app)
    routes.init_app(app)

    return app
