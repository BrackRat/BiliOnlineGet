import websocket
import base64
import requests
import json
import datetime
import time

def get_cid(av):
    response = requests.get("https://api.bilibili.com/x/web-interface/view?aid=" + str(av))
    response.encoding = 'utf-8'
    res = response.text
    # print(res)
    data = json.loads(res)
    c = data['data']['cid']
    # print(c)
    return c

def make_send(av):
    cid = str(get_cid(av))
    res = b'\x00\x00\x00\\\x00\x12\x00\x01\x00\x00\x00\x07\x00\x00\x00\x01\x00\x00{"room_id":"video://' + str(av).encode('utf-8') + '/'.encode('utf-8') + cid.encode('utf-8') + '","platform":"web","accepts":[1000]}'.encode('utf-8')
    return res

def get_online(text):
    cache = text.find(b'"online":')
    # print(cache)
    cache2 = text[cache+9:].find(b',')
    get = int(text[cache+9:cache2+9+cache])
    print(get)
    return get


def connect(plz):
    url = "wss://broadcast.chat.bilibili.com:7823/sub"
    normal = base64.b64decode('AAAAIQASAAEAAAACAAAACQAAW29iamVjdCBPYmplY3Rd') 
    ws = websocket.create_connection(url,timeout=10)
    ws.send(bytes(plz))
    get = ws.recv()
    # print(get)

    ws.send(bytes(normal))
    get = ws.recv()
    # print(get)
    if get.find(b'online') != -1:
        # online = get_online(get)
        online=get_online(get)
        return online
    else :
        print("None")

def get_online_from_av(av):
    send = make_send(av)

    online = connect(send)

    return online


def write_file(onlines,times):
    
    with open(file_name,'a') as file_obj:
      file_obj.write(str(times) + ',' + str(onlines) + '\r')


file_name = str(input("File_Name(a.txt):"))
avid = int(input('AVid(85919470):'))




while True:
    
    online=get_online_from_av(avid)
    now_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    print(now_time)
    write_file(online,now_time)

    
    time.sleep(60)
