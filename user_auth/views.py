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
    form = UserCreationForm()
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username = username, password = password)
            login(request, user)
            return redirect('home')
    context = {
        'form': form
    }
    return render(request, 'registration/register.html', context)