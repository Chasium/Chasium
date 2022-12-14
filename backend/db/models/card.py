from sqlalchemy import Column, Integer, ForeignKey, Text
from db import db
from db.models.user import UserData
from db.models.card_template import CardTemplateData


class CardData(db.Model):
    id = Column(Integer, primary_key=True, autoincrement=True)
    value = Column(Text(65535))
    user_id = Column(Integer, ForeignKey('user_data.id'))
    template_id = Column(Integer, ForeignKey('card_template_data.id'))

    def __init__(self, value: str, user: UserData, template: CardTemplateData):
        self.value = value
        self.user_id = user.id
        self.template_id = template.id
