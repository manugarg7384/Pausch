#/usr/bin/python
"""
Bridge-side server that drives Lumiverse.

TODO:
Set up interface between server and lumiverse, having a alternate testing interface available.
"""

import lumiversepython as L
from bottle import route, post, request
from bottle import run as run_bottle

DEFAULT_RIG_PATH = '/home/teacher/Lumiverse/PBridge.rig.json'

def init_lumiverse(rig_path=DEFAULT_RIG_PATH):
    rig = L.Rig(rig_path)
    rig.init()
    rig.run()

@route('/echo')
@post('/echo')
def server_echo():
    return request.json

def run_bridge_server(port=11111, handler=None):
    run_bottle(host='0.0.0.0', port=port)

if __name__ == '__main__':
    init_lumiverse()
    run_bridge_server()
