#  Copyright (c)2024. zhengzongwei
#  flask-app-backend is licensed under Mulan PSL v2.
#  You can use this software according to the terms and conditions of the Mulan PSL v2.
#  You may obtain a copy of Mulan PSL v2 at:
#          http://license.coscl.org.cn/MulanPSL2
#  THIS SOFTWARE IS PROVIDED ON AN "AS IS" BASIS, WITHOUT WARRANTIES OF ANY KIND,
#  EITHER EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO NON-INFRINGEMENT,
#  MERCHANTABILITY OR FIT FOR A PARTICULAR PURPOSE.
#  See the Mulan PSL v2 for more details.

# DEBUG = True
# SECRET_KEY = 'dev'
SQLALCHEMY_DATABASE_URI = 'mysql://zhengzongwei:zhengzongwei@106.54.39.146:16030/app'


class Config(object):
    DEBUG = True
    SECRET_KEY = 'dev'


class DevelopmentConfig(Config):
    DEBUG = True
    # SQLALCHEMY_DATABASE_URI = 'mysql://zhengzongwei:zhengzongwei@106.54.39.146:16030/app'
    SQLALCHEMY_DATABASE_URI = 'mysql://root:mysql@127.0.0.1:3306/app'
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
