from smartapi import SmartConnect
from smartapi import SmartWebSocket
import json


class websocket():
    with open('creds.json') as f:
            creds = json.load(f)
            f.close()
    Live_Data_API = creds['api_key']

    Username = creds['username']

    Password = creds['password']


    obj=SmartConnect(api_key=Live_Data_API)




    data = obj.generateSession(Username,Password)
    refreshToken= data['data']['refreshToken']


    feedToken=obj.getfeedToken()


    userProfile= obj.getProfile(refreshToken)

    FEED_TOKEN=feedToken
    CLIENT_CODE=Username

    token="EXCHANGE|TOKEN_SYMBOL"

    task="mw" # mw|sfi|dp

    ss = SmartWebSocket(FEED_TOKEN, CLIENT_CODE)

    def on_message(ws, message):
        print("Ticks: {}".format(message))

    def on_open(ws):
        print("on open")
    ss.subscribe(task,token)

    def on_error(ws, error):
        print(error)

    def on_close(ws):
        print("Close")

    ss._on_open = on_open
    ss._on_message = on_message
    ss._on_error = on_error
    ss._on_close = on_close

    ss.connect()