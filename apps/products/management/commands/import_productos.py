from django.core.management.base import BaseCommand
from products.models import Producto, Marca, Precio
from django.utils.dateparse import parse_datetime
import json, os

class Command(BaseCommand):
    help = 'Importa productos desde un archivo JSON y les asigna una categoría'

    def add_arguments(self, parser):
        parser.add_argument('ruta_json', type=str, help='Ruta al archivo JSON de productos')

    def handle(self, *args, **options):
        path = options['ruta_json']
        categoria = os.path.splitext(os.path.basename(path))[0].capitalize()

        with open(path, encoding='utf-8') as f:
            data = json.load(f)
            for item in data:
                marca_obj, _ = Marca.objects.get_or_create(nombre=item['marca'])

                producto = Producto.objects.create(
                    codigo=item['codigo'],
                    codigo_marca=item['codigo_marca'],
                    nombre=item['nombre'],
                    marca=marca_obj,
                    stock=item['stock'],
                    categoria=categoria
                )

                for precio in item['precios']:
                    Precio.objects.create(
                        producto=producto,
                        fecha=parse_datetime(precio['fecha']),
                        valor=precio['valor']
                    )

        self.stdout.write(self.style.SUCCESS(f'Productos de "{categoria}" importados con éxito'))