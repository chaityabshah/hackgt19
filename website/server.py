import os

from flask import Flask, render_template, send_from_directory
from flask_cors import CORS
from flask import request
from trajectory import Trajectory
import json



traj = Trajectory()

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
    traj.set_heatmap(int(frame), int(bbid))
    return send_from_directory("assets", "heatmap.png")

@app.route("/getCustomers/<frame>")
def get_customers(frame):
    return json.dumps(traj.get_customers(int(frame)))

@app.route("/getPie/<frame>/<bbid>")
def get_pie(frame, bbid):
    return json.dumps(traj.get_pie(int(frame), int(bbid)))

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, threaded=False)

def get_app():
    return app
