import websocket
import json
import xmltodict
import time
import pickle
from collections import defaultdict
import threading
import json
import os

class Capture:

    def __init__(self):

        self.lock = threading.Lock()
        try: self.db = json.load(open("log.json", "r"))
        except: self.db = defaultdict(lambda: defaultdict(list))
        print(self.db)

        def on_message(ws, message):
            data = xmltodict.parse(message, dict_constructor=dict)
            data["timestamp"] = int(time.time())
            self.switch(data)


        def on_error(self, ws, error):
            print(error)

        def on_close(self, ws):
            print("### closed ###")

        self.ws = websocket.WebSocketApp("ws://192.168.1.174:8080/", subprotocols=["gabbo"],
                              on_message = on_message,
                              on_error = on_error,
                              on_close = on_close)                              
        self.ws.run_forever()

    def switch(self, message):
        self.lock.acquire()
        ts = message["timestamp"]
        if "updates" in message:
            deviceID = message["updates"]["@deviceID"]
            if "volumeUpdated" in message["updates"]:
                self.db[deviceID]["volume"].append((int(message["updates"]["volumeUpdated"]["volume"]["targetvolume"]), ts))
                self.db[deviceID]["muteenabled"].append((bool(message["updates"]["volumeUpdated"]["volume"]["muteenabled"]), ts))
        with open("log.json", "w") as f:
            json.dump(self.db, f)
        self.lock.release()


if __name__ == "__main__":
    c = Capture()
