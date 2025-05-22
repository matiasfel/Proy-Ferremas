from rest_framework import serializers
from .models import Producto, Precio

class PrecioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Precio
        fields = ['fecha', 'valor']

class ProductoSerializer(serializers.ModelSerializer):
    marca = serializers.StringRelatedField()
    precios = PrecioSerializer(many=True)

    class Meta:
        model = Producto
        fields = ['codigo', 'marca', 'codigo_marca', 'nombre', 'precios']