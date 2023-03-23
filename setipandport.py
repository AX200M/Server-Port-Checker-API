import threading
import time
from time import sleep
import requests
from fastapi import FastAPI

app = FastAPI()
IP = "65.21.130.125"
Port = "8081"

payload = {'remoteAddress': IP, 'portNumber': Port}
r = requests.post('https://ports.yougetsignal.com/check-port.php', params=payload)
#print(r.text)

if "<p><img src=\"/img/flag_red.gif\" alt=\"Closed\" style=\"height: 1em; width: 1em;\" />" in r.text:
    print("Not Open")

else:
    print("Port Open")
