"""
用于快速创建数据库的入口文件
"""
from http_api import http_api
import config
from db import db


http_api.config.from_object(config)
db.init_app(http_api)
http_api.app_context().push()

with http_api.app_context():
    db.drop_all()
    db.create_all()
