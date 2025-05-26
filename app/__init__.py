from flask import Flask
from flask_cors import CORS
import configs
import routes

def create_app():
    app = Flask(__name__)
    CORS(app)
    configs.init_app(app)
    routes.init_app(app)

    return app
