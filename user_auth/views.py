from django.shortcuts import render, redirect , reverse
from django.http import HttpResponse
from django.contrib.auth import login, authenticate
from django.forms import inlineformset_factory
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.decorators import login_required

#importing from same directory
from . import models
from .forms import Register

#Views
@login_required
#home view - renders a success page
def home(request):
    context = {}
    return render(request, 'registration/success.html', context)

#register view initiates a user creation form for registration (sign up)
def register(request):
    form = Register()
    if request.method == 'POST':
        form = Register(request.POST)
        if form.is_valid():
            user = form.save()
            #username = form.cleaned_data.get('username')
            #password = form.cleaned_data.get('password')
            #user = authenticate(username = username, password = password)
            login(request, user)
            return redirect('home')
    context = {
        'form': form
    }
    return render(request, 'registration/registration.html', context)

#To access the registered user
def login(request, user):
    if request.method == 'POST':
        form = AuthenticationForm(request, data= request.POST)
        if form.is_valid():
            #log the user in
            #login(request, user)  
            #username = request.POST['username']
            #password = request.POST['password']
            #user = authenticate(request, username=username, password=password)  
            return redirect('home')
        else:
            form = AuthenticationForm()
    context = {
        'form': form
    }
    return render(request, 'registration/login.html', context)