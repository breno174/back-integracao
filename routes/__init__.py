from flask import Flask

from .user_routes import user_bp
from .file_routes import file_bp
from .zip_routes import zip_bp

blueprints = [user_bp, file_bp, zip_bp]


def init_app(app: Flask) -> None:
    for bp in blueprints:
        app.register_blueprint(bp, url_prefix="/api")
