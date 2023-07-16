from django.shortcuts import render
from .models import *
from django.contrib import messages
from django.db import IntegrityError
from django.shortcuts import get_object_or_404,redirect

# Create your views here.
def home(request):
    return render(request, "proveedores/home.html")

def lista_proveedores(request):
    proveedores = Proveedor.objects.all()
    context = {
        "proveedores": proveedores
    }
    return render(request, "proveedores/lista_proveedores.html", context)

def nuevo_proveedor(request):

    if request.method == "POST":        
        try:
            Proveedor.objects.create(
            nombre = request.POST["nombre"],
            direccion = request.POST["direccion"],
            telefono = request.POST["telefono"],
            email = request.POST["email"],
            cuil = request.POST["cuil"],
            responsable = request.POST["responsable"],
            facturaT = request.POST["facturaT"],
            rubro = request.POST["rubro"],
            );
            messages.add_message(request,messages.SUCCESS,f"""Se registró {request.POST['nombre']} 
                                 {request.POST['cuil']} con numero de legajo {request.POST['rubro']} correctamente""")
        except IntegrityError:

            messages.add_message(request,messages.ERROR,f"El numero de legajo {request.POST['cuil']} ya se encuentra registrado")
            
    return render(request,'proveedores/nuevo_proveedor.html')
    
def desactivar_proveedor(request,id_proveedor):

    proveedor = get_object_or_404(Proveedor,id=id_proveedor)
    if proveedor.estado:
       proveedor.estado=False
       proveedor.save()

    return redirect('lista_proveedores')

def activar_proveedor(request,id_proveedor):

    proveedor = get_object_or_404(Proveedor,id=id_proveedor)
    if not proveedor.estado:
       proveedor.estado=True
       proveedor.save()

    return redirect('lista_proveedores')

def editar_proveedor(request,id_proveedor):

    proveedor = get_object_or_404(Proveedor, id=id_proveedor);
    if request.method == "POST":
        proveedor.nombre = request.POST["nombre"]
        proveedor.direccion = request.POST["direccion"]
        proveedor.telefono = request.POST["telefono"]
        proveedor.email = request.POST["email"]
        proveedor.cuil = request.POST["cuil"]
        proveedor.responsable = request.POST["responsable"]
        proveedor.facturaT = request.POST["facturaT"]
        proveedor.rubro = request.POST["rubro"]
        proveedor.save();
    
    return render(request,'proveedores/editar_proveedor.html',{"proveedor": proveedor})

def resumen(request, id_proveedor):
    compras = Compra.objects.filter(proveedor = id_proveedor)
    
    context = {
        "compras": compras
    }
 
    return render(request, 'proveedores/resumen.html', context)

def lista_compras(request):
    compras = Compra.objects.all()
    context = {
        "compras": compras
    }
    return render(request, "proveedores/lista_compras.html", context)

def desactivar_compra(request,id_compra):

    compra = get_object_or_404(Compra,id=id_compra)
    if compra.estado:
       compra.estado=False
       compra.save()

    return redirect('lista_compras')

def activar_compra(request,id_compra):

    compra = get_object_or_404(Compra,id=id_compra)
    if not compra.estado:
       compra.estado=True
       compra.save()

    return redirect('lista_compras')
