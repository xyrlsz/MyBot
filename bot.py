import requests
import base64
from PIL import Image
from io import BytesIO
import requests
import json
from Based.Stauts import get_Status
from Based.Login import login_QQ
from Based.Config import get_config
from Based.Message import TextMessage
from Based.Message import ImageMessage
from Based.Message import VoiceMessage
from Based.Send_Message import send_message
from Based.ToUpload_File import UpFile

config = "Config/config.yaml"
get_config = get_config(config)

if get_Status(get_config):
    print("已登录")
else:
    print("未登录")
    login_QQ(get_config)


new_dict_array = [
    {"Nick": "XYR⊙LSZ ", "Uin": 2434221948},
]

message = TextMessage(797649367, 2, "shabi", new_dict_array)

img_file = UpFile(2, "FilePath", "QR.png")
img_message = ImageMessage(
    797649367,
    2,
    img_file.get_file_md5(),
    img_file.get_file_id(),
    img_file.get_height(),
    img_file.get_width(),
)

img = ImageMessage(2434221948, 1, img_file.get_file_md5())
print(img.get_body())
print(img_file.get_file_md5())
voice_file = UpFile(29, "FilePath", "ambient-piano-logo-165357.mp3")

voice_message = VoiceMessage(
    797649367,
    2,
    voice_file.get_file_md5(),
    voice_file.get_file_size(),
    voice_file.get_file_token(),
)
# print(voice_file.get_file_md5())
# print(voice_file.get_file_size())
# print(voice_file.get_file_token())
send_message(voice_message)
