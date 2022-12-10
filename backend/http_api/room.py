import asyncio
from flask import (
    Blueprint, request
)
from .config import active_room, Room, getRoom, setRoom, removeRoom
from generated.room.RoomRequest import RoomRequest

room_bp = Blueprint('room', __name__, url_prefix='/room')


@room_bp.route("/exit", methods=['GET', 'POST'])
def exitRoom():
    requestData = RoomRequest(request)
    roomID = int(requestData.roomID)
    responseData = {}
    responseData['code'] = -1
    if request.method == 'POST':
        room: Room = getRoom(roomID)
        if room != None:
            host = room.getHost()
            if (host.session == requestData.userSession):
                asyncio.run(removeRoom(roomID))
                responseData['code'] = 2
            else:
                room.removePlayer(requestData.userSession)
                setRoom(roomID, room)
                responseData['code'] = 1
        else:
            print('unknown room')
            responseData['code'] = -2

    return responseData


@room_bp.route("/check", methods=['GET', 'POST'])
def check():
    requestData = RoomRequest(request)
    roomID = int(requestData.roomID)
    responseData = {}
    responseData['code'] = -1
    if request.method == 'POST':
        room: Room = getRoom(roomID)
        if room != None:
            host = room.getHost()
            responseData['host'] = host.username
            if (host.session == requestData.userSession):
                responseData['code'] = 1
            else:
                playerList = room.getPlayers()
                playerList = [p.session for p in playerList]
                if requestData.userSession in playerList:
                    responseData['code'] = 2
                else:
                    responseData['code'] = -2
        else:
            print('invalid room number')
    return responseData


@room_bp.route("/players", methods=['GET', 'POST'])
def getPlayerNames():
    requestData = RoomRequest(request)
    roomID = int(requestData.roomID)
    responseData = {}
    responseData['code'] = -1
    responseData['players'] = []
    if request.method == 'POST':
        room = active_room.get(roomID)
        responseData['players'] = [p.username for p in room.getPlayers()]
    return responseData
