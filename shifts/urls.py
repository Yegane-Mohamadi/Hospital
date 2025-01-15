# urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('add_employee/', views.add_employee, name='add_employee'),
    path('add_shift/', views.add_shift, name='add_shift'),
]
