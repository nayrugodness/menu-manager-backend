from django.contrib import admin
from .models import CategoriaPlatillo, Platillo

@admin.register(CategoriaPlatillo)
class CategoriaPlatilloAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre')

@admin.register(Platillo)
class PlatilloAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'precio', 'categoria')
    list_filter = ('categoria',)  # Add filter by category
    search_fields = ('nombre', 'descripcion')  # Add search by name and description
