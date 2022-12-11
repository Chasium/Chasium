import random
from .config import Room, active_room, Host, Player, USER_COLOR
from .room import getRoom, setRoom

from flask import (
    Blueprint, request
)
from generated.lobby.RoomCreationRequest import RoomCreationRequest
from generated.lobby.JoinRoomRequest import JoinRoomRequest


lobby_bp = Blueprint('lobby', __name__, url_prefix='/lobby')


@lobby_bp.route("/create", methods=['GET', 'POST'])
def createRoom():
    requestData = RoomCreationRequest(request)
    responseData = {}
    responseData['id'] = -1
    if request.method == 'POST':
        # TODO: set as string, need to check other var type because of room
        roomID = random.randint(1, 999999)
        while roomID in active_room:
            roomID = random.randint(1, 999999)
        host = Host(requestData.hostName, requestData.hostSession)
        room = Room(host, roomID)
        active_room[roomID] = room
        responseData['id'] = roomID

    return responseData


@lobby_bp.route("/getRooms", methods=['GET', 'POST'])
def getRooms():
    responseData = {}
    responseData['roomID'] = list(active_room.keys())
    return responseData


@lobby_bp.route("/join", methods=['GET', 'POST'])
def joinRoom():
    responseData = {}
    responseData['code'] = -1
    requestData = JoinRoomRequest(request)
    username = requestData.username
    session = requestData.session
    roomID = requestData.roomID
    tempRoom = getRoom(roomID)
    if (tempRoom):
        if (session == tempRoom.getHost().session):
            # host join, do nothing
            responseData['code'] = USER_COLOR[0]
            pass
        else:
            # player join, add to room
            tempRoom.addPlayer(Player(username, session))
            setRoom(roomID, tempRoom)
            index = tempRoom.getIdx()
            responseData['code'] = USER_COLOR[index]

        responseData['code'] = 0

    else:
        # error
        pass
    return responseData
