from django_filters import rest_framework as filters

from .models import Hotel


class HotelFilter(filters.FilterSet):
    name = filters.CharFilter(field_name='name', lookup_expr='icontains')
    price_from = filters.NumberFilter(field_name='price', lookup_expr='gte')
    price_to = filters.NumberFilter(field_name='price', lookup_expr='lte')
    description = filters.CharFilter(field_name='description', lookup_expr='icontains')
    image = filters.CharFilter(field_name='image', lookup_expr='icontains')

    class Meta:
        model = Hotel
        fields = ['category']