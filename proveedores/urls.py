from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name= "home"),
    path('lista/', views.lista_proveedores, name="lista_proveedores"),
    path('activar/<int:id_proveedor>',views.activar_proveedor,name="activar_proveedor"),
    path('desactivar/<int:id_proveedor>',views.desactivar_proveedor,name="desactivar_proveedor"),
    path('nuevo/',views.nuevo_proveedor,name="nuevo_proveedor"),
    path('editar/<int:id_proveedor>', views.editar_proveedor,name="editar_proveedor"),
    path('resumen/<int:id_proveedor>', views.resumen,name="resumen"),
    path('lista_compras/', views.lista_compras, name="lista_compras"),
    path('activar_compra/<int:id_compra>',views.activar_compra,name="activar_compra"),
    path('desactivar_compra/<int:id_compra>',views.desactivar_compra,name="desactivar_compra"),
]