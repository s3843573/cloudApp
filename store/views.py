from django.shortcuts import render
from django.http import HttpResponse
from .models import *
import urllib.request
import json
from django.forms.models import model_to_dict

API_URL = "https://73pj96x27h.execute-api.us-east-1.amazonaws.com/dev"
S3_BUCKET_URL = "https://cc-a1.s3.amazonaws.com/"


def home(request):
    productsInfo = Product.objects.all()

    url = API_URL + "/products"
    contents = urllib.request.urlopen(url)
    products = json.load(contents)['products']

    for i in range(len(products)):
        products[i]['image'] = productsInfo[i].image.url
    return render(request, 'store/home.html', {'products': products})


def productInfo(request, id):
    productInfo = Product.objects.get(id=id)

    url = API_URL + F"/products/id?id={id}"
    contents = urllib.request.urlopen(url)
    product = json.load(contents)['products']
    product['image'] = productInfo.image.url
    return render(request, 'store/product.html', {'product': product})


def about(request):
    return render(request, 'store/about.html')
