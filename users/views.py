from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from .forms import RegistrationForm
from django.contrib.auth.models import User
import requests
import json


API_URL = "https://73pj96x27h.execute-api.us-east-1.amazonaws.com/dev"


def postRequest(url, username, password):
    userData = {
        "username": username,
        "password": password
    }
    res = requests.post(url, json.dumps(userData))
    return res.json()


def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            # save user to db
            url = API_URL + "/register"
            username = form['username'].value()
            password = form['password1'].value()
            res = postRequest(url, username, password)
            res = res['message']
            messages.success(request, res)
            return redirect("login")
        else:
            messages.success(request, "Invalid Fields")
            return redirect("register")
    else:
        form = RegistrationForm()
    return render(request, 'users/register.html', {'form': form})


def loginUser(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        # verify user credentials with aws lambda
        url = API_URL + "/login"
        res = postRequest(url, username, password)
        validUser = res['validUser']
        message = res['message']
        if validUser:
            user = User.objects.get(username=username)
            user.is_active = True
            user.save()

            # log user in the website
            login(request, user, backend='django.contrib.auth.backends.ModelBackend')
            messages.success(request, message)
            return redirect('store-home')
        else:
            messages.success(request, "Users Does not Exists")
            return redirect('login')

    return render(request, 'users/login.html')


def logoutUser(request):
    logout(request)
    messages.success(request, "You have Logged Out")
    return redirect('store-home')
