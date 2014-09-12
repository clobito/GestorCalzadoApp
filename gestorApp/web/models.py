from django.db import models

# Create your models here.
# Entidades de la capa Ingreso a la aplicacion
# Fecha creado: 26/08/2014
# Objeto de la entidad web_empresa
# Fecha actualizado: 
# Cambio realizado: Cambio de control texto a Email, Ln 14
class TipoDocumento(models.Model):
    Nombre = models.CharField(max_length=50)
    Codigo = models.CharField(max_length=5, unique=True)
    def __unicode__(self):
        return self.Codigo

class FormaPago(models.Model):
    Nombre = models.CharField(max_length=50)
    def __unicode__(self):
        return self.Nombre

class Empresa(models.Model):
	# Atributos
    Nit = models.CharField(max_length=13, primary_key = True)
    Empresa = models.CharField(max_length=60)
    #Email = models.CharField(max_length=70, null = True)
    Email = models.EmailField(unique=True)
    Direccion = models.CharField(max_length=500)
	# Visualizacion en la grilla
    def __unicode__(self):
        return self.Empresa
# Objeto de la entidad web_usuarios
# Fecha creacion: 26/08/2014
# Fecha cambio: 26/08/2014. Cambio realizado: Cambio nombre clase Usuario => Usuarios. Ln 18
# Fecha cambio: 26/08/2014. Cambio realizado: Colocar campo validador para email, Ln 25
# Fecha actualizado: 05/09/2014
# Cambio realizado: Colocar campo Password con * (favor revisar porque no lo hace), Ln 40 (DESAC). Se instancio en el fuente forms.py la clase ClaveForm() y se redefinio la visualizacion del campo denominado Clave, pero no lo renderiza.

class Usuario(models.Model):
    TipoDocumento = models.ForeignKey(TipoDocumento)
    Documento = models.CharField(max_length=13, primary_key = True)
    Clave = models.CharField(max_length=100)        
    #Email = models.CharField(max_length=70, null=True)
    Email = models.EmailField(unique=True)
    Nombres = models.CharField(max_length=100)
    Apellidos = models.CharField(max_length=100)
	# Atributos FK
    #Empresa = models.ForeignKey(Empresa)
    empresa = models.ForeignKey('Empresa')
	# Visualizacion en la grilla
    def __unicode__(self):
        return self.Nombres + ' ' + self.Apellidos

# Objeto de la entidad Bodegas.
# Capa/Modulo asociado: Inventarios
# Fecha creado: 26/08/2014 
# Fecha actualizado: 27/08/2014
# Cambio realizado: Especificar observaciones como opcional (27/08/2014), Ln 47
class Bodega(models.Model):
	No_Posicion = models.CharField(max_length=15, primary_key = True)
	Estante =  models.IntegerField()
	Bodega = models.CharField(max_length=30)
	Observaciones = models.TextField(blank=True)
	# Visualizacion en la grilla
	def __unicode__(self):
		return self.Bodega
		
# Objeto de la entidad Conversion_UndVenta_UndCompra 
# Capa/Modulo asociado: Facturacion
# Fecha creado: 26/08/2014
class Conversion_UndVenta_UndCompra(models.Model):
	Unidad_Venta = models.CharField(max_length=50, primary_key = True)
	Unidad_Compra= models.CharField(max_length=50)
	Equivalencia= models.DecimalField(max_digits=10, decimal_places=3)
	# Visualizacion en la grilla
	def __unicode__(self):
		return self.Unidad_Compra + self.Unidad_Venta


# Objeto de la entidad Productos
# Capa/Modulo asociado: Inventarios
# Fecha creado: 26/08/2014
# Fecha actualizado: 27/08/2014
# Cambio realizado: Especificar observaciones como opcional (27/08/2014), Ln 82
class Producto(models.Model):
	# Definicion de Atributos
	Ref_Producto = models.CharField(max_length=20, primary_key = True)
	Nombre_producto=models.CharField(max_length=70)
	Linea=models.CharField(max_length=30)
	#Imagen=models.ImageField(upload_to='files')
	Imagen=models.ImageField(upload_to='static/files',null=True,blank=True)
	Observaciones=models.TextField(null = True, blank=True)
	Unidad_Venta=models.ForeignKey(Conversion_UndVenta_UndCompra)
	#Conversion_UndVenta_UndCompra=models.ForeignKey(Conversion_UndVenta_UndCompra)
	# Visualizacion en la grilla
	def __unicode__(self):
		return self.Nombre_producto + ' '+ self.Linea

# Objeto de la entidad Empleados
# Capa/Modulo asociado: Facturacion
class Empleado(models.Model):
    TipoDocumento = models.ForeignKey(TipoDocumento)
    Documento = models.CharField(max_length=13, primary_key = True)
    Nombres = models.CharField(max_length=100)
    Apellidos = models.CharField(max_length=100)
    Direccion = models.CharField(max_length=500)
    Email = models.EmailField(max_length=100, null=True)
    Cargo = models.CharField(max_length=50, null=True)
    Foto = models.ImageField(upload_to='static/files',null=True,blank=True)
    def __unicode__(self):
        return self.Nombres + ' ' + self.Apellidos

# Objeto de la entidad Clientes
# Capa/Modulo asociado: Facturacion
class Cliente(models.Model):
    TipoDocumento = models.ForeignKey(TipoDocumento)
    Nombre = models.CharField(max_length=200)
    Telefono_Fijo = models.CharField(max_length=20, null=True)
    Celular = models.CharField(max_length=20, null=True)
    Direccion = models.CharField(max_length=100, null=True)
    Email = models.EmailField(max_length=100, null=True)
    def __unicode__(self):
        return self.Nombre

# Objeto de la entidad Proveedor
# Capa/Modulo asociado: Facturacion
class Proveedor(models.Model):
    TipoDocumento = models.ForeignKey(TipoDocumento)
    Nombre = models.CharField(max_length=200)
    Telefono_Fijo = models.CharField(max_length=20, null=True)
    Celular = models.CharField(max_length=20, null=True)
    Direccion = models.CharField(max_length=100, null=True)
    Email = models.EmailField(max_length=100, null=True)
    Posicion = models.ForeignKey(Bodega)
    def __unicode__(self):
        return self.Nombre

# Objeto de la entidad Venta
# Capa/Modulo asociado: Facturacion
class Venta(models.Model):
    Numero_Factura_Venta = models.CharField(max_length=20, primary_key=True)
    Fecha = models.DateTimeField(auto_now=False, null=True)
    Valor_Total_Compra = models.DecimalField(max_digits=20,decimal_places=2)
    Forma_Pago = models.ForeignKey(FormaPago)
    Observaciones = models.TextField(null = True)
    Empleado = models.ForeignKey(Empleado)
    Cliente = models.ForeignKey(Cliente)
    def __unicode__(self):
        return self.Numero_Factura

# Objeto de la entidad Detalle_Venta
# Capa/Modulo asociado: Facturacion
class DetalleVenta(models.Model):
    id_DetalleVenta = models.AutoField(primary_key=True)
    Descuento = models.DecimalField(max_digits=5,decimal_places=2)
    Cantidad = models.IntegerField()
    Talla = models.CharField(max_length=10, null=True)
    Color = models.CharField(max_length=50, null=True)
    Observaciones = models.TextField(null=True)
    Producto = models.ForeignKey(Producto)
    Numero_Factura = models.ForeignKey(Venta)
    Posicion = models.ForeignKey(Bodega)
    def __unicode__(self):
        return self.id_DetalleVenta

# Objeto de la entidad Compra_Materiales
# Capa/Modulo asociado: Inventarios
# Fecha creado: 27/08/2014
# Fecha actualizado: 05/09/2014
# Cambio realizado: Correcion campo No_Compra por No_compra, Ln 179. Correcion valores de retorno con la funcion unicode(). FUENTE: http://stackoverflow.com/questions/16169035/coercing-to-unicode-need-string-or-buffer-nonetype-found-when-rendering-in-dja
class Compra_Material(models.Model):
	# Definicion de Atributos
    No_compra = models.CharField(max_length=15, primary_key = True)
    Fecha = models.DateField()
    Observaciones=models.TextField(null = True, blank=True)
    # Aparecen desactivados, ya que aun no se han implementado sus clases
	#Nit_proveedor=models.ForeignKey(Proveedor)
    #CC_empleado=models.ForeignKey(Empleados)
	# Visualizacion en la grilla
    def __unicode__(self):
	    #Desactivado, , ya que aun no se han implementado sus clases
		#return self.No_Compra + ' '+ self.Fecha + ' ' + self.Nit_proveedor + ' ' + self.Observaciones
		return unicode(self.No_compra) or u'' + ' ' + unicode(self.Fecha) or u'' + ' ' + unicode(self.Observaciones) or u''

# Objeto de la entidad Detalle_Compra_Materiales
# Capa/Modulo asociado: Inventarios
# Fecha creado: 27/08/2014
# Fecha actualizado: 05/09/2014
# Cambio realizado: Colocar objeto self en todos las variables para referenciar la informacion dentro de la grilla, Ln 199. 
# Fecha actualizado: 05/09/2014
# Cambio realizado: Especificar llaves foraneas complementarias en el proceso de compra, Ln 199,200.
# Fecha actualizado: 05/09/2014
# Cambio realizado: Colocar columna producto, Ln 205
class Detalle_Compra_Material(models.Model):
	# Definicion de Atributos
	id_Detalle = models.AutoField(primary_key=True)
	Cantidad = models.IntegerField()
	Precio_Und_Compra = models.DecimalField(max_digits=10, decimal_places=2)
	Talla = models.CharField(max_length=4)
	Color = models.CharField(max_length=30)
	# Campo opcional
	Observacion = models.TextField(null = True, blank=True)
	# Llaves Foraneas
	No_compra = models.ForeignKey(Compra_Material)
	No_Posicion = models.ForeignKey(Bodega)
	Ref_Producto = models.ForeignKey(Producto)
	# Visualizacion en la grilla
	def __unicode__(self):
		return unicode(self.Cantidad) + unicode(self.Ref_Producto) + ' ' + self.Talla + ' ' + self.Color + ' ' + self.Observacion
# Objeto de la entidad Gestion_Inventario
# Proposito: Generar el listado de inventario con todos los movimientos relacionados
# Fecha creado: 08/09/2014
# Fecha actualizado: 12/09/2014
# Cambio realizado: Actualizacion del modelo, para la llave primaria como autoincremental, Ln 215
class Inventario(models.Model):
	#id_Inventario = models.BigIntegerField(primary_key = True)	
	id_Inventario = models.AutoField(primary_key=True)
	Cantidad = models.IntegerField()
	Operacion = models.CharField(max_length=3)
	Fecha_Hora= models.DateTimeField()
	# Llaves Foraneas
	No_Posicion = models.ForeignKey(Bodega)
	Ref_Producto = models.ForeignKey(Producto)
	# Visualizacion en la grilla
	def __unicode__(self):
		return unicode(self.Ref_Producto) + ' '+ unicode(self.Cantidad) + ' ' + unicode(self.Fecha_Hora) + ' ' + unicode(self.Operacion)