from django.shortcuts import render, redirect, get_object_or_404
from .serializers import ProductoSerializer
from rest_framework import viewsets, serializers
from .models import Producto
from django.views.decorators.http import require_POST

# Create your views here.

def products_view(request):
    productos = Producto.objects.select_related('marca').prefetch_related('precios')

    q = request.GET.get('q', '')
    categoria = request.GET.get('categoria', '')

    if q:
        productos = productos.filter(
            nombre__icontains=q
        ) | productos.filter(
            marca__nombre__icontains=q
        )

    if categoria:
        productos = productos.filter(categoria=categoria)

    context = {
        'productos': productos,
        'categorias': Producto.CATEGORIAS,
    }
    return render(request, 'products/products.html', context)

class ProductoViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer


def add_to_cart(request, producto_id):
    carrito = request.session.get('carrito', {})

    if str(producto_id) in carrito:
        carrito[str(producto_id)]['cantidad'] += 1
    else:
        producto = get_object_or_404(Producto, id=producto_id)
        precio_actual = producto.precios.order_by('-fecha').first().valor
        carrito[str(producto_id)] = {
            'nombre': producto.nombre,
            'precio': float(precio_actual),
            'cantidad': 1
        }

    request.session['carrito'] = carrito
    return redirect(request.META.get('HTTP_REFERER', 'products'))  # Redirige a la misma vista o a 'products' si no hay referencia

def ver_carrito(request):
    carrito = request.session.get('carrito', {})
    total = sum(item['precio'] * item['cantidad'] for item in carrito.values())
    return render(request, 'products/ver_carrito.html', {'carrito': carrito, 'total': total})

def actualizar_carrito(request, producto_id):
    carrito = request.session.get('carrito', {})

    nueva_cantidad = int(request.POST.get('cantidad', 1))

    if str(producto_id) in carrito:
        if nueva_cantidad > 0:
            carrito[str(producto_id)]['cantidad'] = nueva_cantidad
        else:
            # Si cantidad es 0 o menor, elimina el producto
            carrito.pop(str(producto_id))

    request.session['carrito'] = carrito
    return redirect('ver_carrito')

def eliminar_del_carrito(request, producto_id):
    carrito = request.session.get('carrito', {})

    if str(producto_id) in carrito:
        del carrito[str(producto_id)]
        request.session['carrito'] = carrito

    return redirect('ver_carrito')