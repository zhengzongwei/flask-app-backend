import os
from flask import Flask
from app.initialize.initialize import init_app, init_blueprint
from app.config.config import config as cfg


def create_app(config: str = ''):
    app = Flask(__name__, instance_relative_config=True)

    if config == '':
        app.config.from_object(cfg['develop'])
    else:
        app.config.from_object(cfg[config])

    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass
    init_app(app)
    init_blueprint(app)

    return app
