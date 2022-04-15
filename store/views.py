from django.shortcuts import render
from django.http import HttpResponse
from .models import *
# Create your views here.


def home(request):
    products = Product.objects.all
    return render(request, 'store/home.html', {'products': products})


def productInfo(request, id):
    product = Product.objects.get(id=id)
    return render(request, 'store/product.html', {'product': product})


def about(request):
    return render(request, 'store/about.html')


def cart(request):
    return render(request, 'store/cart.html')
