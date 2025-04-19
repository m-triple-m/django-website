
from django.contrib import admin
from django.urls import path
from django.views.generic import TemplateView
from .views import browse, productDetails

urlpatterns = [
    path("browse/", browse, name="browse"),
    path("view-details/<int:product_id>", productDetails, name="productDetails")
]