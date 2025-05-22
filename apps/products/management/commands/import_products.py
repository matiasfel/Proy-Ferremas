import json
from django.core.management.base import BaseCommand
from products.models import Producto, Marca, Precio
from django.utils.dateparse import parse_datetime

class Command(BaseCommand):
    help = 'Importa productos desde un archivo JSON'

    def handle(self, *args, **kwargs):
        with open('data/productos.json', encoding='utf-8') as f:
            data = json.load(f)
            for item in data:
                marca_obj, _ = Marca.objects.get_or_create(nombre=item['marca'])
                producto = Producto.objects.create(
                    codigo=item['codigo'],
                    codigo_marca=item['codigo_marca'],
                    nombre=item['nombre'],
                    marca=marca_obj,
                    stock=item['stock']
                )
                for precio in item['precios']:
                    Precio.objects.create(
                        producto=producto,
                        fecha=parse_datetime(precio['fecha']),
                        valor=precio['valor']
                    )
            self.stdout.write(self.style.SUCCESS('Productos importados con éxito'))