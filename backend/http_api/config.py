import asyncio
from ws_api import ws_api


class Player:
    def __init__(self, username, session):
        self.username = username
        self.session = session
        self.id = login_user[session]
        self.card = None
        pass
    # username
    # id
    # card
    pass


class Host:
    def __init__(self, username, session):
        self.username = username
        self.session = session
        self.id = login_user[session]
        self.template = []
    # username
    # id
    # template
    pass


class Room:
    def __init__(self, host: Host, id):
        self.__host: Host = host
        self.__playerList: list[Player] = []
        self.__id = id
        pass

    def printDetail(self):
        print('Room ID:', self.__id)
        print('Host:', self.__host)
        print('Players:', self.__playerList)

    def getID(self):
        return self.__id

    def getHost(self):
        return self.__host

    def getPlayers(self):
        return self.__playerList

    def addPlayer(self, player: Player):
        if player not in self.__playerList:
            self.__playerList.append(player)

    # host and player
    def removePlayer(self, player: Player):
        if player in self.__playerList:
            self.__playerList.remove(player)

    def removePlayer(self, playerSession: str):
        for player in self.__playerList:
            if player.session == playerSession:
                self.__playerList.remove(player)

    def notifyPlayer(self, player: Player):
        ws_api.emit('FireEvent', {'EventName': 'ExitRoom',
                                  'Data': {'Room': self.__id, 'User': player.session}}, namespace='/chat')

    def dismissRoom(self):
        for player in self.__playerList:
            self.notifyPlayer(player)
        self.__playerList = []


def getRoom(roomID: int):
    return active_room.get(roomID)


def setRoom(roomID: int, room: Room):
    if roomID in active_room:
        active_room[roomID] = room


async def removeRoom(roomID: int):
    active_room.pop(roomID, None)

active_room: dict[int, Room] = {}
login_user = {}
