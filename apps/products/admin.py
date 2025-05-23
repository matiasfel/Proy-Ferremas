from django.contrib import admin
from .models import Marca, Producto, Precio

class PrecioInline(admin.TabularInline):  # También puedes usar StackedInline si prefieres
    model = Precio
    extra = 0  # No mostrar filas vacías por defecto
    readonly_fields = ('valor', 'fecha')  # Opcional: evita que se editen

@admin.register(Marca)
class MarcaAdmin(admin.ModelAdmin):
    list_display = ('nombre',)

@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    list_display = ('codigo', 'nombre', 'marca', 'stock', 'categoria')
    list_filter = ('categoria', 'marca')
    search_fields = ('nombre', 'codigo', 'marca__nombre')

@admin.register(Precio)
class PrecioAdmin(admin.ModelAdmin):
    list_display = ('producto', 'fecha', 'valor')
    list_filter = ('fecha',)
