# -*- coding: utf-8 -*-

from django.conf.urls import include, url
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('test', views.app, name='app'),
    path('past/', views.past, name='past'),
    path('present/', views.present, name='present'),
    path('future/', views.future, name='future'),
    url(r'^submit/', views.submit),
]