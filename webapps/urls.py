from django.conf.urls import patterns, include, url

urlpatterns = [
    url(r'^private/', include('private.urls')),
    url(r'^shared/',  include('shared.urls')),
]
