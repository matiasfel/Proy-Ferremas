from django.shortcuts import render

# Create your views here.

def login_view(request):
    return render(request, 'core/login.html')

def dashboard_view(request):
    return render(request, 'core/dashboard.html')