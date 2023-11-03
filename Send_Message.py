from Message import TextMessage
from Message import ImageMessage
from Message import VoiceMessage
import requests
import json

from Based.Config import get_config
from ToUpload_File import UpFile

config = "Config/config.yaml"
get_config = get_config(config)

Host = get_config["Host"]
QQBotUid = get_config["QQBotUid"]
devicename = get_config["devicename"]
Myjson = get_config["json"]


url = "http://{}/v1/LuaApiCaller?funcname=MagicCgiCmd&timeout=10&qq={}".format(
    Host, QQBotUid
)
print(url)
text_message = TextMessage(2434221948, 1, "666")

file = UpFile(
    2, "FileUrl", "https://pic1.zhimg.com/v2-e0ca937a1d3296e7463aa0aa096bef48_r.jpg"
)
# print(file.get_file_md5())
# print(file.get_file_id())
# print(file.get_file_size())
voise_file = UpFile(2, "FilePath", "y2232.wav")

print(voise_file.get_file_md5())
print(voise_file.get_file_id())
print(voise_file.get_file_size())
# print(voise_file.get_file_token())
img_message = ImageMessage(2434221948, 1, file.get_file_md5(), file.get_file_size())

voise_message = VoiceMessage(2434221948, 1, voise_file.get_file_md5())


payload = json.dumps(voise_message.get_body())

headers = {
    "User-Agent": "Apifox/1.0.0 (https://apifox.com)",
    "Content-Type": "application/json",
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)
