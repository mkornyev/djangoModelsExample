from django.conf.urls import include, url
from django.contrib.auth import views as auth_views
from welcome import views as welcome_views


urlpatterns = [
    url(r'^$', welcome_views.home, name='welcome'),
    url(r'^register$', welcome_views.register, name='register'),
    # Route for built-in authentication with our own custom login page
    url(r'^login$', auth_views.login, {'template_name':'welcome/login.html'}, name='login'),
    # Route to logout a user and send them back to the login page
    url(r'^logout$', auth_views.logout_then_login, name='logout'),
]

