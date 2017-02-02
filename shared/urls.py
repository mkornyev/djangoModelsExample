from django.conf.urls import include, url
from shared import views

urlpatterns = [
    url(r'^$', views.home),
    url(r'^add-item$', views.add_item),
    # Parses number from URL and uses it as the item_id argument to the action
    url(r'^delete-item/(?P<item_id>\d+)$', views.delete_item),
]
