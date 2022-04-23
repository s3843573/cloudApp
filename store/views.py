from django.shortcuts import render
from django.http import HttpResponse
from .models import *
import requests
from django.forms.models import model_to_dict

API_URL = "https://73pj96x27h.execute-api.us-east-1.amazonaws.com/dev"
S3_BUCKET_URL = "https://cc-a1.s3.amazonaws.com/"


def home(request):
    productsInfo = Product.objects.all()

    url = API_URL + "/products"
    res = requests.get(url)
    products = res.json()['products']

    for i in range(len(products)):
        products[i]['image'] = productsInfo[i].image.url
    return render(request, 'store/home.html', {'products': products})


def productInfo(request, id):
    productInfo = Product.objects.get(id=id)

    url = API_URL + F"/products/id?id={id}"
    res = requests.get(url)
    product = res.json()['product']
    product['image'] = productInfo.image.url
    return render(request, 'store/product.html', {'product': product})


def about(request):
    return render(request, 'store/about.html')
