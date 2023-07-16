from django.db import models

class Proveedor(models.Model):
    nombre = models.CharField(verbose_name="Nombre",max_length=50)
    direccion = models.CharField(verbose_name="Direccion",max_length=500)
    telefono = models.IntegerField(verbose_name="Telefono")
    email = models.EmailField(verbose_name="Email", null= False)
    cuil = models.IntegerField(verbose_name="CUIL",unique=True)
    responsable = models.CharField(verbose_name="responsable", null= False,max_length=50)
    facturaT = models.CharField(verbose_name="Tipo Factura", max_length = 5, null= False)
    rubro = models.CharField(verbose_name="Rubro", null=False,max_length=50)    
    estado = models.BooleanField(verbose_name="Estado",default=True)
    
    def __str__(self):
        return f"{self.nombre} - {self.cuil} - {self.responsable} - {self.facturaT}"
    
class Compra(models.Model):
    dia = models.IntegerField(verbose_name="DD")
    mes = models.IntegerField(verbose_name="MM")
    anio = models.IntegerField(verbose_name="AAAA")
    proveedor = models.ForeignKey(Proveedor,verbose_name="Proveedor",on_delete=models.CASCADE,related_name="proveedor")
    facturaT = models.ForeignKey(Proveedor,verbose_name="Tipo Factura",on_delete=models.CASCADE,related_name="facturat")
    facturaN = models.IntegerField(verbose_name="N° Factura", null=False)
    producto = models.CharField(verbose_name="Producto", null=False,max_length=50)
    cantidad = models.IntegerField(verbose_name="Cantidad", null=False)
    precio_unitario = models.FloatField(verbose_name="Precio Unitario", default = 0)
    estado = models.BooleanField(verbose_name="Estado", default=False)
    
    def __str__(self):
        return f"{self.producto} - {self.cantidad}"
    
class Usuario(models.Model):
    nombre = models.CharField(verbose_name="Nombre", max_length=50, null=False)
    apellido = models.CharField(verbose_name="Apellido", max_length=50, null=False)
    user_name = models.CharField(verbose_name="Nombre de Ususario", max_length=20, null=False, unique=True)
    password = models.CharField(verbose_name="Contraseña", max_length=20, null=False)
    email = models.EmailField(verbose_name="Email", null=False)
    tipo = models.CharField(verbose_name="Tipo", default="proveedor", max_length=20)
    estado = models.BooleanField(verbose_name="Estado", default=True)
    
    def __str__(self) -> str:
        return f"{self.user_name} - {self.estado}"