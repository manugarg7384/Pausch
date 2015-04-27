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
        i = 0
        for [r, g, b] in r.content:
            print(r)
            print(g)
            print(b)
            context['button'+str(i)] = (r, g, b)
            i++
        # Hardcode the states of every button into context
        return render(request, 'Home.html', context)
    except:
        return render(request, 'Home.html')
