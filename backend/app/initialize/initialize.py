import os
from flask import request
from flask_migrate import Migrate
from flask_babel import Babel
from app.common.common import db
from app.common.common import ma
from app.common.logs import Logger
from .db import init_app as init_db

logger = Logger("initialize")


def init_blueprint(app):
    logger.debug("init blueprint")
    from app.api import api
    app.register_blueprint(api)


def init_app(app):
    logger.debug("init app ")

    Babel(app)
    db.init_app(app)
    init_db(app)
    Migrate(app, db)
    ma.init_app(app)


