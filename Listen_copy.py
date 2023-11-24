import requests
import json
from Based.Config import get_config
from Based.Activity import Remove_Msg, Ban_Member, Remove_Member
from Based.Event import Event

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


# websocket client
SERCIVE_HOST = "127.0.0.1:8086"

# 创建一个异步队列
queue = asyncio.Queue()


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
                await queue.put(Message)

    except Exception as e:
        # 断线重连
        t = random.randint(5, 8)
        print(f"< 超时重连中... { t}", e)
        await asyncio.sleep(t)
        await Wsdemo()


def Todo(message: Event):
    if message.getEventData().MsgBody() is not None:
        print(message.getEventData().MsgBody())
    if message.getEventData().Content() == "666":
        Remove_Msg(message)
        # Ban_Member(message.getEventData().FromUin(), message.getEventData().SenderUid())
        # Remove_Member(
        #     message.getEventData().FromUin(), message.getEventData().SenderUid()
        # )


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
