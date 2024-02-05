#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Time    : 2024/2/4 15:50                              
# @Author  :  zhengzongwei<zhengzongwei@foxmail.com>

# DEBUG = True
# SECRET_KEY = 'dev'
SQLALCHEMY_DATABASE_URI = 'mysql://zhengzongwei:zhengzongwei@106.54.39.146:16030/app'


class Config(object):
    DEBUG = True
    SECRET_KEY = 'dev'


class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'mysql://zhengzongwei:zhengzongwei@106.54.39.146:16030/app'
    BABEL_DEFAULT_LOCALE = 'zh'
    LANGUAGES = ['en', 'zh']


class TestingConfig(Config):
    TESTING = True
    # DATABASE_URI = 'your_test_database_uri_here'


class ProductionConfig(Config):
    # DATABASE_URI = 'your_prod_database_uri_here'
    pass


config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig
}
