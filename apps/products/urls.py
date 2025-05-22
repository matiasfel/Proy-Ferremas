from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ProductoViewSet, products_view

router = DefaultRouter()
router.register(r'productos', ProductoViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
    path('', products_view, name='products'),
]