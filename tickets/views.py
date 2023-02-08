from django.shortcuts import render
from . import models
# Create your views here.

def Landing(request):
    context = { }
    return render(request, 'main.html', context)