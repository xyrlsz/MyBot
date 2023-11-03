import requests
import json

# 获取状态


def get_Status(my_config):  # Corrected the function name
    Host = my_config["Host"]
    QQBotUid = my_config["QQBotUid"]
    # devicename = my_config["devicename"]
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
