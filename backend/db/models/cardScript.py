from sqlalchemy import Column, Integer, String
from db import db


class ScriptData(db.Model):
    __tablename__ = 'script_data'
    id = Column(Integer, primary_key=True)
    script = Column(String(1000), unique=False)

    def __init__(self, script):
        self.script = script

    def getId(self):
        return self.id

    def getScript(self):
        return self.script
