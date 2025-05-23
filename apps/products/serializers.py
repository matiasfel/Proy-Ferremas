from rest_framework import serializers
from .models import Producto, Marca, Precio

class PrecioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Precio
        fields = ['fecha', 'valor']

class MarcaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Marca
        fields = ['nombre']

class ProductoSerializer(serializers.ModelSerializer):
    precios = PrecioSerializer(many=True)
    marca = serializers.CharField(source='marca.nombre')

    class Meta:
        model = Producto
        fields = ['codigo', 'codigo_marca', 'nombre', 'stock', 'marca', 'precios']
