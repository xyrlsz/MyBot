import requests
import json

from Based.Config import get_config
from Based.ToUpload_File import UpFile

config = "Config/config.yaml"
get_config = get_config(config)

Host = get_config["Host"]
QQBotUid = get_config["QQBotUid"]
devicename = get_config["devicename"]
Myjson = get_config["json"]


def send_message(message):
    url = "http://{}/v1/LuaApiCaller?funcname=MagicCgiCmd&timeout=10&qq={}".format(
        Host, QQBotUid
    )

    payload = json.dumps(message.get_body())

    headers = {
        "User-Agent": "Apifox/1.0.0 (https://apifox.com)",
        "Content-Type": "application/json",
    }

    response = requests.request("POST", url, headers=headers, data=payload)

    print(response.text)
