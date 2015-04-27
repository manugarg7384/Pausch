from django.shortcuts import render
from django.core.context_processors import csrf
from django.http import HttpResponse
from lumiverse.io import *

from random import random, randint

import time

def home(request):
    return render(request, 'Home.html')

def panel_input(request):
    update = BridgeUpdate()
    panel = BridgePanel(request.GET['index'], [random(), random(), random()])
    update.addPanel(panel)

    sendUpdate(update)

    return HttpResponse()

def get_bridge_state(request):
    r = requests.post(URL)
    '''
    if(str(r.content).count(' ') == 0): #If all the lights are on
        timeout = time.time() + 60*5 #Play random colors for 5 minutes
        while True:
            update = BridgeUpdate()
            panel = BridgePanel(randint(9, 49), [random(), random(), random()])
            update.addPanel(panel)
            sendUpdate(update)
            
            if time.time() > timeout:
                # TO DO: reload the bridge
                break
    '''
    return JsonResponse(r.content)
