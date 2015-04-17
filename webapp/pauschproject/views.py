from django.shortcuts import render
from django.core.context_processors import csrf
from django.http import HttpResponse
from lumiverse.io import *

from random import random

def home(request):
    context = {}
    context.update(csrf(request))

    update = BridgeUpdate()
    panel = BridgePanel(33, GREEN)
    update.addPanel(panel)

    sendUpdate(update)

    return render(request, 'Home.html', context)

def panel_input(request):
    update = BridgeUpdate()
    panel = BridgePanel(request.GET['index'], [random(), random(), random()])
    update.addPanel(panel)

    sendUpdate(update)

    return HttpResponse()