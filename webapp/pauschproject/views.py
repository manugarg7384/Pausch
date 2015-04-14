import requests
import json

from django.shortcuts import render

from django.core.context_processors import csrf

def home(request):
    context = {}
    context.update(csrf(request))
    r = requests.post("http://pbridge.adm.cs.cmu.edu:11111/update",
                       data=json.dumps({
                           "data": [
                               {
                                   "selector": "$panel=31",
                                   "rgb": [1, 0, 0]
                               }
                                    ]}))
    print(r.text)
    return render(request, 'Home.html', context)
