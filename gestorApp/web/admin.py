# Importacion de los modelos de la capa de ingreso a la aplicacion: Empresa, Usuarios; capa de facturacion: Conversion_UndVenta_UndCompra; capa de inventarios: Bodegas 
# Fecha creado: 26/08/2014
# Fecha actualizado: 27/08/2014
# Cambio realizado: Inclusion de los modulos Productos (Falta habilitar el control de cargue de imagen), Compra de Materiales, Detalle de compra de materiales correspondiente a la capa de inventarios, Ln 9
from django.contrib import admin

from web.models import Empresa, Usuario
from web.models import Conversion_UndVenta_UndCompra 
from web.models import Bodega, Producto, Compra_Material, Detalle_Compra_Material
from web.models import TipoDocumento, FormaPago, Empleado, Cliente, Proveedor, Venta, DetalleVenta

# Adicion del administrador Empresa
# Fecha creado: 26/08/2014
class EmpresaAdmin(admin.ModelAdmin):
    list_display = ('Empresa', 'Nit', 'Direccion')
    list_filter = ['Nit']
    search_fields = ['Empresa', 'Nit']
#fields = ['Empresa', 'Nit', 'Direccion']

# Adicion del administrador Usuario
# Fecha creado: 26/08/2014
# Cambio realizado: Cambio nombre UsuarioAdmin => UsuariosAdmin, Ln 18
class UsuariosAdmin(admin.ModelAdmin):
    list_display = ('Nombres', 'Apellidos', 'Email')

# Adicion del administrador Bodegas
# Fecha creado: 26/08/2014
class BodegasAdmin(admin.ModelAdmin):
	list_display = ('Bodega','Estante','Observaciones')

# Adicion del administrador de Conversiones entre Unidad de compra y Unidad de Venta.
# Filtro por Unidades de venta
# Fecha creado: 26/08/2014	
class ConversionesAdmin(admin.ModelAdmin):
	list_display = ('Unidad_Venta', 'Unidad_Compra', 'Equivalencia')
	# Definicion de filtros
	list_filter = ['Unidad_Venta']
	search_fields = ['Unidad_Venta']

# Adicion del administrador de productos
# Fecha creado: 26/08/2014
class ProductosAdmin(admin.ModelAdmin):
	list_display = ('Nombre_producto', 'Linea', 'Observaciones')
	# Definicion de filtros
	list_filter = ['Nombre_producto']
	search_fields = ['Nombre_producto']
# Adicion del administrador Compra de Materiales
# Fecha creado: 27/08/2014
class Compra_MaterialesAdmin(admin.ModelAdmin):
	list_display = ('No_compra', 'Fecha', 'Observaciones')
	# Definicion de filtros
	list_filter = ['No_compra']
	search_fields = ['No_compra', 'Observaciones']
# Adicion del Administrador para procesar el detalle en la compra de materiales
# Fecha creado: 27/08/2014
class Detalle_Compra_MaterialesAdmin(admin.ModelAdmin):
	list_display = ('Cantidad', 'Talla', 'Color', 'Observacion')
	# Definicion de filtros
	list_filter = ['Observacion']
	search_fields = ['Observacion']
# Register your models here.
# Registro de los modulos Empresa, Usuarios, Bodegas, Conversiones, Productos
# Fecha creado: 26/08/2014.
# Cambio realizado: Cambio nombre UsuarioAdmin => UsuariosAdmin, Ln 31
# Fecha actualizado: 27/08/2014.
# Cambio realizado: Registro del modulo Compra de materiales en el sitio, Ln 71
# Fecha actualizado: 27/08/2014.
# Cambio realizado: Registro del modulo Detalle de compra de materiales en el sitio, Ln 74
admin.site.register(Empresa, EmpresaAdmin)
admin.site.register(Usuario, UsuariosAdmin)
admin.site.register(Bodega, BodegasAdmin)
admin.site.register(Conversion_UndVenta_UndCompra, ConversionesAdmin)
admin.site.register(Producto, ProductosAdmin)
admin.site.register(Compra_Material, Compra_MaterialesAdmin)
admin.site.register(Detalle_Compra_Material, Detalle_Compra_MaterialesAdmin)

admin.site.register(TipoDocumento)
admin.site.register(FormaPago)
admin.site.register(Empleado)
admin.site.register(Cliente)
admin.site.register(Proveedor)
admin.site.register(Venta)
admin.site.register(DetalleVenta)

