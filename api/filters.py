from .models import Shop
import django_filters

django_filters.ChoiceFilter


class ShopFilter(django_filters.FilterSet):
    class Meta:
        model = Shop
        fields = {
            "category": ["icontains"],
            "name": ["icontains"],
            "location": ["icontains"],
        }
