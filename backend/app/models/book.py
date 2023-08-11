import datetime

from app.common.common import db
from .base import BaseModel
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship


class Books(BaseModel, db.Model):
    """
    书籍类
    """
    __tablename__ = "db_books"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    comment = db.Column(db.String(200))
    data_publish = db.Column(db.DateTime, default=datetime.datetime.now)
    count_page = db.Column(db.String(10))
    version = db.Column(db.String(10))
    recomLevel = db.Column(db.String(10))
    url = db.Column(db.String(50))
    isbn = db.Column(db.String(80), unique=True, nullable=True)
    is_delete = db.Column(db.Boolean, default=False)
    author = relationship("Author", secondary="book_m2m_author", back_populates='book_id')
    publisher = relationship("Publish", secondary="book_m2m_publish", back_populates='book_id')

    def to_json(self):
        resp_dict = {
            "id": self.id,
            "name": self.name,
            "isbn": self.isbn,
            "author": [author.name for author in self.author],
            "comment": self.comment if self.comment else "",
            "publisher": [publisher.name for publisher in self.publisher],
            "count_page": self.count_page if self.count_page else "",
            "version": self.version if self.version else "",
            "recomLevel": self.recomLevel if self.recomLevel else "",
            "url": self.url if self.url else "",
        }
        return resp_dict


class Author(BaseModel, db.Model):
    __tablename__ = "db_authors"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    phone = db.Column(db.String(11))
    addr = db.Column(db.String(80))
    book_id = relationship("Books", secondary="book_m2m_author", back_populates="author")

    def to_json(self):
        resp_dict = {
            'name': self.name,
        }
        return resp_dict


class Book_m2m_author(BaseModel, db.Model):
    __tablename__ = "book_m2m_author"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    book_id = db.Column(db.Integer, ForeignKey("db_books.id"))
    author_id = db.Column(db.Integer, ForeignKey("db_authors.id"))


class Book_m2m_publish(BaseModel, db.Model):
    __tablename__ = "book_m2m_publish"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    book_id = db.Column(db.Integer, ForeignKey("db_books.id"))
    publish_id = db.Column(db.Integer, ForeignKey("db_publish.id"))


class Publish(BaseModel, db.Model):
    """出版社"""
    __tablename__ = "db_publish"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    book_id = relationship("Books", secondary="book_m2m_publish", back_populates="publisher")
