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
    return update_bridge_state(request)

def panel_input(request):
    try:
        requests.get(toggle_URL + str(request.GET['index']))
        return update_bridge_state(request)
    except:
        return render(request, 'Home.html')
    
def update_bridge_state(request):
    try:
        r = requests.get(state_URL)
        data = json.loads(r.text)
        print(data['win'])
        context = {}
        i = 22
        print("I'M OUTSIDE THE LOOP")

        for panel in data['panels']:
            print("I GET IN THE LOOP")
            red = 255
            green = 255
            blue = 255

            if(panel['active']):
                [red, green, blue] = panel['color']
            context['button'+str(i)] = (red, green, blue)
            i = i - 1
            print(context['button' + str(i + 1)])
        return render(request, 'Home.html', context)
    except:
        return render(request, 'Home.html')