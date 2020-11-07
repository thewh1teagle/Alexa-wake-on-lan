import websocket
import time
import base64
import json
from wakeonlan import send_magic_packet as power_on_pc

api_key = '<api_key>'  # https://sinric.com
pc_mac = 'aa:bb:cc:dd:ee:ff'
device_id = "<device_id>"

def on_message(ws, message):
    obj = json.loads(message)
    deviceId = obj['deviceId']
    action = obj['action']
    value = obj['value']
    if deviceId == device_id and value == "ON":
        power_on_pc(pc_mac)
    print(message)


def on_error(ws, error):
    print(error)


def on_close(ws):
    print("### closed ###")
    time.sleep(2)
    initiate()


def on_open(ws):
    print("### Initiating new websocket connection ###")


def initiate():
    raw_api_key = base64.b64encode(f'apikey:{api_key}'.encode('ascii')).decode("ascii")
    websocket.enableTrace(True)

    ws = websocket.WebSocketApp("ws://iot.sinric.com",
            header={'Authorization:' + raw_api_key},
                                on_message=on_message,
                                on_error=on_error,
                                on_close=on_close)
    ws.on_open = on_open

    ws.run_forever()


if __name__ == "__main__":
    print("Alexa wake on lan started...")
    initiate()
