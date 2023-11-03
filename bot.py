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
img_file = UpFile(
    1,
    "FileUrl",
    "https://pic3.zhimg.com/v2-11e37bfc3b150e7ad3bffeb6fb6bf203_r.jpg?source=1940ef5c",
)
img_message = ImageMessage(2434221948, 1, img_file.get_file_md5())
send_message(img_message)
