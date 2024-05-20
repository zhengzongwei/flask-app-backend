#  Copyright (c)2024. zhengzongwei
#  flask-app-backend is licensed under Mulan PSL v2.
#  You can use this software according to the terms and conditions of the Mulan PSL v2.
#  You may obtain a copy of Mulan PSL v2 at:
#          http://license.coscl.org.cn/MulanPSL2
#  THIS SOFTWARE IS PROVIDED ON AN "AS IS" BASIS, WITHOUT WARRANTIES OF ANY KIND,
#  EITHER EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO NON-INFRINGEMENT,
#  MERCHANTABILITY OR FIT FOR A PARTICULAR PURPOSE.
#  See the Mulan PSL v2 for more details.

import unittest

from app import create_app
from app.dao.authors import AuthorDao
from app.extensions import db
from app.schemas.authors import AuthorSchema


class TestAuthorDao(unittest.TestCase):

    def setUp(self):
        self.app = create_app()
        self.app_context = self.app.app_context()
        self.app_context.push()
        self.author = AuthorDao
        self.author_schema = AuthorSchema(many=True)
        db.create_all()

    def tearDown(self):
        db.session.remove()
        # db.drop_all()
        # self.app_context.pop()

    def test_create_author(self):
        create_author_data = [
            {
                'name': 'NIEANTAI'
            },
            {
                'name': 'HUJINYONG'
            }
        ]
        authors = AuthorSchema().load(create_author_data, many=True)
        self.author.create_author(authors)

    def test_list_author(self):
        author = self.author.list_author()
        # return self.author.list_author()
        print(self.author_schema.dump(author))


if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTest(TestAuthorDao('test_create_author'))
    suite.addTest(TestAuthorDao('test_list_author'))
    runner = unittest.TextTestRunner()
    runner.run(suite)

    # unittest.main()
