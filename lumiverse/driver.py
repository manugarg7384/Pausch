#/usr/bin/python
"""
Bridge-side server that drives Lumiverse.

TODO:
Set up interface between server and lumiverse, having a alternate testing interface available.
Create a function to send a request to change the running Pharos show.
"""

import lumiversepython as L
from bottle import route, post, request
from bottle import run as run_bottle

import datetime
import json

DEFAULT_RIG_PATH = '/home/teacher/Lumiverse/PBridge.rig.json'

rig = None

def init_lumiverse(rig_path=DEFAULT_RIG_PATH):
    rig = L.Rig(rig_path)
    rig.init()
    rig.run()
    rig.getAllDevices().setColorRGBRaw("color", 1, 0, 0)
    return rig

@post('/update')
def server_update():
    """Accepts a list of actions, where each action is
    {'selector': selector, 'rgb': [r, g, b]}"""
    params = json.load(request.body)
    for action in params['data']:
        [r, g, b] = action['rgb']
        rig.select(action['selector']).setColorRGBRaw("color", r, g, b)
    return "success"

@route('/test/<selector>/<r>/<g>/<b>')
def server_test(selector, r, g, b):
    r = float(r)
    g = float(g)
    b = float(b)
    rig.select(selector).setColorRGBRaw("color", r, g, b)
    return "success: {}=({},{},{})".format(selector, r, g, b)

@route('/echo')
@post('/echo')
def server_echo():
    """Echos request body with current time for testing."""
    params = json.load(request.body)
    return str(datetime.datetime.now()) + " " + str(params)

def run_bridge_server(port=11111, handler=None):
    run_bottle(host='0.0.0.0', port=port)

if __name__ == '__main__':
    # global
    rig = init_lumiverse()
    run_bridge_server()
