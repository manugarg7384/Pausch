from django.shortcuts import render
from django.core.context_processors import csrf
from django.http import HttpResponse
from django.template.loader import render_to_string
from lumiverse.io import *

from random import random, randint

import time
import requests
import json

toggle_URL = 'http://pbridge.adm.cs.cmu.edu:11111/toggle/'
state_URL = 'http://pbridge.adm.cs.cmu.edu:11111/state'

def home(request):
    context = update_bridge_state(request)
    return render(request, 'Home.html', context)

def update(request):
    context = update_bridge_state(request)
    return HttpResponse(render_to_string('buttons.html', update_bridge_state(request)))

def panel_input(request):
    try:
        requests.get(toggle_URL + str(request.GET['index']))
        return HttpResponse(render_to_string('buttons.html', update_bridge_state(request)))
    except:
        return HttpResponse(render_to_string('buttons.html', update_bridge_state(request)))
    
def update_bridge_state(request):
    try:
        r = requests.get(state_URL)
        data = json.loads(r.text)
        context = {}
        i = 22

        for panel in data['panels']:
            red = 255
            green = 255
            blue = 255

            if(panel['active']):
                [red, green, blue] = panel['color']
            context['button'+str(i)] = (red, green, blue)
            i = i - 1
        return context
    except:
        return {}