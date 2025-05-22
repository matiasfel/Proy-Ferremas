from django.shortcuts import render
from .serializers import ProductoSerializer
from rest_framework import viewsets
from .models import Producto

# Create your views here.

def products_view(request):
    productos = Producto.objects.all()
    return render(request, 'products/products.html', {'productos': productos})


class ProductoViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer