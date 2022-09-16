"""
后端所有的Http API。
API将分为多个部分，由Flask的蓝图功能实现。
"""
from flask import Flask

http_api = Flask(__name__)
