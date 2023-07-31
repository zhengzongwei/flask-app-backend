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


if __name__ == '__main__':
    # print(get_config('mysql'))
    pass
