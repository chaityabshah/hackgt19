import os

from flask import Flask, render_template, send_from_directory
from flask_cors import CORS
from flask import request
# from trajectory import Trajectory
from parse_data import Parser
import json
import socket 
from capture import Capture
import threading

parser = Parser()
thread = threading.Thread(target=lambda : Capture())
thread.start()

app = Flask(__name__)
CORS(app)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/js/<path:path>")
def send_js(path):
    return send_from_directory("js", path)

@app.route("/css/<path:path>")
def send_css(path):
    return send_from_directory("css", path)

@app.route("/assets/<path:path>")
def send_assets(path):
    return send_from_directory("assets", path)

@app.route("/semantic/<path:path>")
def send_semantic(path):
    return send_from_directory("semantic", path)

@app.route("/updateHeatMap/<frame>/<bbid>")
def update_heat_map(frame, bbid):
    #traj.set_heatmap(int(frame), int(bbid))
    return send_from_directory("assets", "heatmap.png")

@app.route("/getUsers")
def get_users():
    return json.dumps(parser.get_users())

@app.route("/getUserData/<bbid>")
def get_user_data(bbid):
    return json.dumps(parser.get_user_data(bbid))

@app.route("/getTop5/<bbid>")
def get_top_5(bbid):
    return json.dumps(list(parser.get_top_5_for_user(bbid)))

@app.route("/getGenres/<bbid>")
def get_genres(bbid):
    return json.dumps(parser.get_top_genres(bbid))

@app.route("/getValence/<bbid>")
def get_valence(bbid):
    return parser.get_valence(bbid)
    

if __name__ == "__main__":
    try:
        host_name = socket.gethostname() 
        host_ip = socket.gethostbyname(host_name)
    except:
        host_ip = "192.168.1.151"
    print("Hosting on", host_ip)
    app.run(host=host_ip, port=8000, threaded=False)

def get_app():
    return app
