from dataclasses import field
from .models import Shop
import django_filters

class ShopFilter(django_filters.FilterSet):
    class Meta:
        model=Shop
        fields=["category","name","location"]
