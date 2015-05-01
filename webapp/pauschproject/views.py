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
    return HttpResponse(json.dumps(get_bridge_state()), content_type='application/json')

    #context = update_bridge_state(request)
    #return HttpResponse(render_to_string('buttons.html', update_bridge_state(request)))

def panel_input(request):
    try:
        r = requests.get(toggle_URL + str(request.GET['index']))
        return HttpResponse(r.text, content_type='application/json')
    except Exception as e:
        return HttpResponse(json.dumps({}), content_type='application/json')

    #try:
    #    requests.get(toggle_URL + str(request.GET['index']))
    #    return HttpResponse(render_to_string('buttons.html', update_bridge_state(request)))
    #except:
    #    return HttpResponse(render_to_string('buttons.html', update_bridge_state(request)))

def get_bridge_state():
    try:
        r = requests.get(state_URL)
        data = json.loads(r.text)
        return data
    except Exception as e:
        return {}

def update_bridge_state(request):
    try:
        r = requests.get(state_URL)
        data = json.loads(r.text)
        context = {}
        i = 22

        for panel in data['panels']:
            red = 0
            green = 0
            blue = 0

            if(panel['active']):
                [red, green, blue] = panel['color']
            context['button'+str(i)] = (red, green, blue)
            i = i - 1
        return context
    except:
        return {}