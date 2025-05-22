from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('register/', views.register_view, name='register'),
    path('', views.account_view, name='account'),
    path('logout/', views.logout_view, name='logout'),
]