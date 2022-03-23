from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils import timezone
from .managers import UserManager
from . import choices as user_constants


class User(AbstractUser):
    username = None  # remove username field, we will use email as unique identifier
    email = models.EmailField(unique=True, null=True, db_index=True)
    is_active = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    date_joined = models.DateTimeField(default=timezone.now)
    user_type = models.PositiveSmallIntegerField(
        choices=user_constants.USER_TYPE_CHOICES
    )
    phone = models.CharField(max_length=11, blank=True)
    REQUIRED_FIELDS = []
    USERNAME_FIELD = "email"

    objects = UserManager()


class Shop(models.Model):
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=512)
    category = models.CharField(max_length=255)
    address = models.JSONField()
    contact = models.JSONField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)


class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=512)
    price = models.FloatField()
    image = models.URLField()
    shop = models.ForeignKey(Shop, on_delete=models.CASCADE)
    category = models.CharField(max_length=255)


class Subscription(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    shop = models.ForeignKey(Shop, on_delete=models.CASCADE)
    price = models.FloatField()
    time_period = models.JSONField()
    quantity_list = models.JSONField()


class Order(models.Model):
    timestamp = models.DateTimeField(auto_now=True)
    address = models.JSONField()
    products = models.ManyToManyRel(to=Product, field=Product)
    user = models.ForeignKey(to=User, on_delete=models.CASCADE)
    subscription = models.ForeignKey(to=Subscription, on_delete=models.CASCADE)
    shop = models.ForeignKey(to=Shop, on_delete=models.CASCADE)
