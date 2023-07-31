import os

from flask import Flask


def create_app(config: str = None):
    app = Flask(__name__, instance_relative_config=True)

    if config is None:
        app.config.from_pyfile('config.py', silent=True)
    else:
        app.config.from_object(config)

    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    from app.api import api
    app.register_blueprint(api)

    return app