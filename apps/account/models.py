from django.contrib.auth.models import AbstractUser
from django.db import models
from django.conf import settings
from products.models import Producto

class CustomUser(AbstractUser):
    class TiposUsuario(models.TextChoices):
        CLIENTE = 'cliente', 'Cliente'
        ADMINISTRADOR = 'admin', 'Administrador'
        VENDEDOR = 'vendedor', 'Vendedor'
        BODEGUERO = 'bodeguero', 'Bodeguero'
        CONTADOR = 'contador', 'Contador'

    tipo = models.CharField(max_length=20, choices=TiposUsuario.choices, default=TiposUsuario.CLIENTE)