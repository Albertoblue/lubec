from django.db import models

# Create your models here.
class TipoClientes(models.Model):
    descripcion=models.CharField(max_length=30)
    def __str__(self):
        return self.descripcion

class Clientes(models.Model):
    nombreComercial=models.CharField(max_length=150)
    razonSocial=models.CharField(max_length=50)
    #tipoCliente=models.CharField(max_length=50)
    telefono=models.CharField(max_length=20)
    tipoCliente=models.ForeignKey(TipoClientes, on_delete=models.CASCADE)
    correo=models.CharField(max_length=70)
    def __str__(self):
        return self.nombreComercial

class Marcas(models.Model):
    cliente=models.ForeignKey(Clientes, on_delete=models.CASCADE)
    descripcion=models.TextField()

    


class Productos(models.Model):
    descripcion=models.TextField()
    espaciosDisponibles=models.IntegerField()
    def __str__(self):
        return self.descripcion


class Cadenas(models.Model):
    cliente=models.ForeignKey(Clientes, on_delete=models.CASCADE)
    descripcion=models.TextField()

class StatusDocumentos(models.Model):
    descripcion=models.TextField()
    def __str__(self):
        return self.descripcion
       
class Tiendas(models.Model):
    cliente=models.ForeignKey(Clientes,on_delete=models.CASCADE)
    nombre=models.CharField(max_length=50)
    descripcion=models.TextField()
    estado=models.CharField(max_length=50)
    ciudad=models.CharField(max_length=50)
    def __str__(self):
        return self.nombre

class Inventario(models.Model):
        producto=models.ForeignKey(Productos,on_delete=models.CASCADE)
        cantidad=models.IntegerField()
        precioCotizado=models.IntegerField()
        precioFacturacion=models.IntegerField()
        cantidadReservada=models.IntegerField()
        cantidadDisponible=models.IntegerField()
        tienda=models.ForeignKey(Tiendas, on_delete=models.CASCADE,null=True)

class Vendedores(models.Model):
    nombre=models.CharField(max_length=70)
    numeroEmpleado=models.CharField(max_length=30)
    email=models.CharField(max_length=50)
    telefono=models.CharField(max_length=15)
    def __str__(self):
        return self.nombre

class Status(models.Model):
    descripcion=models.CharField(max_length=30)
    def __str__(self):
        return self.descripcion

class Documentos(models.Model):
    descripcion=models.CharField(max_length=30)
    def __str__(self):
        return self.descripcion

    
class Transacciones(models.Model):
    cliente=models.ForeignKey(Clientes,on_delete=models.CASCADE)
    orden=models.CharField(max_length=30, null=True)
    contrato=models.CharField(max_length=30, null=True)
    campana=models.CharField(max_length=30, null=True)
    tienda=models.ForeignKey(Tiendas,on_delete=models.CASCADE)
    #marca=models.ForeignKey(Marcas,on_delete=models.CASCADE)
    descripcion=models.TextField()
    fecha=models.DateField(auto_now_add=True)
    fechaInicio=models.DateField()
    fechaFinal=models.DateField()
    status=models.ForeignKey(Status, on_delete=models.CASCADE,null=True)
    documento=models.ForeignKey(Documentos, on_delete=models.CASCADE,null=True)
    vendedor=models.ForeignKey(Vendedores,on_delete=models.CASCADE)
    is_activo=models.BooleanField(null=True)

class Detalle(models.Model):
        producto=models.ForeignKey(Productos,on_delete=models.CASCADE)
        cantidad=models.IntegerField()
        precioCotizado=models.IntegerField()
        precioFacturacion=models.IntegerField()
        cantidadReservada=models.IntegerField()
        cantidadDisponible=models.IntegerField()
        transaccion=models.ForeignKey(Transacciones, on_delete=models.CASCADE,null=True)




