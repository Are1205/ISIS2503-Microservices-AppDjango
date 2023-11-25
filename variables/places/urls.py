from django.urls import path
from django.conf.urls import url, include
from django.views.decorators.csrf import csrf_exempt

from . import views

urlpatterns = [
    url(r'^places/', views.placesList, name='placesList'),
    url(r'^placescreate/$', csrf_exempt(views.placesCreate), name='placesCreate'),
]