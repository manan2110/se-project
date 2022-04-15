from django.contrib import admin
from .models import *
from django.contrib.auth.admin import UserAdmin
# Register your models here.

class FilterProductAdmin(admin.ModelAdmin):
    def get_queryset(self, request):
        # For Django < 1.6, override queryset instead of get_queryset
        qs = super(FilterProductAdmin, self).get_queryset(request)
        user = request.user
        if not user.is_superuser:
            if Shop.objects.filter(user=user).exists():
                shop = Shop.objects.get(user=user)
                return qs.filter(shop=shop)
            return qs.filter(shop=None)
        return qs

class FilterSubscriptionAdmin(admin.ModelAdmin):
    def get_queryset(self, request):
        # For Django < 1.6, override queryset instead of get_queryset
        qs = super(FilterSubscriptionAdmin, self).get_queryset(request)
        user = request.user
        if not user.is_superuser:
            if Shop.objects.filter(user=user).exists():
                shop = Shop.objects.get(user=user)
                return qs.filter(shop=shop)
            return qs.filter(shop=None)
        return qs
class ShopAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "description", "category", "contact", "location","user")
class OrderAdmin(admin.ModelAdmin):
    list_display = ("id", "timestamp", "address", "user")

class SubscriptionAdmin(FilterSubscriptionAdmin):
    list_display = ("id", "product", "shop", "user","price","time_period","quantity","number_of_weeks","has_ordered")

class ProductAdmin(FilterProductAdmin):
    list_display = ("id", "name", "description", "price","shop","category")

class CartAdmin(admin.ModelAdmin):
    list_display = ("id", "user")


admin.site.register(Shop,ShopAdmin)
admin.site.register(Order,OrderAdmin)
admin.site.register(Subscription,SubscriptionAdmin)
admin.site.register(Product,ProductAdmin)
admin.site.register(User,UserAdmin)
admin.site.register(Cart,CartAdmin)
