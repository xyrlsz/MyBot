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
from Based.Message import NormalMessage

from Based.Send_Message import send_message
from Based.ToUpload_File import UpFile

config = "Config/config.yaml"
get_config = get_config(config)

if get_Status(get_config):
    print("已登录")
else:
    print("未登录")
    login_QQ(get_config)


# new_dict_array = [
#     {"Nick": "XYR⊙LSZ ", "Uin": 2434221948},
# ]

# message = TextMessage(797649367, 2, "shabi", new_dict_array)

# img_file = UpFile(2, "FilePath", "QR.png")
# img_message = ImageMessage(
#     797649367,
#     2,
#     img_file.get_file_md5(),
#     img_file.get_file_id(),
#     img_file.get_height(),
#     img_file.get_width(),
# )

# img = ImageMessage(2434221948, 1, img_file.get_file_md5())
# print(img.get_body())
# print(img_file.get_file_md5())
# voice_file = UpFile(29, "FilePath", "ambient-piano-logo-165357.mp3")

# voice_message = VoiceMessage(
#     797649367,
#     2,
#     voice_file.get_file_md5(),
#     voice_file.get_file_size(),
#     voice_file.get_file_token(),
# )
# # print(voice_file.get_file_md5())
# # print(voice_file.get_file_size())
# # print(voice_file.get_file_token())
# send_message(voice_message)


msg = {
    "CgiCmd": "MessageSvc.PbSendMsg",
    "CgiRequest": {
        "ToUin": 2434221948,
        "ToType": 1,
        "Content": "你好",
        "Images": [{"FileMd5": "ZMj7Nx8q9PojeVGcYETM3g==", "FileSize": 544988}],
        # "Video": {
        #     "FileMd5": "yyYmhuZChF7m3M486vG8jw==",
        #     "FileSize": 1732142,
        #     "Url": "30510201000436303402010002049117477c02037a1afd02042f2a56310204654a5a3a0410cb262686e642845ee6dcce3ceaf1bc8f02037a1db902010004140000000866696c65747970650000000431303031",
        # },
    },
}
send_message(NormalMessage(msg))

# send_message(TextMessage(2434221948, 1, "你好"))
