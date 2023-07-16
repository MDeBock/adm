from django.contrib import admin
from proveedores.models import *

class UsuarioAdmin(admin.ModelAdmin):
    model = Usuario
    list_display = ("id", "nombre", "apellido", "user_name", "email", "tipo", "estado")
    search_fields = ("nombre", "apellido")
    list_filter = ("estado",)
    
class ProveedorAdmin(admin.ModelAdmin):
    model = Proveedor
    list_display = ("id", "nombre", "estado")
    search_fields = ("nombre",)
    list_filter = ("estado",)
    
class CompraAdmin(admin.ModelAdmin):
    model = Compra
    list_display = ("id", "proveedor", "facturaN", "producto")
    search_fields = ("proveedor",)
    list_filter = ("estado",)

admin.site.register(Usuario, UsuarioAdmin)
admin.site.register(Proveedor, ProveedorAdmin)
admin.site.register(Compra, CompraAdmin)
