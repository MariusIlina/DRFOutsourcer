from rest_framework import viewsets, filters
from serializers import PaymentTypesSerializer, CurrencySerializer
from serializers import TimeUnitSerializer, CountrySerializer
from serializers import CompanySerializer, ProjectSerializer
from serializers import BidSerializer, RecommendationSerializer
from serializers import CategorySerializer, CommentSerializer
from serializers import UserSerializer
from permissions import IsCompanyOwner, IsEntityOwner, EditorIsStaff
from core.models import Company, Country, PaymentTypes, Currency, TimeUnit
from core.models import Project, Bid, Recommendation, Category, Comment
from filters import ProjectFilter
from drf_cached_instances.mixins import CachedViewMixin
from caches import ProjectCache
from rest_framework.generics import CreateAPIView
from django.contrib.auth import get_user_model
from rest_framework.permissions import AllowAny


# Create your views here.

class PaymentTypesViewSet(viewsets.ModelViewSet):
    serializer_class = PaymentTypesSerializer
    permission_classes = (EditorIsStaff,)
    queryset = PaymentTypes.objects.all()


class CurrencyViewSet(viewsets.ModelViewSet):
    serializer_class = CurrencySerializer
    permission_classes = (EditorIsStaff,)
    queryset = Currency.objects.all()


class TimeUnitViewSet(viewsets.ModelViewSet):
    serializer_class = TimeUnitSerializer
    permission_classes = (EditorIsStaff,)
    queryset = TimeUnit.objects.all()


class CountryViewSet(viewsets.ModelViewSet):
    serializer_class = CountrySerializer
    permission_classes = (EditorIsStaff,)
    queryset = Country.objects.all()


class CompanyViewSet(viewsets.ModelViewSet):
    serializer_class = CompanySerializer
    permission_classes = (IsCompanyOwner,)
    queryset = Company.objects.all()

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class ProjectViewSet(CachedViewMixin, viewsets.ModelViewSet):
    serializer_class = ProjectSerializer
    permission_classes = (IsEntityOwner,)
    queryset = Project.objects.all()
    filter_backends = (filters.DjangoFilterBackend,)
    filter_class = ProjectFilter
    cache_class = ProjectCache


class BidViewSet(viewsets.ModelViewSet):
    serializer_class = BidSerializer
    permission_classes = (IsEntityOwner,)
    queryset = Bid.objects.all()


class CommentViewSet(viewsets.ModelViewSet):
    serializer_class = CommentSerializer
    permission_classes = (IsEntityOwner,)
    queryset = Comment.objects.all()


class RecommendationViewSet(viewsets.ModelViewSet):
    serializer_class = RecommendationSerializer
    permission_classes = (IsEntityOwner,)
    queryset = Recommendation.objects.all()


class CategoryViewSet(viewsets.ModelViewSet):
    serializer_class = CategorySerializer
    permission_classes = (EditorIsStaff,)
    queryset = Category.objects.all()


class CreateUserView(CreateAPIView):
    model = get_user_model()
    permission_classes = (AllowAny,)
    serializer_class = UserSerializer
