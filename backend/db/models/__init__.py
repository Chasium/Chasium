"""
用于声明数据库对象的结构。

每个对象将被声明在单独的python文件中，并统一import到此处。
"""
from db import db


class Test(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True)
    email = db.Column(db.String(120), unique=True)

    def __init__(self, username, email):
        self.username = username
        self.email = email
