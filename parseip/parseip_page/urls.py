from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.parseip_page, name='parseip_page'),
    url(r'^ajax/parse/$', views.parse, name='parse'),
]
