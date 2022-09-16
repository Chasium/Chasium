"""
后端的入口文件
"""
from http_api import http_api
from ws_api import ws_api
from db import db


db.init_app(http_api)

if __name__ == '__main__':
    ws_api.run(http_api)
