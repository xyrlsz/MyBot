import requests
import base64
from PIL import Image
from io import BytesIO
import requests
import json
from Based.Stauts import get_Status
from Based.Login import login_QQ

Host = "127.0.0.1:8086"
QQBotUid = "1457362358"
devicename = "李三喵🐱"
json = "1"

login_url = "http://{}/v1/login/getqrcode?qq={}&devicename={}&json={}".format(
    Host, QQBotUid, devicename, json
)

if get_Status():
    print("已登录")
else:
    print("未登录")
    login_QQ()
