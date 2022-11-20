import random
from .config import Room, active_room, Host


from flask import (
    Blueprint, request
)
from generated.lobby.RoomCreationRequest import RoomCreationRequest


lobby_bp = Blueprint('lobby', __name__, url_prefix='/lobby')
# TODO: Create a class for room storage


@lobby_bp.route("/create", methods=['GET', 'POST'])
def createRoom():
    requestData = RoomCreationRequest(request)
    responseData = {}
    responseData['id'] = -1
    if request.method == 'POST':
        # should use bucket_list
        roomID = random.randint(1, 999999)
        while roomID in active_room:
            roomID = random.randint(1, 999999)
        host = Host(requestData.hostName, requestData.hostSession)
        room = Room(host, roomID)
        active_room[roomID] = room
        for id, room in active_room.items():
            room.printDetail()
        responseData['id'] = roomID

    return responseData


def joinRoom():
    pass
