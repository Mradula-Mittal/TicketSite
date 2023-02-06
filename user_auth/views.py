from django.shortcuts import render, redirect , reverse
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required

#Views
@login_required
#home view - renders a success page
def home(request):
    context = {}
    return render(request, 'registration/success.html', context)

#register view initiates a user creation form for registration (sign up)
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()

