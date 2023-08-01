import datetime

from app.common.db import db
from .base import BaseModel
from sqlalchemy import DDL


class Books(BaseModel, db.Model):
    """
    书籍类
    """
    __tablename__ = "db_books"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    author = db.Column(db.String(50), nullable=False)
    comment = db.Column(db.String(200))
    data_publish = db.Column(db.DateTime, default=datetime.datetime.now)
    count_page = db.Column(db.String(10))
    version = db.Column(db.String(10))
    recomLevel = db.Column(db.String(10))
    url = db.Column(db.String(50))
    publisher = db.Column(db.ForeignKey("db_publish.id"))

    def to_json(self):
        resp_dict = {
            "id": self.id,
            "name": self.name,
            "author": self.author,
            "comment": self.comment if self.comment else "",
            "publisher": self.publisher if self.publisher else "",
            "count_page": self.count_page if self.count_page else "",
            "version": self.version if self.version else "",
            "recomLevel": self.recomLevel if self.recomLevel else "",
            "url": self.url if self.url else "",
        }
        return resp_dict

mysql_autoincrement_start = DDL("ALTER TABLE db_books AUTO_INCREMENT = 1001;")
db.event.listen(Books.__table__, 'after_create', mysql_autoincrement_start)


class Publish(BaseModel, db.Model):
    """出版社"""
    __tablename__ = "db_publish"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    relate_book = db.relationship("Books", backref="relate_publish", lazy="dynamic")
