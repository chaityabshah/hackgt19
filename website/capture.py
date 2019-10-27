import websocket
import json
import xmltodict
import time
import pickle
from collections import defaultdict
import threading
import json
import os
import requests

from text_to_speech import play_text_to_speech
from bose_library import set_bass, set_volume, get_bass, get_volume

class Capture:

    def __init__(self):

        self.lock = threading.Lock()
        self.context = None
        try: self.db = json.load(open("log.json", "r"))
        except: self.db = {}

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


        def block_for_volume(val):
            loop = True
            while loop:
                loop = get_volume() != val
            print("good v")

        def block_for_bass(val):
            loop = True
            while loop:
                loop = get_bass() != val
            print("good b")

        def connect(name):
            if self.context != name:
                self.context = None
                if name not in self.db:
                    print("{} connected. New user.".format(name))
                    play_text_to_speech("{} connected. New user.".format(name))
                elif "volume" in self.db[name] and "bass" not in self.db[name]:
                    volume = self.db[name]["volume"][-1]["volume"]
                    set_volume(volume)
                    block_for_volume(volume)
                    print("{} connected. Volume restored to {}.".format(name, volume))
                    play_text_to_speech("{} connected. Volume restored to {}.".format(name, volume))
                elif "volume" not in self.db[name] and "bass" in self.db[name]:
                    bass = self.db[name]["bass"][-1]["bass"]
                    set_bass(bass)
                    block_for_bass(bass)
                    print("{} connected. Bass reduction restored to {}.".format(name, bass))
                    play_text_to_speech("{} connected. Bass reduction restored to {}.".format(name, bass))
                else:
                    volume = self.db[name]["volume"][-1]["volume"]
                    bass = self.db[name]["bass"][-1]["bass"]
                    set_volume(volume)
                    set_bass(bass)
                    block_for_volume(volume)
                    block_for_bass(bass)
                    print(get_bass(), get_volume())
                    print("{} connected. Volume restored to {} and bass reduction restored to {}.".format(name, volume, bass))
                    play_text_to_speech("{} connected. Volume restored to {} and bass reduction restored to {}.".format(name, volume, bass))

                print("{} connected.".format(name))

            self.context = name
            
            
        def try_create(d, key, val):
            if key not in d: d[key] = val

        try:
            self.lock.acquire()
            ts = message["timestamp"]
            if "updates" in message:

                # Volume
                if "volumeUpdated" in message["updates"] and self.context is not None:
                    try_create(self.db[self.context], "volume", [])
                    packet = {"timestamp":ts}
                    packet["volume"] = int(message["updates"]["volumeUpdated"]["volume"]["targetvolume"])
                    packet["muteenabled"] = message["updates"]["volumeUpdated"]["volume"]["muteenabled"] != "false"
                    print(packet)
                    self.db[self.context]["volume"].append(packet)

                # Bass update
                if "bassUpdated" in message["updates"] and self.context is not None:
                    response = requests.request("GET", "http://192.168.1.174:8090/bass").text
                    bass = int(xmltodict.parse(response, dict_constructor=dict)["bass"]["targetbass"])
                    try_create(self.db[self.context], "bass", [])
                    packet = {"timestamp":ts}
                    packet["bass"] = bass
                    print(packet)
                    self.db[self.context]["bass"].append(packet)


                # nowPlayingUpdated
                if "nowPlayingUpdated" in message["updates"]:
                    npu = message["updates"]["nowPlayingUpdated"]["nowPlaying"]

                    packet = {"timestamp":ts}
                    if (npu["@source"] == "SPOTIFY"
                        and all(x in npu for x in ["track", "artist", "album", "playStatus", "trackID"]) 
                        and npu["track"] is not None
                        and npu["playStatus"] == "PLAY_STATE"):
                        
                        username = npu["@sourceAccount"]
                        if username != "":
                            connect(username)
                            self.context = username
                            try_create(self.db, self.context, {})
                            packet["track"] = npu["track"]
                            packet["artist"] = npu["artist"]
                            packet["album"] = npu["album"]
                            packet["playStatus"] = npu["playStatus"]
                            packet["image"] = npu["art"]["#text"]
                            packet["trackID"] = npu["trackID"]
                            try_create(self.db[self.context], "nowPlaying", [])
                            if len(self.db[self.context]["nowPlaying"]) == 0 or self.db[self.context]["nowPlaying"][-1]["trackID"] != packet["trackID"]:
                                print(packet)
                                self.db[self.context]["nowPlaying"].append(packet)


            json.dump(self.db, open('log.json', 'w'))

        except Exception as e:
            print(e, "died")
            print(message)
        
        self.lock.release()
        #print("released")


if __name__ == "__main__":
    c = Capture()
