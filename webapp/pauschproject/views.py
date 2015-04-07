import requests
import json

from django.shortcuts import render

from django.core.context_processors import csrf

def home(request):
    context = {}
    context.update(csrf(request))
    r = requests.post("http://pbridge.adm.cs.cmu.edu:11111/echo",
                       data=json.dumps({"hello" : "hello"}))
    print(r.text)
    return render(request, 'Home.html', context)
