from django.shortcuts import render
from django.core.context_processors import csrf
from django.http import HttpResponse
from lumiverse.io import *

from random import random, randint

def home(request):
    while True:
        update = BridgeUpdate()
        panel = BridgePanel(randint(9, 49), [random(), random(), random()])
        update.addPanel(panel)

        sendUpdate(update)

    return render(request, 'Home.html')

def panel_input(request):
    update = BridgeUpdate()
    panel = BridgePanel(request.GET['index'], [random(), random(), random()])
    update.addPanel(panel)

    sendUpdate(update)

    return HttpResponse()

def get_bridge_state(request):
    r = requests.post(URL)
    return JsonResponse(r.content)