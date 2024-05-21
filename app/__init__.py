#  Copyright (c)2024. zhengzongwei
#  flask-app-backend is licensed under Mulan PSL v2.
#  You can use this software according to the terms and conditions of the Mulan PSL v2.
#  You may obtain a copy of Mulan PSL v2 at:
#          http://license.coscl.org.cn/MulanPSL2
#  THIS SOFTWARE IS PROVIDED ON AN "AS IS" BASIS, WITHOUT WARRANTIES OF ANY KIND,
#  EITHER EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO NON-INFRINGEMENT,
#  MERCHANTABILITY OR FIT FOR A PARTICULAR PURPOSE.
#  See the Mulan PSL v2 for more details.

import os
from flask import Flask

from app.api import init_bps
from app.conf.conf import config as config
from app.extensions import init_plugs


def create_app():
    app = Flask(__name__, instance_relative_config=True)

    app.config['BABEL_TRANSLATION_DIRECTORIES'] = os.path.join(os.path.abspath(os.path.dirname(__file__)),
                                                               'translations')

    try:
        os.makedirs(os.path.join(os.path.dirname(app.root_path), 'logs'), exist_ok=True)
    except OSError:
        pass
    # 加载配置
    FLASK_ENV = os.environ.get('FLASK_ENV')
    if FLASK_ENV is None or FLASK_ENV not in ['development', 'production', 'testing']:
        app.config.from_object(config['development'])
    else:
        app.config.from_object(config[FLASK_ENV])
    # if app.debug:
    #     app.config.from_object(config['development'])
    # else:
    #     app.config.from_object(config['production'])

    # 注册插件
    init_plugs(app)

    # 注册蓝图
    init_bps(app)
    print(app.url_map)
    # 注册日志
    return app
