# Importacion de los modelos de la capa de ingreso a la aplicacion: Empresa, Usuarios; capa de facturacion: Conversion_UndVenta_UndCompra; capa de inventarios: Bodegas 
# Fecha creado: 26/08/2014
# Fecha actualizado: 27/08/2014
# Cambio realizado: Inclusion de los modulos Productos, Compra de Materiales, Detalle de compra de materiales correspondiente a la capa de inventarios, Ln 9
from django.contrib import admin

from web.models import Empresa, Usuario
from web.models import Conversion_UndVenta_UndCompra 
from web.models import Bodega, Producto, Compra_Material, Detalle_Compra_Material
from web.models import TipoDocumento, FormaPago, Empleado, Cliente, Proveedor, Venta, DetalleVenta

# Adicion del administrador Empresa
# Fecha creado: 26/08/2014
# Fecha actualizado: 05/09/2014
# Cambio realizado: Incluir filtro de busqueda actualizado, para el listado de empresas, Ln 19
class EmpresaAdmin(admin.ModelAdmin):
    list_display = ('Empresa', 'Nit', 'Direccion')
    list_filter = ['Nit']
    search_fields = ['Empresa', 'Nit', 'Direccion']
#fields = ['Empresa', 'Nit', 'Direccion']

# Adicion del administrador Usuario
# Fecha creado: 26/08/2014
# Cambio realizado: Cambio nombre UsuarioAdmin => UsuariosAdmin, Ln 18
# Fecha actualizado: 05/09/2014
# Cambio realizado: Incluir filtro de busqueda, para el listado de usuarios, Ln 27-29
class UsuariosAdmin(admin.ModelAdmin):
    list_display = ('Nombres', 'Apellidos', 'Email')
	# Definicion de filtros
    list_filter = ['Nombres', 'Apellidos']
    search_fields = ['Nombres', 'Apellidos', 'Email']
# Adicion del administrador Bodegas
# Fecha creado: 26/08/2014
# Fecha actualizado: 05/09/2014
# Cambio realizado: Incluir filtro de busqueda, para el listado de bodegas, Ln 32-34
class BodegasAdmin(admin.ModelAdmin):
	list_display = ('Bodega','Estante','Observaciones')
	# Definicion de filtros
	list_filter = ['Bodega']
	search_fields = ['Bodega','Estante','Observaciones']
# Adicion del administrador de Conversiones entre Unidad de compra y Unidad de Venta.
# Filtro por Unidades de venta
# Fecha creado: 26/08/2014	
# Fecha actualizado: 05/09/2014
# Cambio realizado: Actualizacion de filtros, para todos los campos de la grilla, Ln 40
class ConversionesAdmin(admin.ModelAdmin):
	list_display = ('Unidad_Venta', 'Unidad_Compra', 'Equivalencia')
	# Definicion de filtros
	list_filter = ['Unidad_Venta']
	search_fields = ['Unidad_Venta', 'Unidad_Compra', 'Equivalencia']

# Adicion del administrador de productos
# Fecha creado: 26/08/2014
# Fecha actualizado: 05/09/2014
# Cambio realizado: Actualizacion de filtros, para todos los campos de la grilla, Ln 48
class ProductosAdmin(admin.ModelAdmin):
	list_display = ('Nombre_producto', 'Linea', 'Observaciones')
	# Definicion de filtros
	list_filter = ['Nombre_producto']
	search_fields = ['Nombre_producto', 'Linea', 'Observaciones']
# Adicion del administrador Compra de Materiales
# Fecha creado: 27/08/2014
# Fecha actualizado: 05/09/2014
# Cambio realizado: Actualizacion de filtros, para todos los campos de la grilla, Ln 55
class Compra_MaterialesAdmin(admin.ModelAdmin):
	list_display = ('No_compra', 'Fecha', 'Observaciones')
	# Definicion de filtros
	list_filter = ['No_compra']
	search_fields = ['No_compra', 'Observaciones', 'Fecha']
# Adicion del Administrador para procesar el detalle en la compra de materiales
# Fecha creado: 27/08/2014
# Fecha actualizado: 05/09/2014
# Cambio realizado: Colocar el campo nombre producto, Ln 60-63. Especificar la busqueda por Observacion o por Producto, Ln 67 (FUENTE: https://groups.google.com/forum/#!msg/django-users/JKhf05HOezg/klz7A-vs_U0J)
# Fecha actualizado: 05/09/2014
# Cambio realizado: Colocar el numero de compra relacionado, Ln 62, 67-70, 73
class Detalle_Compra_MaterialesAdmin(admin.ModelAdmin):
	#list_display = ('Cantidad', 'Ref_Producto' ,'Talla', 'Color', 'Observacion')
	list_display = ('Cantidad', 'get_producto' ,'Talla', 'Color', 'Observacion', 'get_ncompra')
	def get_producto(self, obj):
		return obj.Ref_Producto.Nombre_producto
	get_producto.short_description = 'Producto'	
	get_producto.admin_order_field = 'Nombre_producto'
	def get_ncompra(self, obj):
		return obj.No_compra
	get_ncompra.short_description = 'Numero_de_compra'
	get_ncompra.admin_order_field = 'No_compra'
	# Definicion de filtros
	list_filter = ['Observacion',]	
	search_fields = ['Observacion', 'Ref_Producto__Nombre_producto', 'Talla', 'Color', 'No_compra__No_compra']
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

