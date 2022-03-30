from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils import timezone
from .managers import UserManager
from . import choices as user_constants


class User(AbstractUser):
    user_type = models.PositiveSmallIntegerField(
        choices=user_constants.USER_TYPE_CHOICES,null = True,blank = True
    )
    phone = models.CharField(max_length=15, blank=True)


class Shop(models.Model):
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=512,blank=True,null=True)
    category = models.CharField(max_length=255,blank=True,null=True)
    address = models.JSONField(blank=True,null=True)
    contact = models.JSONField(blank=True,null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.URLField(max_length=2084,null=True,blank=True)
    location = models.CharField(max_length=128,null=True,blank = True)


class Product(models.Model):
    name = models.CharField(max_length=255,blank=True,null=True)
    description = models.CharField(max_length=512,blank=True,null=True)
    price = models.FloatField(blank=True,null=True)
    image = models.URLField(max_length=2084,blank=True,null=True)
    shop = models.ForeignKey(Shop, on_delete=models.CASCADE)
    category = models.CharField(max_length=255,blank=True,null=True)


class Subscription(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    shop = models.ForeignKey(Shop, on_delete=models.CASCADE)
    price = models.FloatField(blank=True,null=True)
    time_period = models.JSONField(blank=True,null=True)
    quantity_list = models.JSONField(blank=True,null=True)
    quantity = models.IntegerField(blank=True,null=True)
    number_of_weeks = models.IntegerField(blank=True,null=True)


class Order(models.Model):
    timestamp = models.DateTimeField(auto_now=True)
    address = models.JSONField(blank=True,null=True)
    products = models.ManyToManyRel(to=Product, field=Product)
    user = models.ForeignKey(to=User, on_delete=models.CASCADE)
    subscription = models.ForeignKey(to=Subscription, on_delete=models.CASCADE)
    shop = models.ForeignKey(to=Shop, on_delete=models.CASCADE)
