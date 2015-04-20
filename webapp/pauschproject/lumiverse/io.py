import requests
import json

URL = 'http://pbridge.adm.cs.cmu.edu:11111/update'

# Color constants
RED   = [1, 0, 0]
GREEN = [0, 1, 0]
BLUE  = [0, 0, 1]

class BridgePanel(object):
    '''A class representing a panel on the Pausch bridge.'''
    def __init__(self, index, color):
        self.selector = "$panel={}".format(index) 
        self.rgb = color

class BridgeUpdate(object):
    '''The transcational unit for communicating with the bridge.'''
    def __init__(self):
        self.data = []

    def addPanel(self, panel):
        self.data.append(panel)

def sendUpdate(update):
    data = json.dumps(update, default = lambda obj: obj.__dict__)
    r = requests.post(URL, data = data)
