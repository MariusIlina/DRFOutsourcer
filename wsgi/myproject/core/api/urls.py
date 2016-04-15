from django.conf.urls import patterns, include, url

urlpatterns = patterns('core.api.views',
    # url(r'^hola_mundo_rest/(?P<nombre>\w+)$', 'hola_mundo'),
    url(r'^usuarios/$', 'usuarios'),
    url(r'^items/$', 'items'),
    url(r'^usuarios/(?P<id>\d+)$', 'usuarios', name='usuario'),
    url(r'^sizes/$', 'sizes_all'),
    url(r'^sizes/(?P<id>\d+)$', 'sizes_all', name='sizeintro'),
    # url(r'^todos/$', 'to_do'),
    # url(r'^valuta/$', 'valuta'),
)
