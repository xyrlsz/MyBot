import os
import subprocess
import http.client
import requests
import base64
from PIL import Image
from io import BytesIO
import qrcode


exe_path = "OPQBot.exe"
command = "-token"
tokne = "7b4909d1b1af2dcaa46a28250d4f6de8"

subprocess.call([exe_path, command, tokne])
