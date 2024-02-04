#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Time    : 2024/2/4 15:50                              
# @Author  :  zhengzongwei<zhengzongwei@foxmail.com>

DEBUG = True
SECRET_KEY = 'dev'
# DATABASE_URI = 'your_database_uri_here'


class Config(object):
    DEBUG = True



class DevelopmentConfig(Config):
    DEBUG = True
    # DATABASE_URI = 'your_dev_database_uri_here'

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