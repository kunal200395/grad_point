from django.contrib import admin
from django.urls import path
from django.conf.urls import include, url
from . import home

urlpatterns = [
    url('', home.index),
    path('admin/', admin.site.urls),
]
