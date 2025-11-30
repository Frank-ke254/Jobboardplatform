from django_filters import rest_framework as filters
from .models import Job

class JobFilter(filters.FilterSet):
    category = filters.CharFilter(field_name='category', lookup_expr='icontains')
    location = filters.CharFilter(field_name='location', lookup_expr='icontains')

    class Meta:
        model = Job
        fields = ['category', 'location']
