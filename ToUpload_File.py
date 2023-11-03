"""   
command_id 1好友图片 2群组图片 26好友语音 29群组语音

way 有一下三种：

FilePath  文件本地路径FilePath, FileUrl、Base64Buf不能同时存在

FileUrl 文件网络路径

Base64Buf Base64Buf编码

path 是文件路径或者文件网络路径或者Base64Buf编码
"""
import requests
import json
from Based.Config import get_config

config = "Config/config.yaml"
config_data = get_config(config)  # Renamed the variable to avoid conflict
Host = config_data["Host"]
QQBotUid = config_data["QQBotUid"]
devicename = config_data["devicename"]
Myjson = config_data["json"]


class UpFile:
    def __init__(self, command_id: int, way: str, path: str):
        is_Uplaoded = False
        if way == "FilePath":
            self.__body = {
                "CgiCmd": "PicUp.DataUp",
                "CgiRequest": {
                    "CommandId": command_id,
                    "FilePath": path,
                },
            }
        elif way == "FileUrl":
            self.__body = {
                "CgiCmd": "PicUp.DataUp",
                "CgiRequest": {
                    "CommandId": command_id,
                    "FileUrl": path,
                },
            }
        elif way == "FileBase64":
            self.__body = {
                "CgiCmd": "PicUp.DataUp",
                "CgiRequest": {
                    "CommandId": command_id,
                    "Base64Buf": path,
                },
            }

    def get_body(self) -> dict:
        return self.__body

    def get_info(self) -> dict:
        url = "http://{}/v1/upload?qq={}".format(Host, QQBotUid)

        payload = json.dumps(self.__body)  # Use the constructed body

        headers = {
            "User-Agent": "Apifox/1.0.0 (https://apifox.com)",
            "Content-Type": "application/json",
        }

        response = requests.post(url, headers=headers, data=payload)
        if response.json()["CgiBaseResponse"]["Ret"] == 0 and self.is_Uplaoded == False:
            print("上传成功")
        else:
            print("上传失败")
        # print(response.text)
        if self.is_Uplaoded == False:
            self.is_Uplaoded = True
        return response.json()

    def get_file_md5(self) -> str:
        return self.get_info()["ResponseData"]["FileMd5"]

    def get_file_id(self) -> int:
        return self.get_info()["ResponseData"]["FileId"]

    def get_file_size(self) -> int:
        return self.get_info()["ResponseData"]["FileSize"]

    # def get_file_token(self) -> str:
    #     return self.get_info()["ResponseData"]["FileToken"]


# file = UpFile(
#     2, "FileUrl", "https://pic1.zhimg.com/v2-e0ca937a1d3296e7463aa0aa096bef48_r.jpg"
# )
# print(file.get_file_md5())
# print(file.get_file_id())
# print(file.get_file_size())
