import requests
from typing import Dict
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root(remoteAddress: str, portNumber: int):
    payload = {'remoteAddress': remoteAddress, 'portNumber': portNumber}
    r = requests.post('https://ports.yougetsignal.com/check-port.php', params=payload)
    if "<p><img src=\"/img/flag_red.gif\" alt=\"Closed\" style=\"height: 1em; width: 1em;\" />" in r.text:
        return {"message": "Server Is Offline"}
    else:
        return {"message": "Server Is Online"}
