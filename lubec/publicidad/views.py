from django.shortcuts import render,redirect,reverse
from django.contrib.auth.decorators import login_required
from .forms import Clientesform, Transaccionesform, Vendedoresform, Productosform, Tiendasform, Detalleform
from .models import Clientes, TipoClientes, Vendedores, Productos, Tiendas, Detalle, Transacciones, Status, Documentos 
from django.contrib import messages
from django.http import HttpResponse
import random
from datetime import datetime
# Create your views here.
@login_required
def clientes(request):
    datos=Clientes.objects.all().select_related('tipoCliente')
    form=Clientesform()
    return render(request,'clientes.html',{"datos":datos,"form":form})

@login_required
def cadenas(request):
    return render(request,'cadenas.html')


#Aquí tenemos las vistas correspondientes con los documentos

@login_required
def sA(request,id):#Sin Autorizar
    cliente=Clientes.objects.get(id=id)
    datos=Transacciones.objects.filter(cliente=cliente).filter(documento=1)
    return render(request,'sinAutorizar.html',{"dato":cliente,"datos":datos,'documento':"Ordenes"})

@login_required
def contratos(request,id):
    cliente=Clientes.objects.get(id=id)
    datos=Transacciones.objects.filter(cliente=cliente).filter(documento=2)
    return render(request,'contratos.html',{"dato":cliente,"datos":datos,'documento':"Contratos"})


@login_required
def campa(request,id):
    cliente=Clientes.objects.get(id=id)
    datos=Transacciones.objects.filter(cliente=cliente).filter(documento=3)
    return render(request,'campa.html',{"dato":cliente,"datos":datos,'documento':"Campañas"})


@login_required
def ordenesG(request):
    documentos=Transacciones.objects.filter(documento=1)
    return render(request,'ordenes.html',{"datos":documentos,'documento':"Ordenes"})

@login_required
def contratosG(request):
    documentos=Transacciones.objects.filter(documento=2)
    return render(request,'ordenes.html',{"datos":documentos,'documento':'Contratos'})

@login_required
def campaG(request):
    documentos=Transacciones.objects.filter(documento=3)
    return render(request,'ordenes.html',{"datos":documentos,'documento':'Campañas'})



@login_required
def aprobarContrato(request,id):
    documento=Transacciones.objects.get(id=id)
    doc=Documentos.objects.get(id=1)
    if(documento.documento==doc):
        
        doc=Documentos.objects.get(id=2)
        documento.documento=doc
        documento.contrato=generador()
        status=Status.objects.get(id=3)
        documento.status=status
        documento.save()
        return redirect(reverse('publicidad:contratosG'))
    else :
        doc=Documentos.objects.get(id=3)
        documento.documento=doc
        documento.contrato=generador()
        status=Status.objects.get(id=4)
        documento.status=status
        documento.save()
        return redirect(reverse('publicidad:campaG'))














@login_required
def reportes(request):
    return render(request,'reportes.html')



@login_required
def gastos(request):
    return render(request,'gastos.html')
@login_required
def factura(request):
    return render(request,'factura.html')
@login_required
def tiendas(request):
    return render(request,'tiendas.html')

@login_required
def detalleOrden(request,id):
    trans=Transacciones.objects.get(id=id)
    detalles=Detalle.objects.filter(transaccion=trans)
    return render(request,'detalle_orden.html',{"trans":trans,'detalles':detalles})

@login_required
def formOrden(request):
    return render(request,'formOrden.html')

@login_required
def formCliente(request):
    form=Clientesform()
    if request.method=='POST':
        form=Clientesform(data=request.POST)
        if form.is_valid():
            user=form.save()
            messages.add_message(request,messages.SUCCESS,"Cliente creado")
            return redirect(reverse('publicidad:clientes'))
    
    return render(request,'formCliente.html',{"form":form})

@login_required
def editCliente(request,id):
    cliente=Clientes.objects.get(id=id)
    if request.method=='GET':
        form=Clientesform(instance=cliente)
    else:
        form=Clientesform(data=request.POST,instance=cliente)
        if form.is_valid():
            form.save()
            messages.add_message(request,messages.INFO,"Cliente actualizado")
            return redirect(reverse('publicidad:clientes'))

    return render(request,'formCliente.html',{"form":form})

@login_required
def deleteCliente(request,id):
    cliente=Clientes.objects.get(id=id)
    cliente.delete()
    messages.add_message(request,messages.WARNING,"Cliente eliminado")
    return redirect(reverse('publicidad:clientes'))

def generador():
    clave=''
    for i in range(5):
        clave=clave+str(random.randrange(1,9,1))
    return clave

@login_required
def transaccionesForm(request):
    form=Transaccionesform()
    form2=Detalleform()
    if request.method=='POST':
        print(request.POST)
        print("El dato es:")
        resultado=dict(request.POST)
        trans=Transacciones()
        trans.cliente=Clientes.objects.get(id=int(resultado['cliente'][0]))
        trans.tienda=Tiendas.objects.get(id=int(resultado['tienda'][0]))
        trans.descripcion=resultado['descripcion'][0]
        trans.fechaInicio=datetime.strptime(resultado['fechaInicio'][0],'%d/%m/%Y')
        trans.fechaFinal=datetime.strptime(resultado['fechaFinal'][0],'%d/%m/%Y')
        trans.vendedor=Vendedores.objects.get(id=int(resultado['vendedor'][0]))
        trans.orden=generador()
        trans.is_activo=False
        trans.documento=Documentos.objects.get(id=1)
        trans.status=Status.objects.get(id=2)
        trans.save()
        for i in range(len(resultado['producto'])):
            detalles=Detalle()
            detalles.producto=Productos.objects.get(id=int(resultado['producto'][i]))
            detalles.cantidad=resultado['cantidad'][i]
            detalles.precioCotizado=resultado['precioCotizado'][i]
            detalles.precioFacturacion=resultado['precioFacturacion'][i]
            detalles.cantidadReservada=resultado['cantidadReservada'][i]
            detalles.cantidadDisponible=resultado['cantidadDisponible'][i]
            detalles.transaccion=Transacciones.objects.last()
            detalles.save()
        return redirect(reverse('publicidad:ordenesG'))
        

    return render(request,'ordenf.html',{"form":form,"titulo":"Nueva orden",'detalle':form2})

@login_required
def vendedoresForm(request):
    form=Vendedoresform()
    if request.method=='POST':
        form=Vendedoresform(data=request.POST)
        if form.is_valid():
            user=form.save()
            messages.add_message(request,messages.SUCCESS,"Vendedor guardado")
            return redirect(reverse('publicidad:vendedores'))
    return render(request,'formCliente.html',{"form":form,"titulo":"Nuevo empleado"})
    
#CRUD vendedores
@login_required
def vendedores(request):
    datos=Vendedores.objects.all()
    return render(request,'vendedores.html',{"datos":datos})


@login_required
def editVendedor(request,id):
    vendedor=Vendedores.objects.get(id=id)
    if request.method=='GET':
        form=Vendedoresform(instance=vendedor)
    else:
        form=Vendedoresform(data=request.POST)
        if form.is_valid():
            user=form.save()
            messages.add_message(request,messages.INFO,"Vendedor actualizado")
            return redirect(reverse('publicidad:vendedores'))

    return render(request,'formCliente.html',{"form":form})
    
    
@login_required
def deleteVendedor(request,id):
    cliente=Vendedores.objects.get(id=id)
    cliente.delete()
    messages.add_message(request,messages.WARNING,"Vendedor eliminado")
    return redirect(reverse('publicidad:vendedores'))




@login_required
def vendedoresForm(request):
    form=Vendedoresform()
    if request.method=='POST':
        form=Vendedoresform(data=request.POST)
        if form.is_valid():
            user=form.save()
            messages.add_message(request,messages.SUCCESS,"Vendedor guardado")
            return redirect(reverse('publicidad:vendedores'))
    return render(request,'formCliente.html',{"form":form,"titulo":"Nuevo empleado"})
    
#path('productos/',views.productos,name='productos')
@login_required
def productos(request):
   datos=Productos.objects.all()
   return render(request,'productos.html',{"datos":datos})


#path('editProducto/<int:id>',views.editProducto,name='editProducto')
@login_required
def editProducto(request,id):
    producto=Productos.objects.get(id=id)
    if request.method=='GET':
        form=Productosform(instance=producto)
    else:
        form=Productosform(data=request.POST)
        if form.is_valid():
            form.save()
            messages.add_message(request,messages.INFO,"Producto actualizado")
            return redirect(reverse('publicidad:productos'))

    return render(request,'formCliente.html',{"form":form})
    
# path('productoForm/',views.productosForm,name='productosForm')
@login_required
def productoForm(request):
    form=Productosform()
    if request.method=='POST':
        form=Productosform(data=request.POST)
        if form.is_valid():
            form.save()
            messages.add_message(request,messages.SUCCESS,"Producto guardado")
            return redirect(reverse('publicidad:productos'))
    return render(request,'formCliente.html',{"form":form,"titulo":"Nuevo producto"})
    
#path('deleteProducto/<int:id>',views.deleteProductos,name='deleteProducto')
@login_required
def deleteProducto(request,id):
    print("Hola soy un rpoducto")
    producto=Productos.objects.get(id=id)
    producto.delete()
    messages.add_message(request,messages.WARNING,"Producto eliminado")
    return redirect(reverse('publicidad:productos'))

#path('tiendas/',views.tiendas,name='tiendas'),
#path('tiendasForm/',views.tiendasForm,name='tiendasForm'),
#path('ediTienda/<int:id>',views.editProducto,name='editienda'),
#path('deleteTienda/<int:id>',views.deleteProducto,name='deleteTienda')

#path('productos/',views.productos,name='productos')
@login_required
def tiendas(request):
   datos=Tiendas.objects.all()
   return render(request,'tiendas.html',{"datos":datos})


#path('editProducto/<int:id>',views.editProducto,name='editProducto')
@login_required
def editTienda(request,id):
    tienda=Tiendas.objects.get(id=id)
    if request.method=='GET':
        form=Tiendasform(instance=tienda)
    else:
        form=Tiendasform(data=request.POST,instance=tienda)
        if form.is_valid():
            form.save()
            messages.add_message(request,messages.INFO,"Tienda actualizada")
            return redirect(reverse('publicidad:tiendas'))
    return render(request,'formCliente.html',{"form":form})
    
# path('productoForm/',views.productosForm,name='productosForm')
@login_required
def tiendasForm(request):
    form=Tiendasform()
    if request.method=='POST':
        form=Tiendasform(data=request.POST)
        if form.is_valid():
            form.save()
            messages.add_message(request,messages.SUCCESS,"Tienda guardada")
            return redirect(reverse('publicidad:tiendas'))
    return render(request,'formCliente.html',{"form":form,"titulo":"Nueva Tienda"})
    
#path('deleteProducto/<int:id>',views.deleteProductos,name='deleteProducto')
@login_required
def deleteTienda(request,id):
    print("Estoy dentro")
    tienda=Tiendas.objects.get(id=id)
    tienda.delete()
    messages.add_message(request,messages.WARNING,"Tienda Eliminada")
    return redirect(reverse('publicidad:tiendas'))

@login_required
def cliente(request,id):
    cliente=Clientes.objects.get(id=id)
    return render(request,'cliente.html',{"dato":cliente,"id":id})
    


#Detalle CRUD

@login_required
def formDetalle(request,id):
    form=Detalleform()
    if request.method=='POST':
        form=Detalleform(data=request.POST)
        if form.is_valid():
            form.save()
            tienda=Tiendas.objects.get(id=id)
            detalle=Detalle.objects.last()
            tienda.detalle=detalle
            tienda.save()
            
            messages.add_message(request,messages.SUCCESS,"Articulo creado")
            return redirect(reverse('publicidad:tiendas'))
    
    return render(request,'formCliente.html',{"form":form})

@login_required
def editDetalle(request,id):
    cliente=Detalleform.objects.get(id=id)
    if request.method=='GET':
        form=Detalleform(instance=cliente)
    else:
        form=Detalleform(data=request.POST)
        if form.is_valid():
            form.save()
            messages.add_message(request,messages.INFO,"Articulo actualizado")
            return redirect(reverse('publicidad:tiendas'))

    return render(request,'formCliente.html',{"form":form})

@login_required
def deleteDetalle(request,id):
    cliente=Clientes.objects.get(id=id)
    cliente.delete()
    messages.add_message(request,messages.WARNING,"Cliente eliminado")
    return redirect(reverse('publicidad:clientes'))

@login_required
def detalle(request,id):
    tienda=Tiendas.objects.get(id=id)
    return render(request,'detalle.html',{"tienda":tienda})

@login_required
def editOrden(request,id):
    dato=Transacciones.objects.get(id=id)
    detalles=dato.detalle_set.all()
    forms=[]
    if request.method=='GET':
        for i in detalles:
            forms.append(Detalleform(instance=i))
        form=Transaccionesform(instance=dato)
        return render(request,'formCliente.html',{"form":form,'detalles':forms,"titulo":"Orden"})
    if request.method=='POST':
        print(request.POST)
        print("El dato es:")
        resultado=dict(request.POST)
        trans=Transacciones.objects.get(id=id)
        trans.cliente=Clientes.objects.get(id=int(resultado['cliente'][0]))
        trans.tienda=Tiendas.objects.get(id=int(resultado['tienda'][0]))
        trans.descripcion=resultado['descripcion'][0]
        trans.fechaInicio=datetime.strptime(resultado['fechaInicio'][0],'%d/%m/%Y')
        trans.fechaFinal=datetime.strptime(resultado['fechaFinal'][0],'%d/%m/%Y')
        trans.vendedor=Vendedores.objects.get(id=int(resultado['vendedor'][0]))
        
        detalles=list(trans.detalle_set.all())
        print(detalles)
        for i in range(len(detalles)):
            detalles[i].producto=Productos.objects.get(id=int(resultado['producto'][i]))
            detalles[i].cantidad=resultado['cantidad'][i]
            detalles[i].precioCotizado=resultado['precioCotizado'][i]
            detalles[i].precioFacturacion=resultado['precioFacturacion'][i]
            detalles[i].cantidadReservada=resultado['cantidadReservada'][i]
            detalles[i].cantidadDisponible=resultado['cantidadDisponible'][i]
            detalles[i].transaccion=trans
            detalles[i].save()
        trans.save()
        return redirect(reverse('publicidad:ordenesG'))
    
    """
    else:
        form=Transaccionesform(data=request.POST)
        if form.is_valid():
            form.save()
            messages.add_message(request,messages.INFO,"Orden actualizada")
            return redirect(reverse('publicidad:ordenes'))
    """

    #return render(request,'formCliente.html',{"form":form,'detalles':form2,"Titulo":"Cliente"})

@login_required
def deleteOrden(request,id):
    orden=Transacciones.objects.get(id=id)
    orden.delete()
    messages.add_message(request,messages.WARNING,"Orden eliminada")
    return redirect(reverse('publicidad:ordenes'))



@login_required
def formDetalleO(request,id):
    form=Detalleform()
    if request.method=='POST':
        form=Detalleform(data=request.POST)
        if form.is_valid():
            form.save()
            
            trans=Transacciones.objects.get(id=id)
            detalle=Detalle.objects.all()
            for i in detalle:
                d=i
            d.transaccion=trans
            d.save()
            
            messages.add_message(request,messages.SUCCESS,"Articulo creado")
            return redirect(reverse('publicidad:clientes'))
    
    return render(request,'formCliente.html',{"form":form})


@login_required
def verOrden(request,id):
    tran=Transacciones.objects.get(id=id)
    detalles=tran.detalle_set.all()
    return render(request,'verOrden.html',{"tran":tran,"detalles":detalles,"titulo":"Orden"})