"""
后端所有的Http API。
API将分为多个部分，由Flask的蓝图功能实现。
"""
from flask import Flask
from . import auth, config, lobby, room, script

http_api = Flask(__name__)
http_api.secret_key = "secret_key"
http_api.register_blueprint(auth.auth_bp)
http_api.register_blueprint(lobby.lobby_bp)
http_api.register_blueprint(room.room_bp)
http_api.register_blueprint(script.script_bp)
