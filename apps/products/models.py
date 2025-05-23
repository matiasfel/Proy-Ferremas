from django.db import models
from django.contrib.auth.models import User

class Marca(models.Model):
    nombre = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.nombre

class Producto(models.Model):
    CATEGORIAS = [
        ('Basicos', 'Básicos'),
        ('Fijacion', 'Fijación'),
        ('Manuales', 'Herramientas Manuales'),
        ('Seguridad', 'Equipos de Seguridad'),
    ]

    codigo = models.CharField(max_length=20, unique=True)  # Código único del producto
    codigo_marca = models.CharField(max_length=20)
    marca = models.ForeignKey(Marca, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=255)
    stock = models.PositiveIntegerField()
    categoria = models.CharField(max_length=20, choices=CATEGORIAS, default='Basicos')

    def __str__(self):
        return f"{self.nombre} ({self.categoria})"

class Precio(models.Model):
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE, related_name="precios")
    fecha = models.DateField()  # Cambiado a DateField porque el JSON solo tiene fecha
    valor = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        unique_together = ('producto', 'fecha')
        ordering = ['-fecha']

    def __str__(self):
        return f"${self.valor} - {self.fecha.strftime('%Y-%m-%d')}"