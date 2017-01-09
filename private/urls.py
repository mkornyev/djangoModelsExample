from django.conf.urls import patterns, include, url
from django.contrib.auth import views as auth_views
from private import views as private_views

urlpatterns = [
    url(r'^$', private_views.home),
    url(r'^add-item$', private_views.add_item),
    url(r'^delete-item/(?P<id>\d+)$', private_views.delete_item),
    # Route for built-in authentication with our own custom login page
    url(r'^login$', auth_views.login, {'template_name':'private/login.html'}),
    # Route to logout a user and send them back to the login page
    url(r'^logout$', auth_views.logout_then_login),
    url(r'^register$', private_views.register),
]

