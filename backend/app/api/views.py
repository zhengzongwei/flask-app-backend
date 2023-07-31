import time

from flask import jsonify

from . import api as api


@api.route("/")
def api_info():
    """
    API 相关信息
    :return:
    """
    data = {"code": 0, "message": 'success', 'data': {}}
    date = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
    api_version = 'v1'
    data['data']['date'] = date
    data['data']['api_version'] = api_version
    return jsonify(data)