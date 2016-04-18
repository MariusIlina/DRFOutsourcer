from django.conf.urls import patterns, include, url
from rest_framework.routers import DefaultRouter
from core.api.views import ItemViewSet, SizeViewSet

router = DefaultRouter()
router.register(r'items', ItemViewSet).register(r'sizes', SizeViewSet)

urlpatterns = patterns('core.api.views',
    # url(r'^hola_mundo_rest/(?P<nombre>\w+)$', 'hola_mundo'),
    url(r'^usuarios/$', 'usuarios'),
    #url(r'^items/$', 'items'),
    url(r'^', include(router.urls)),
    url(r'^usuarios/(?P<id>\d+)$', 'usuarios', name='usuario'),
    #url(r'^sizes/$', 'sizes_all'),
    #url(r'^sizes/(?P<id>\d+)$', 'sizes_all', name='sizeintro'),
    # url(r'^todos/$', 'to_do'),
    # url(r'^valuta/$', 'valuta'),
)
