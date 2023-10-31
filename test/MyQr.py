import requests
import re
import base64
import os
from PIL import Image
from io import BytesIO


def output_to_console(img):
    """将二维码输出到控制台"""
    qr_code = ""
    for y in range(img.height):
        for x in range(img.width):
            color = img.getpixel((x, y))
            if color == 0:  # black
                qr_code += "\033[1;30m" + "▇" + "\033[0m"  # 使用全角黑色方块字符代替"#"
            else:  # white
                qr_code += "\033[1;37m" + "▇" + "\033[0m"
        qr_code += "\n"
    print(qr_code)


def save_to_file(img, filename):
    """将二维码保存为图片文件"""
    path = "二维码登入"
    if not os.path.isdir(path):
        os.mkdir(path)
    img.save(os.path.join(path, filename))


# url = "http://127.0.0.1:8086/v1/login/getqrcode?qq=534413561&devicename=lmys%F0%9F%90%B1&json=1"


Host = "127.0.0.1:8086"
QQBotUid = "1457362358"
devicename = "李三喵🐱"
json = "1"


url = "http://{}/v1/login/getqrcode?qq={}&devicename={}&json={}".format(
    Host, QQBotUid, devicename, json
)
payload = {}
headers = {"User-Agent": "Apifox/1.0.0 (https://apifox.com)"}

response = requests.request("GET", url, headers=headers, data=payload)

data = response.text

parr = re.compile(r'"BQBase64rpic":"(.*?)"')
matches = re.findall(parr, data)
if matches:
    for i, base64_string in enumerate(matches):
        # 将字符串编码为字节类型
        encoded_string = base64_string.encode("utf-8")

        # 将base64编码解码为二进制数据
        decoded_data = base64.b64decode(encoded_string)

        # 使用PIL将二进制数据解码为Image对象
        img = Image.open(BytesIO(decoded_data))
        resized_img = img.resize((100, 50))
        # 输出到控制台或保存为图片文件
        save_to_file(img, f"qrcode{i+1}.jpg")
        output_to_console(resized_img)
else:
    print("未找到匹配的内容")
