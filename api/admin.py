from django.contrib import admin
from .models import *
from django.contrib.auth.admin import UserAdmin
# Register your models here.
class ShopAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "description", "category", "contact", "location")
class OrderAdmin(admin.ModelAdmin):
    list_display = ("id", "timestamp", "address", "user")

class SubscriptionAdmin(admin.ModelAdmin):
    list_display = ("id", "product", "shop", "user","price","time_period","quantity","number_of_weeks","has_ordered")

class ProductAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "description", "price","shop","category")

class CartAdmin(admin.ModelAdmin):
    list_display = ("id", "user")


admin.site.register(Shop,ShopAdmin)
admin.site.register(Order,OrderAdmin)
admin.site.register(Subscription,SubscriptionAdmin)
admin.site.register(Product,ProductAdmin)
admin.site.register(User,UserAdmin)
admin.site.register(Cart,CartAdmin)
