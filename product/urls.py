
from django.contrib import admin
from django.urls import path
from django.views.generic import TemplateView
from .views import browse

urlpatterns = [
    path("browse/", browse, name="browse")
]