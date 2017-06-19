import django_filters
from core.models import Project, Bid, Recommendation, Company, Comment


class ProjectFilter(django_filters.rest_framework.FilterSet):
    min_amount = django_filters.NumberFilter(name="payment_amount", lookup_expr='gte')
    max_amount = django_filters.NumberFilter(name="payment_amount", lookup_expr='lte')

    class Meta:
        model = Project
        fields = ['category', 'by_company', 'currency', 'payment_type', 'min_amount', 'max_amount']


class BidFilter(django_filters.rest_framework.FilterSet):
    min_amount = django_filters.NumberFilter(name="payment_amount", lookup_expr='gte')
    max_amount = django_filters.NumberFilter(name="payment_amount", lookup_expr='lte')

    class Meta:
        model = Bid
        fields = ['payment_type', 'currency', 'by_company', 'project', 'min_amount', 'max_amount']


class RecommendationFilter(django_filters.rest_framework.FilterSet):

    class Meta:
        model = Recommendation
        fields = ['by_company', 'for_company']


class CompanyFilter(django_filters.rest_framework.FilterSet):

    class Meta:
        model = Company
        fields = ['county', 'country', 'city', 'employees_no']


class CommentFilter(django_filters.rest_framework.FilterSet):

    class Meta:
        model = Comment
        fields = ['by_company', 'on_project']
