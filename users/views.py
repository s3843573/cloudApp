from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from .forms import RegistrationForm
from django.contrib.auth.decorators import login_required


def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "User Created")
            return redirect("login")
    else:
        form = RegistrationForm()
    return render(request, 'users/register.html', {'form': form})


def loginUser(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('store-home')
        else:
            messages.success(request, "Users Does not Exists")
            return redirect('login')

    return render(request, 'users/login.html')


def logoutUser(request):
    logout(request)
    messages.success(request, "You have Logged Out")
    return redirect('store-home')
