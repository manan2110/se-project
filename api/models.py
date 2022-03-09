from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=11, blank=True)


class Shop(models.Model):
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=512)
    category = models.CharField(max_length=255)
    address = models.JSONField()
    contact = models.JSONField()
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)


class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=512)
    price = models.FloatField()
    image = models.URLField()
    shop = models.ForeignKey(Shop, on_delete=models.CASCADE)
    category = models.CharField(max_length=255)


class Subscription(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    shop = models.ForeignKey(Shop, on_delete=models.CASCADE)
    price = models.FloatField()
    time_period = models.JSONField()
    quantity_list = models.JSONField()


class Order(models.Model):
    timestamp = models.DateTimeField(auto_now=True)
    address = models.JSONField()
    products = models.ManyToManyRel(to=Product, field=Product)
    user = models.ForeignKey(to=UserProfile, on_delete=models.CASCADE)
    subscription = models.ForeignKey(to=Subscription, on_delete=models.CASCADE)
    shop = models.ForeignKey(to=Shop, on_delete=models.CASCADE)
