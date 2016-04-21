from django.shortcuts import render, get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView
from django.contrib.auth.models import User
from django.http import Http404
from rest_framework import status
from rest_framework import viewsets
from core.api.serializers import PaymentTypesSerializer, CurrencySerializer
from core.api.serializers import TimeUnitSerializer, CountrySerializer
from core.api.serializers import CompanySerializer, ProjectSerializer
from core.api.serializers import BidSerializer, RecommendationSerializer
from core.api.serializers import CategorySerializer, CommentSerializer
from core.api.permissions import IsCompanyOwner, IsEntityOwner, EditorIsStaff
from core.models import Company, Country, PaymentTypes, Currency, TimeUnit
from core.models import Project, Bid, Recommendation, Category, Comment


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


class ProjectViewSet(viewsets.ModelViewSet):
    serializer_class = ProjectSerializer
    permission_classes = (IsEntityOwner,)
    queryset = Project.objects.all()


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
