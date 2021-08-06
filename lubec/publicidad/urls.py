from django.urls import path
from . import views

app_name='publicidad'
urlpatterns = [
  

    path('cadenas/',views.cadenas,name='cadenas'),
    
    #Las rutas para las ordenes, contratos y campañas
    
    path('sA/<int:id>',views.sA,name='sA'),
    path('contratos/<int:id>',views.contratos,name='contratos'),
    path('campa/<int:id>',views.campa,name='campa'),


    path('clientes/',views.clientes,name='clientes'),
    path('gastos/',views.gastos,name='gastos'),
    path('factura/',views.factura,name='factura'),
    path('tiendas/',views.tiendas,name='tiendas'),
    path('reportes/',views.reportes,name='reportes'),
    
    
    #ordenes
    path('detalleOrden/<int:id>',views.detalleOrden,name='detalleOrden'),
    
    
    
    path('formOrden/',views.formOrden,name='formOrden'),
    

    #CRUD de cliente
    path('formCliente/',views.formCliente,name='formCliente'),
    path('editCliente/<int:id>',views.editCliente,name='editCliente'),
    path('deleteCliente/<int:id>',views.deleteCliente,name='deleteCliente'),
    path('transaccionesForm/', views.transaccionesForm,name='transaccionesForm'),
    
    #vendedores
    path('vendedores/',views.vendedores,name='vendedores'),
    path('vendedoresForm/',views.vendedoresForm,name="vendedoresForm"),
    path('editVendedor/<int:id>',views.editVendedor,name='editVendedor'),
    path('loginVendedor/<int:id>',views.deleteVendedor,name='deleteVendedor'),
    
    #Productos
    path('productos/',views.productos,name='productos'),
    path('productoForm/',views.productoForm,name='productoForm'),
    path('editProducto/<int:id>',views.editProducto,name='editProducto'),
    path('deleteProducto/<int:id>',views.deleteProducto,name='deleteProducto'),

    #Tiendas
    path('tiendas/',views.tiendas,name='tiendas'),
    path('tiendasForm/',views.tiendasForm,name='tiendasForm'),
    path('ediTienda/<int:id>',views.editTienda,name='ediTienda'),
    path('deleteTienda/<int:id>',views.deleteTienda,name='deleteTienda'),

    #Detalle
    #path('detalle/',views.tiendas,name='tiendas'),
    path('detalle/<int:id>',views.detalle,name='detalle'),
    path('formDetalle/<int:id>',views.formDetalle,name='formDetalle'),
    path('editDetalle/<int:id>',views.editDetalle,name='editDetalle'),
    path('deleteDetalle/<int:id>',views.deleteDetalle,name='deleteDetalle'),

    path('editOrden/<int:id>',views.editOrden,name='editOrden'),
    path('deleteOrden/<int:id>',views.deleteOrden,name='deleteOrden'),


    path('cliente/<int:id>',views.cliente,name='cliente'),

    path('ordenesG/',views.ordenesG,name='ordenesG'),
    path('verOrden/<int:id>',views.verOrden,name='verOrden'),
    path('contratosG/',views.contratosG,name='contratosG'),
    path('campaG/',views.campaG,name='campaG'),
    path('aprobarContrato/<int:id>',views.aprobarContrato,name="aprobarContrato"),
    path('formDetalleO/<int:id>',views.formDetalleO,name='formDetalleO'),
    

]