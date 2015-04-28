#!/usr/bin/env python
"""
Bridge-side server that drives Lumiverse.

TODO:
Create a function to send a request to change the running Pharos show.
"""

import lumiversepython as L
from bottle import route, post, request
from bottle import run as run_bottle

import datetime
import json
import random
import sys
import threading
import time

DEFAULT_RIG_PATH = '/home/teacher/Lumiverse/PBridge.rig.json'

rig = None
bridge_state = {}
panels = {k: [10 + 2*k, 11 + 2*k] for k in range(0, 19)}
panels[19] = [48, 49, 50]
panels[20] = [51, 52]
panels[21] = [53, 54]

def hsl_to_rgb(H, S, L):
    C = (1 - abs(2 * L - 1)) * S
    H_ = H / 60.
    X = C * (1 - abs(H_ % 2 - 1))
    if 0 <= H_ < 1:
        r1, g1, b1 = C, X, 0
    elif 1 <= H_ < 2:
        r1, g1, b1 = X, C, 0
    elif 2 <= H_ < 3:
        r1, g1, b1 = 0, C, X
    elif 3 <= H_ < 4:
        r1, g1, b1 = 0, X, C
    elif 4 <= H_ < 5:
        r1, g1, b1 = X, 0, C
    else:
        r1, g1, b1 = C, 0, X
    m = L - 0.5 * C
    R, G, B = (r1 + m, g1 + m, b1 + m)

    return (R, G, B)

def random_color():
    r, g, b = hsl_to_rgb(random.uniform(0, 360), 1.0, 0.5)
    return (int(r * 255), int(g * 255), int(b * 255))

def win_show(bridge_state):
    for i in range(1200):
        r, g, b = hsl_to_rgb((i * 10) % 360, 1.0, 0.5)
        rig.select('$panel={}'.format(i % 57 + 1)).setColorRGBRaw('color', r, g, b)
        time.sleep(0.1)
    # start next game
    init_game()

def bridge_render(bridge_state):
    win = True
    for panel in panels:
        for selector in bridge_state['panels'][panel]['selectors']:
            if bridge_state['panels'][panel]['active']:
                r, g, b = bridge_state['panels'][panel]['color']
                rig.select(selector).setColorRGBRaw('color',
                        r / 256., g / 256., b / 256.)
            else:
                rig.select(selector).setColorRGBRaw('color', 0, 0, 0)
                win = False

    if win:
        bridge_state['win'] = True
        t = threading.Thread(target=win_show, args=(bridge_state,))
        t.start()
    else:
        bridge_state['win'] = False


def init_game(randomized=True):
    global bridge_state
    bridge_state = {
            'win': False,
            'panels': [
                {
                    'id': panel,
                    'color': random_color(),
                    'active': random.choice([True, False]) if randomized else True,
                    'selectors': ['$panel=' + str(idx) for idx in panels[panel]]
                }
                for panel in panels
            ]
}

    rig.getAllDevices().setColorRGBRaw('color', 1, 1, 1)
    bridge_render(bridge_state)


def init_lumiverse(rig_path=DEFAULT_RIG_PATH):
    global rig
    rig = L.Rig(rig_path)
    rig.init()
    rig.run()
    init_game()

    return rig


@route('/reset')
@post('/reset')
def server_reset():
    init_game()
    return json.dumps(bridge_state)
    
@route('/toggle/<panel>')
@post('/toggle/<panel>')
def server_toggle(panel):
    if bridge_state['win']:
        return json.dumps(bridge_state)
    here = int(panel)
    left = here - 1
    right = here + 1

    if left in panels:
        bridge_state['panels'][left]['active'] ^= True
    if here in panels:
        bridge_state['panels'][here]['active'] ^= True
    if right in panels:
        bridge_state['panels'][right]['active'] ^= True

    # also updates win state
    bridge_render(bridge_state)

    return json.dumps(bridge_state)

@route('/state')
def server_state():
    return json.dumps(bridge_state)


@route('/echo')
@post('/echo')
def server_echo():
    """Echos request body with current time for testing."""
    params = json.load(request.body)
    return str(datetime.datetime.now()) + " " + str(params)

def run_bridge_server(port=11111):
    # keep the server single threaded so that no locking is necessary
    # around bridge_state
    run_bottle(host='0.0.0.0', port=port, server='paste')

if __name__ == '__main__':
    # global
    rig = init_lumiverse()
    run_bridge_server(port=int(sys.argv[1]) if len(sys.argv) > 1 else 11111)
