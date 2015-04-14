#/usr/bin/python
"""
Bridge-side server that drives Lumiverse.

TODO:
Set up interface between server and lumiverse, having a alternate testing interface available.
"""

import lumiversepython as L
from bottle import route, post, request
from bottle import run as run_bottle

import datetime
import json

DEFAULT_RIG_PATH = '/home/teacher/Lumiverse/PBridge.rig.json'

def init_lumiverse(rig_path=DEFAULT_RIG_PATH):
    rig = L.Rig(rig_path)
    rig.init()
    rig.run()
    rig.select('$panel=31').setColorRGBRaw("color", 1, 0, 0)

@route('/echo')
@post('/echo')
def server_echo():
    """Echos request body with current time for testing."""
    params = json.load(request.body)
    return str(datetime.datetime.now()) + " " + str(params)

def run_bridge_server(port=11111, handler=None):
    run_bottle(host='0.0.0.0', port=port)

if __name__ == '__main__':
    init_lumiverse()
    run_bridge_server()
