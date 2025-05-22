from django.db import models

class Marca(models.Model):
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre

class Producto(models.Model):
    codigo = models.CharField(max_length=20, unique=True)  # FER-12345
    codigo_marca = models.CharField(max_length=20)         # BOS-67890
    marca = models.ForeignKey(Marca, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=255)
    stock = models.PositiveIntegerField()

    def __str__(self):
        return self.nombre

class Precio(models.Model):
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE, related_name="precios")
    fecha = models.DateTimeField()
    valor = models.DecimalField(max_digits=10, decimal_places=2)
