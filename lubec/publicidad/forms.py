from django.forms import ModelForm
from .models import Clientes,Transacciones, Vendedores, Productos, Tiendas, Detalle

class Clientesform(ModelForm):
    class Meta:
        model= Clientes
        fields= '__all__'

class Transaccionesform(ModelForm):
    class Meta:
        model= Transacciones
        fields= ['cliente','tienda','descripcion','fechaInicio','fechaFinal','vendedor']

class Vendedoresform(ModelForm):
    class Meta:
        model= Vendedores
        fields= '__all__'

class Productosform(ModelForm):
    class Meta:
        model= Productos
        fields='__all__'

class Tiendasform(ModelForm):
    class Meta:
        model= Tiendas
        fields=['cliente','nombre','descripcion','estado','ciudad']

class Detalleform(ModelForm):
    class Meta:
        model= Detalle
        fields=['producto','cantidad','precioCotizado','precioFacturacion','cantidadReservada','cantidadDisponible']

