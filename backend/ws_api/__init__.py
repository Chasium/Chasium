"""
后端所有的Websocket API。
其模块化设计由自定义类WSHelper实现。
"""
from flask_socketio import (
    SocketIO, send, emit, join_room, leave_room
)
from engineio.payload import Payload

Payload.max_decode_packets = 100

ws_api = SocketIO()


@ws_api.on('join', namespace='/chat')
def connect_by_client(session):
    join_room(session)
    ws_api.emit('FireEvent', {'EventName': 'connected'},
                namespace='/chat', to=session)


@ws_api.on('leave', namespace='/chat')
def disconnect_by_client(session):
    ws_api.emit('FireEvent', {'EventName': 'disconnected'},
                namespace='/chat', to=session)
    leave_room(session)


@ws_api.on('test', namespace='/chat')
def test(socket_id, user_session):
    print('test from client ' + socket_id)
    print('user: ' + user_session)
    ws_api.emit('FireEvent', {'EventName': 'response',
                'Data': {'Msg': 'ok', 'User': user_session}}, namespace='/chat', to=user_session)


'''
    Room socket functions.
'''


@ws_api.on('createRoom', namespace='/chat')
def updateRoom():
    print('broadcast!')
    ws_api.emit('FireEvent', {'EventName': 'UpdateRoom'},
                namespace='/chat', broadcast=True)


@ws_api.on('joinRoom', namespace='/chat')
def addUserToRoom(roomID, username):
    print('addUserToRoom')
    join_room(roomID)
    ws_api.emit('FireEvent', {'EventName': 'NewMsg',
                'Data': {'Msg': username + ' join the room!'}}, namespace='/chat', to=roomID)


@ws_api.on('leaveRoom', namespace='/chat')
def removeUserFromRoom(roomID, username):
    print('removeUserFromRoom')
    ws_api.emit('FireEvent', {'EventName': 'NewMsg',
                              'Data': {'Msg': username + ' leave the room!'}}, namespace='/chat', to=roomID)
    leave_room(roomID)


@ws_api.on('dismissRoom', namespace='/chat')
def dismissRoom(roomID, username):
    print(username, 'DismissRoom', roomID)
    ws_api.emit('FireEvent', {'EventName': 'DismissRoom'},
                namespace='/chat', to=roomID)


'''
    Drawing
'''


@ws_api.on('joinRoom', namespace='/draw')
def drawerJoinRoom(roomID):
    join_room(roomID)


@ws_api.on('leaveRoom', namespace='/draw')
def drawerLeaveRoom(roomID):
    leave_room(roomID)


@ws_api.on('playerDrawing', namespace='/draw')
def playerDrawing(roomID, x, y, color, type):
    ws_api.emit('UpdateMapDrawing', {'x': x, 'y': y, 'color': color, 'type': type},
                namespace='/draw', include_self=False, to=roomID)


@ws_api.on('cleanMapDrawing', namespace='/draw')
def cleanMapDrawing(roomID):
    ws_api.emit('CleanMapDrawing', namespace='/draw', to=roomID)


@ws_api.on('updateBg', namespace='/draw')
def updateBackgroundImage(roomID, src):
    print('update background')
    ws_api.emit('UpdateBg', {'src': src},
                namespace='/draw', include_self=False, to=roomID)
