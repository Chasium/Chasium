"""
用于声明数据库对象的结构。

每个对象将被声明在单独的python文件中，并统一import到此处。
"""
from db import db

from db.models.user import UserData
from db.models.card_script import CardScriptData
from db.models.card import CardData
from db.models.card_template import CardTemplateData


__all__ = [UserData, CardScriptData, CardData, CardTemplateData]


class Test(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True)
    email = db.Column(db.String(120), unique=True)

    def __init__(self, username, email):
        self.username = username
        self.email = email
