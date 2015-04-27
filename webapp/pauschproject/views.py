from django.shortcuts import render
from django.core.context_processors import csrf
from django.http import HttpResponse
from lumiverse.io import *

from random import random, randint

import time
import requests

toggle_URL = 'http://pbridge.adm.cs.cmu.edu:11111/toggle/'
state_URL = 'http://pbridge.adm.cs.cmu.edu:11111/state/'

def home(request):
    return render(request, 'Home.html')

def panel_input(request):
    try:
        requests.get(toggle_URL + str(request.GET['index']))
        return update_bridge_state(request)
    except:
        return render(request, 'Home.html')
    
def update_bridge_state(request):
    try:
        r = requests.get(state_URL)
        context = {}
        i = 21
        red = 0
        green = 0
        blue = 0
        for panel in r.content['panels']:
            if(panel['active']):
                [red, green, blue] = panel['color']
            context['button'+str(i)] = (red, green, blue)
            i = i - 1
        return render(request, 'Home.html', context)
    except:
        return render(request, 'Home.html')
