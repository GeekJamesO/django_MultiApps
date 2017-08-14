from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^register$', views.register),
    url(r'^login$', views.login),
    url(r'^new$', views.newUser),
    url(r'^$', views.users),
]
