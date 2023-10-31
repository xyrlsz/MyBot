import requests
import base64
from PIL import Image
from io import BytesIO
from Based.QR_Cout import print_QR
import requests
import json


Host = "127.0.0.1:8086"
QQBotUid = "1457362358"
devicename = "李三喵🐱"
json = "1"


def login_QQ():
    login_url = "http://{}/v1/login/getqrcode?qq={}&devicename={}&json={}".format(
        Host, QQBotUid, devicename, json
    )
    payload = {}
    headers = {"User-Agent": "Apifox/1.0.0 (https://apifox.com)"}

    response = requests.get(login_url, headers=headers, data=payload)

    """print(response.text)
    """
    response_json = response.json()

    bqbase64rpic = response_json["ResponseData"]["BQBase64rpic"]
    ##print(bqbase64rpic)

    # 将 BQBase64rpic 的内容解码为二进制数据
    bqbinary = base64.b64decode(bqbase64rpic)

    # 将二进制数据转换为图片对象
    bqimage = Image.open(BytesIO(bqbinary))

    bqimage.save("QR.png")
    qr_code = Image.open("QR.png")
    print_QR(qr_code)
