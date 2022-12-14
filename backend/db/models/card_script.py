from sqlalchemy import Column, Integer, String, ForeignKey, Text
from db import db
from db.models.card_template import CardTemplateData


class CardScriptData(db.Model):
    __tablename__ = 'card_script_data'
    id = Column(Integer, primary_key=True, autoincrement=True)
    value = Column(Text(65535))
    card_id = Column(Integer, ForeignKey('card_template_data.id'))

    def __init__(self, value: str, card: CardTemplateData):
        self.value = value
        self.card_id = card.id
