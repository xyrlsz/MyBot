class EventData:
    def __init__(self, EventJson: dict) -> None:
        self.__body = EventJson

    def FromUin(self) -> int:
        return self.__body["MsgHead"]["FromUin"]

    def ToUin(self) -> int:
        return self.__body["MsgHead"]["ToUin"]

    def FromType(self) -> int:
        return self.__body["MsgHead"]["FromType"]

    def SenderUin(self) -> int:
        return self.__body["MsgHead"]["SenderUin"]

    def SenderNick(self) -> str:
        return self.__body["MsgHead"]["SenderNick"]

    def GroupCard(self) -> str:
        return self.__body["MsgHead"]["GroupInfo"]["GroupCard"]

    def GroupName(self) -> str:
        return self.__body["MsgHead"]["GroupInfo"]["GroupName"]

    def Content(self) -> str:
        return self.__body["MsgBody"]["Content"]

    def MsgBody(self) -> dict:
        return self.__body["MsgBody"]

    def EventName(self) -> str:
        return self.__body["EventName"]
