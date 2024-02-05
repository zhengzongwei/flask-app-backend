from flask import Blueprint

from .books import bp as book_bp

books_bp = Blueprint('books',__name__,url_prefix='/books')


def init_book_bps(app) -> None:
    books_bp.register_blueprint(book_bp)
