from django.shortcuts import render

from django.core.context_processors import csrf

def home(request):
    context = {}
    context.update(csrf(request))
    return render(request, 'Home.html', context)
