from flask import Flask, Blueprint

from .user_routes import user_bp
from .file_routes import file_bp
from .zip_routes import zip_bp

# blueprints = [user_bp, file_bp, zip_bp]
bp_main = Blueprint("matriz", __name__)


def init_app(app: Flask) -> None:
    bp_main.register_blueprint(user_bp)
    bp_main.register_blueprint(file_bp)
    bp_main.register_blueprint(zip_bp)

    app.register_blueprint(bp_main, url_prefix="/api")
