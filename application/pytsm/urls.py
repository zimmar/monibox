from django.contrib import admin
from django.urls import path, include

from application.pytsm import views

from base.admin import pytsm_admin_site

urlpatterns = [
    path('', views.index, name='index'),
    path('overview_table/<mainname>/<subname>', views.overview, name='overview_table'),
]