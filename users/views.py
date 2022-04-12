from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
# Create your views here.
from django.contrib.auth import authenticate, login


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "User Created")
            return redirect("login")
    else:
        form = UserCreationForm()
    return render(request, 'users/register.html', {'form': form})


# def login(request):
#     username = request.POST['username']
#     password = request.POST['password']
#     user = authenticate(request, username, password)
#     if user is not None:
#         login(request, user)
#         return redirect('store-home')

#     return None


def logout(request):
    pass
