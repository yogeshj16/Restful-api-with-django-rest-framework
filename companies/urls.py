from django.contrib import admin
from django.urls import path, include
from rest_framework.urlpatterns import format_suffix_patterns
from companies import views

urlpatterns = [
    path('Stocks/',views.StocksList.as_view()),
    path('Stocks/(?P<pk>[0-9]+)/$',views.StocksList.as_view())
]