# tpye 1：好友 2：群聊 3：私聊
class TextMessage:
    def __init__(self, receiver: int, type: int, message: str):
        self.__body = {
            "CgiCmd": "MessageSvc.PbSendMsg",
            "CgiRequest": {
                "ToUin": receiver,  # Replace 88888888 with the actual receiver
                "ToType": type,  # 2 for group; 3 for private chat
                "Content": message,
            },
        }

    def get_body(self):
        return self.__body


class ImageMessage:
    def __init__(self, receiver: int, type: int, file_md5: str, file_size: int = None):
        if file_size is None:
            self.__body = {
                "CgiCmd": "MessageSvc.PbSendMsg",
                "CgiRequest": {
                    "ToUin": receiver,  # Replace 88888888 with the actual receiver
                    "ToType": type,  # 2 for group; 3 for private chat
                    "Images": [
                        {
                            "FileMd5": file_md5,
                        }
                    ],
                },
            }
        else:
            self.__body = {
                "CgiCmd": "MessageSvc.PbSendMsg",
                "CgiRequest": {
                    "ToUin": receiver,  # Replace 88888888 with the actual receiver
                    "ToType": type,  # 2 for group; 3 for private chat
                    "Images": [
                        {
                            "FileMd5": file_md5,
                            "FileSize": file_size,
                        }
                    ],
                },
            }

    def get_body(self):
        return self.__body


class VoiceMessage:
    def __init__(
        self, receiver: int, type: int, file_md5: str, file_size: int, file_token: str
    ):
        self.__body = {
            "CgiCmd": "MessageSvc.PbSendMsg",
            "CgiRequest": {
                "ToUin": receiver,
                "ToType": type,
                "Voice": {
                    "FileMd5": file_md5,
                    "FileSize": file_size,
                    "FileToken": file_token,
                },
            },
        }

    def get_body(self):
        return self.__body
