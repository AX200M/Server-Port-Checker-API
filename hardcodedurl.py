import requests
from typing import Union
from fastapi import FastAPI
from urllib.parse import urlparse, parse_qs

app = FastAPI()

URL='https://pgnserverchecker.onrender.com/?serveraddress=65.21.130.125&serverport=8010'
parse_result = urlparse(URL)
#print(parse_result)
#print(parse_result.query)
dict_result = parse_qs(parse_result.query)
#print(dict_result)
#print(dict_result['serveraddress'][0]) 
#print(dict_result['serverport'][0]) 


IP = (dict_result['serveraddress'][0]) 
Port = (dict_result['serverport'][0]) 
print(IP,Port)

payload = {'remoteAddress': IP, 'portNumber': Port}

@app.get("/")
def read_root():
    r = requests.post('https://ports.yougetsignal.com/check-port.php', params=payload)
    #print(r.text)

    if "<p><img src=\"/img/flag_red.gif\" alt=\"Closed\" style=\"height: 1em; width: 1em;\" />" in r.text:
        return {"message": "Server Is Offline"}

    else:
        return {"message": "Server Is Online"}