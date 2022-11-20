from flask import (
    Blueprint, request
)
from .config import active_room, Room
from generated.room.ExitRoomRequest import ExitRoomRequest

room_bp = Blueprint('room', __name__, url_prefix='/room')


# host exit room

# player exit room

@room_bp.route("/exit", methods=['GET', 'POST'])
def exitRoom():
    requestData = ExitRoomRequest(request)
    roomID = int(requestData.roomID)
    responseData = {}
    responseData['code'] = -1
    if request.method == 'POST':
        # TODO: room management
        room: Room = getRoom(roomID)
        if room != None:
            host = room.getHost()
            if (host.session == requestData.userSession):
                removeRoom(roomID)
            else:
                room.removePlayer(requestData.userSession)
                setRoom(roomID, room)
            # try if success
            responseData['code'] = 0
        else:
            print('unknown room')
            responseData['code'] = -2

    return responseData


def getRoom(roomID: int):
    return active_room.get(roomID)


def setRoom(roomID: int, room: Room):
    if roomID in active_room:
        active_room[roomID] = room

def removeRoom(roomID: int):
    active_room.pop(roomID, None)