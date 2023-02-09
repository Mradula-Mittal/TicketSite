from django.shortcuts import render, redirect
from .models import Ticket, Site
from django.http import HttpResponse
from django.template import loader
# Create your views here.

def Landing(request):
    context = { }
    return render(request, 'main.html', context)