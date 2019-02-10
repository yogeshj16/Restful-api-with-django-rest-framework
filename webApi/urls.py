from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from webApi import views

urlpatterns = [
    path('employees/', views.employeesList.as_view())
]


