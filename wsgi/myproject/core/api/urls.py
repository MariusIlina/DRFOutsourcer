from django.conf.urls import patterns, include, url
from rest_framework.routers import DefaultRouter
from core.api.views import PaymentTypesViewSet, CurrencyViewSet
from core.api.views import TimeUnitViewSet, CountryViewSet
from core.api.views import CompanyViewSet, ProjectViewSet
from core.api.views import BidViewSet, RecommendationViewSet

router = DefaultRouter()
router.register(r'payment-types', PaymentTypesViewSet)
router.register(r'currencies', CurrencyViewSet)
router.register(r'time-units', TimeUnitViewSet)
router.register(r'countries', CountryViewSet)
router.register(r'companies', CompanyViewSet)
router.register(r'projects', ProjectViewSet)
router.register(r'bids', BidViewSet)
router.register(r'recommendations', RecommendationViewSet)

urlpatterns = patterns('core.api.views',
    url(r'^', include(router.urls)),
)
