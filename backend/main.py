"""
后端的入口文件
"""
from distutils.command.config import config
from db.models import Test
from http_api import http_api
from ws_api import ws_api
from db import db

import config
http_api.config.from_object(config)

db.init_app(http_api)


@http_api.route('/')
def test():
    db.session.add(Test('a', 'b'))
    db.session.commit()


if __name__ == '__main__':
    ws_api.run(http_api)
