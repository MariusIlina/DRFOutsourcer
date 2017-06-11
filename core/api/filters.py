import django_filters
from core.models import Project


class ProjectFilter(django_filters.rest_framework.FilterSet):
    min_amount = django_filters.NumberFilter(name="payment_amount", lookup_expr='gte')
    max_amount = django_filters.NumberFilter(name="payment_amount", lookup_expr='lte')

    class Meta:
        model = Project
        fields = ['category', 'by_company', 'currency', 'payment_type', 'min_amount', 'max_amount']
