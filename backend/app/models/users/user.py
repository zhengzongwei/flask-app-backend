# #!/usr/bin/env python
# # -*- coding: utf-8 -*-
# # @Time    : 2024/2/5 11:28
# # @Author  :  zhengzongwei<zhengzongwei@foxmail.com>
#
# import datetime
# from werkzeug.security import generate_password_hash, check_password_hash
#
# from app.extensions import db
# from app.models.base import BaseModel
#
# class User(db.Model):
#     __tablename__ = "users"
#     id = db.Column(db.Integer, primary_key=True, autoincrement=True, comment='用户ID')
#     username = db.Column(db.String(20), comment='用户名')
#     realname = db.Column(db.String(20), comment='真实名字')
#     avatar = db.Column(db.String(255), comment='头像', default="/static/system/admin/images/avatar.jpg")
#     remark = db.Column(db.String(255), comment='备注')
#     password_hash = db.Column(db.String(128), comment='哈希密码')
#     enable = db.Column(db.Integer, default=0, comment='启用')
#
#     # role = db.relationship('Role', secondary="admin_user_role", backref=db.backref('user'), lazy='dynamic')
#
#     def set_password(self, password):
#         self.password_hash = generate_password_hash(password)
#
#     def validate_password(self, password):
#         return check_password_hash(self.password_hash, password)
