import datetime

from app.common.common import db


class BaseModel(object):
    """
    模型基类，为每个模型补充创建时间和更新时间
    """
    creat_time = db.Column(db.DateTime, default=datetime.datetime.now)
    update_time = db.Column(db.DateTime, default=datetime.datetime.now, onupdate=datetime.datetime.now)