from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ProductoViewSet, products_view
from . import views

router = DefaultRouter()
router.register(r'json', ProductoViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
    path('', products_view, name='products'),
    path('carrito/', views.ver_carrito, name='ver_carrito'),
    path('carrito/agregar/<int:producto_id>/', views.add_to_cart, name='agregar_al_carrito'),
    path('carrito/actualizar/<int:producto_id>/', views.actualizar_carrito, name='actualizar_carrito'),
    path('carrito/eliminar/<int:producto_id>/', views.eliminar_del_carrito, name='eliminar_del_carrito'),
]