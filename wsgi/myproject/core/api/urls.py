from django.conf.urls import patterns, include, url
from rest_framework.routers import DefaultRouter
from core.api.views import CompanyViewSet, CountryViewSet #SizeViewSet, ItemViewSet

router = DefaultRouter()
router.register(r'companies', CompanyViewSet)
router.register(r'countries', CountryViewSet)

urlpatterns = patterns('core.api.views',
    url(r'^', include(router.urls)),
)
