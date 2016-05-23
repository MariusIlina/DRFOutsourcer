import django_filters
from rest_framework import filters
from core.models import Project


class ProjectFilter(filters.FilterSet):
    min_amount = django_filters.NumberFilter(name="payment_amount", lookup_type='gte')
    max_amount = django_filters.NumberFilter(name="payment_amount", lookup_type='lte')

    class Meta:
        model = Project
        fields = ['category', 'by_company', 'currency', 'payment_type', 'min_amount', 'max_amount']
