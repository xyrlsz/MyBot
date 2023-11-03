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
        self, receiver: int, type: int, file_md5: str, file_size=None, file_token=None
    ):
        self.__body = {
            "CgiCmd": "MessageSvc.PbSendMsg",
            "CgiRequest": {
                "ToUin": receiver,  # 替换成实际的接收者
                "ToType": type,  # 2 表示群组；3 表示私聊
                "Voice": [
                    {
                        "FileMd5": file_md5,
                    }
                ],
            },
        }
        if file_size is not None:
            self.__body["CgiRequest"]["Voice"][0]["FileSize"] = file_size
        if file_token is not None:
            self.__body["CgiRequest"]["Voice"][0]["FileToken"] = file_token

    def get_body(self):
        return self.__body
