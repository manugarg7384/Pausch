from django.shortcuts import render
from django.core.context_processors import csrf

from lumiverse.io import *

def home(request):
    context = {}
    context.update(csrf(request))

    update = BridgeUpdate()
    panel = BridgePanel(33, GREEN)
    update.addPanel(panel)

    sendUpdate(update)

    return render(request, 'Home.html', context)
