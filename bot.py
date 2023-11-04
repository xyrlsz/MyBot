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

message = TextMessage(2434221948, 1, "失败")
# img_file = UpFile(
#     1,
#     "FilePath",
#     "./QR.png",
# )
# img_message = ImageMessage(2434221948, 1, img_file.get_file_md5())

voice_file = UpFile(26, "FilePath", "ambient-piano-logo-165357.mp3")

voice_message = VoiceMessage(
    2434221948,
    1,
    voice_file.get_file_md5(),
    voice_file.get_file_size(),
    voice_file.get_file_token(),
)
print(voice_file.get_file_md5())
print(voice_file.get_file_size())
print(voice_file.get_file_token())
send_message(voice_message)
