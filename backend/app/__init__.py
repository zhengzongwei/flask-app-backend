import os

from flask import Flask
from flask_migrate import Migrate
from app.config.config import config as cfg
from app.common.db import db
from app.models.book import Books, Publish


def create_app(config: str = ''):
    app = Flask(__name__, instance_relative_config=True)

    if config == '':
        app.config.from_object(cfg['develop'])
    else:
        app.config.from_object(cfg[config])

    # try:
    #     os.makedirs(app.instance_path)
    # except OSError:
    #     pass

    db.init_app(app)
    migrate = Migrate(app, db)
    # with app.app_context():
    #     db.create_all()

    from app.api import api
    app.register_blueprint(api)

    return app
