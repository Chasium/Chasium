"""
后端所有的Websocket API。
其模块化设计由自定义类WSHelper实现。
"""
from flask_socketio import SocketIO


ws_api = SocketIO()
