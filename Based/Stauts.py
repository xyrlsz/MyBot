import requests
import json

Host = "127.0.0.1:8086"
QQBotUid = "157362358"
devicename = "李三喵🐱"
json_payload = "1"  # Rename the variable


def get_Status():  # Corrected the function name
    url = f"http://{Host}/v1/LuaApiCaller?funcname=MagicCgiCmd&timeout=10&qq={QQBotUid}"

    payload = json.dumps({"CgiCmd": "ClusterInfo", "CgiRequest": {}})
    headers = {
        "User-Agent": "Apifox/1.0.0 (https://apifox.com)",
        "Content-Type": "application/json",
    }

    response = requests.request("POST", url, headers=headers, data=payload)

    # print(response.text)

    response.json()["CgiBaseResponse"]["Ret"]

    return response.json()["CgiBaseResponse"]["Ret"] == 0
