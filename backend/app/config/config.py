import os
import toml

BSAE_DIR = os.path.abspath(os.path.dirname(__file__))


def get_config(conf_type=None):
    config = toml.load(BSAE_DIR + "/config.toml")
    return config if conf_type is None else config[conf_type]


class Config(object):
    # BSAE_DIR = os.path.abspath(os.path.dirname(__file__))
    SECRET_KEY = 'dev'
    DEBUG = True
    BABEL_DEFAULT_LOCALE = 'zh'
    BABEL_DEFAULT_TIMEZONE = 'UTC'
    BABEL_TRANSLATION_DIRECTORIES = os.path.join(os.path.abspath(os.path.dirname(BSAE_DIR)), "locale")
    # BABEL_DOMAIN = 'messages'


class DevelopmentConfig(Config):
    DEBUG = True
    HOSTNAME = "123.249.13.235"
    PORT = 16030
    DB_NAME = "bookCity"
    USERNAME = "bookCity"
    PASSWORD = "bookCity"

    SQLALCHEMY_DATABASE_URI = 'mysql+mysqlconnector://%s:%s@%s:%s/%s?charset=utf8' % (
        USERNAME, PASSWORD, HOSTNAME, PORT, DB_NAME)


class ProductionConfig(Config):
    DEBUG = False
    HOSTNAME = "123.249.13.235"
    PORT = 16030
    DB_NAME = "bookCity"
    USERNAME = "bookCity"
    PASSWORD = "bookCity"
    SQLALCHEMY_DATABASE_URI = 'mariadb://%s:%s@%s:%s/%s?charset=utf8mb4' % (
        USERNAME, PASSWORD, HOSTNAME, PORT, DB_NAME)


config = {
    'develop': DevelopmentConfig,
    'production': ProductionConfig
}
