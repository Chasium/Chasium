"""
后端所有的Websocket API。
其模块化设计由自定义类WSHelper实现。
"""
from flask_socketio import (
    SocketIO, send, emit, join_room, leave_room
)
from http_api import config

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


@ws_api.on('createRoom', namespace='/chat')
def updateRoomList(socket_id, user_session):
    rooms = config.active_room.keys()
    ws_api.emit('FireEvent', {'EventName': 'updateRoomList',
                'Data': {'RoomList': rooms}}, namespace='/chat')


'''
1. client request for room_name & room_namespace
2. server respond for allocation of room
3. client send join_room_event
4. server receive join_room_event, join player into room specified
'''


# receiving

'''
@ws_api.on('message')
def handle_message(data):
    print('receive message: ' + data)


@ws_api.on('json')
def handle_message(json):
    print('receive message: ' + str(json))


@ws_api.on('my_event')
def handle_my_custom_event(arg1, arg2, arg3):
    print('received args: ' + arg1 + arg2 + arg3)

# sending


@ws_api.on('message')
def handle_message(message):
    send(message, namespace='/chat')


def ack():
    print('message was received!')


@ws_api.on('my event')
def handle_my_custom_event(json):
    emit('my response', json, callback=ack)

# broadcasting
# passively


@ws_api.on('broadcast')
def broadcast_event(data):
    emit('response', data, broadcast=True, namespace="/chat")

# actively


def some_function():
    ws_api.emit('some event', {'data': 42})


# Rooms: seperate users, 留一個房間接口

@ws_api.on('join')
def on_join(data):
    username = data['username']
    room = data['room']
    join_room(room)
    send(username + ' has entered the room.', to=room)


@ws_api.on('leave')
def on_leave(data):
    username = data['username']
    room = data['room']
    leave_room(room)
    send(username + ' has left the room.', to=room)


class MyCustomNamespace(Namespace):
    def on_connect(self):
        pass


# class namespace
ws_api.on_namespace(MyCustomNamespace('/test'))
'''
