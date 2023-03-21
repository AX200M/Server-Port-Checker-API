import main
import requests
from typing import Union
from fastapi import FastAPI

app = FastAPI()


IP = "65.21.130.125"
Port = "8081"

payload = {'remoteAddress': IP, 'portNumber': Port}

@app.get("/")
def read_root():
    r = requests.post('https://ports.yougetsignal.com/check-port.php', params=payload)
    #print(r.text)

    if (r.text == '<p><img src="/img/flag_red.gif" alt="Closed" style="height: 1em; width: 1em;" /> Port <a href="http://en.wikipedia.org/wiki/Port_8081" target="_blank" />8081</a> is closed on 65.21.130.125.</p>'):
        print("Not Open")

    else:
        print("Port Open")
    return {r.text}