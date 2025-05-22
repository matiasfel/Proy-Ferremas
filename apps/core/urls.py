from django.urls import path
from django.shortcuts import redirect
from . import views

urlpatterns = [
    path('', lambda request: redirect('base'), name='home'),
    path('home/', views.base_view, name='base'),
]
