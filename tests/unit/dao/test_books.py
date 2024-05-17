import unittest
from app.dao.books import BookDao
from app.schemas.books import BookSchema
from app import create_app
from app.extensions.init_db import db


class TestBookDao(unittest.TestCase):
    def setUp(self):
        self.app = create_app()
        self.app_context = self.app.app_context()
        self.app_context.push()
        self.book = BookDao()
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()
        self.app_context.pop()

    def test_create_book(self):
        create_book_data = [
            {
                "name": "C# 程序设计{{$randomInt}}",
                "authors": [
                    {
                        "name": "曾宪权"
                    },
                    {
                        "name": "曹玉松"
                    },
                    {
                        "name": "鄢靖丰"
                    }
                ],
                "isbn": "978730257{{$randomInt}}",
                "publication_date": "2021-02-15"
            }
        ]
        books = BookSchema().load(create_book_data, many=True)
        self.book.create_book(books)

    def test_list_book(self):
        book = self.book.list_book()
        print(book)


if __name__ == '__main__':
    unittest.main()
