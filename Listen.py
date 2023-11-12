import requests
import json
from Based.Config import get_config

config = "Config/config.yaml"
config_data = get_config(config)  # Renamed the variable to avoid conflict
Host = config_data["Host"]
QQBotUid = config_data["QQBotUid"]
devicename = config_data["devicename"]
Myjson = config_data["json"]

import asyncio
import json
import random
import requests
import websockets

from Based.Event import Event
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
from Based.Message import TextWithImageMessage
from Based.Message import CardMessage
from Based.Send_Message import send_message
from Based.ToUpload_File import UpFile

config = "Config/config.yaml"
get_config = get_config(config)

if get_Status(get_config):
    print("已登录")
else:
    print("未登录")
    login_QQ(get_config)


# websocket client
SERCIVE_HOST = Host

# 创建一个异步队列
queue = asyncio.Queue()

receive_forbidden_list = list(get_config["receive_forbidden"])


async def Wsdemo():
    uri = "ws://{}/ws".format(SERCIVE_HOST)
    try:
        async with websockets.connect(uri) as websocket:
            while True:
                greeting = await websocket.recv()
                EventJson = json.loads(greeting)
                EventName = EventJson["CurrentPacket"]["EventName"]
                EventData = EventJson["CurrentPacket"]["EventData"]
                Message = Event(EventJson)
                # 把Message对象放入队列
                if int(Message.getEventData().FromUin()) not in receive_forbidden_list:
                    if str(Message.getEventData().SenderUin()) != str(QQBotUid): 
                        await queue.put(Message)
                else:
                    print("已过滤" + str(Message.getEventData().FromUin()) + "消息")
                    
    except Exception as e:
        # 断线重连
        t = random.randint(5, 8)
        print(f"< 超时重连中... { t}", e)
        await asyncio.sleep(t)
        await Wsdemo()


def Todo(message):
    if message.getEventData().MsgBody() is not None:
        print(message.getEventData().MsgBody())


async def process_message():
    # 从队列里取出Message对象并处理
    while True:
        message = await queue.get()
        # do something with message
        # print(message.getEventData().Content())
        Todo(message)
        queue.task_done()


# 创建一个事件循环
loop = asyncio.get_event_loop()

# 把两个异步函数添加到事件循环
tasks = asyncio.gather(Wsdemo(), process_message())

# 运行
loop.run_until_complete(tasks)

# asyncio.get_event_loop().run_until_complete(Wsdemo())
