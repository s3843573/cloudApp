from distutils.command.upload import upload
from pickle import TRUE
from pyexpat import model
from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Product(models.Model):
    name = models.CharField(max_length=100, null=True)
    price = models.FloatField(null=False)
    category = models.CharField(max_length=100, null=True)
    image = models.ImageField(null=True, blank=True,
                              upload_to="productImages/")
    description = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.name


# class Order(models.Model):
#     user = models.ForeignKey(
#         User, on_delete=models.SET_NULL, blank=TRUE, null=True)

#     def __str__(self):
#         return str(self.id)


# class OrderItem(models.Model):
#     product = models.ForeignKey(
#         Product, on_delete=models.SET_NULL, blank=TRUE, null=True)
#     order = models.ForeignKey(
#         Order, on_delete=models.SET_NULL, blank=TRUE, null=True)

#     quantity = models.IntegerField(default=0, null=True, blank=True)
