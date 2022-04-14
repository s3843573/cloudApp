from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='store-home'),
    path('about/', views.about, name='store-about'),
    path('cart', views.cart, name="store-cart"),
    path('products/<int:id>/', views.productInfo, name="product-info")
]
