from django.conf.urls import patterns, include, url

urlpatterns = patterns('core.api.views',
    url(r'^hola_mundo_rest/$','hola_mundo')
)
