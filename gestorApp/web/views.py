# Importacion de clases
# Fecha creado: 25/08/2014
# Fecha actualizado: 03/09/2014
# Cambio realizado: Importacion de forms
# Fecha actualizado: 05/09/2014
# Cambio realizado: Redefinicion del metodo CrearCompra() para inicio del cargue de inventario
# Fecha actualizado: 08/09/2014
# Cambio realizado: Carga de la clase Inventario procedente del modelo.
# Fecha actualizado: 12/09/2014
# Cambio realizado: Inclusion de la libreria de tiempo, Ln 15. Inclusion de la clase Producto desde el modelo, Ln 12
# Fecha actualizado: 17/09/2014
# Cambio realizado: Inclusion del modulo Compra_Material, Ln 14
from django.shortcuts import render, render_to_response
from web.models import Bodega, Inventario, Producto, Compra_Material
from forms import BodegaForm, CrearCompraForm, CrearDetalleCompraForm
from django.http import HttpResponseRedirect
from datetime import datetime
from django.core.context_processors import csrf

# Create your views here.
# Fecha actualizado: 19/09/2014
# Cambio realizado: Direccionar al template base.html, Ln 25
def index(request):
    context = {}
    return render(request, 'web/base.html', context)

# Vista para procesar listado del inventario
# Fecha creado: 03/09/2014
# Fecha actualizado: 08/09/2014
# Cambio realizado: Traer la data del sistema de inventario y visualizarla en el template, Ln 23, 24
# Fecha actualizado: 12/09/2014
# Cambio realizado: cambio metodo render_to_response => render, Ln 30
# Fecha actualizado: 22/09/2014
# Cambio realizado: Realizar un "Join" entre las entidades Gestion_Inventario y Producto para obtener la cantidad disponible del producto, Ln 36 ()
def inventario(request):
	inventario = Inventario.objects.select_related('Producto')
	#qry	=	"SELECT * FROM web_inventario INNER JOIN web_producto ON ('web_producto.Ref_Producto'='web_inventario.Ref_Producto')"
	#inventario=Inventario.objects.raw(qry)
	return render(request,'web/inventario.html',{'inventario_lst':inventario})
	
# Vista para crear compra para surtir el inventario
# Fecha creado: 05/09/2014
# Fecha actualizado: 17/09/2014
# Cambio realizado: Devolver objeto a la vista, Ln 52. Almacenar el campo No_compra como string a la BD, Ln 41. FUENTE: http://bytes.com/topic/python/answers/20874-converting-integer-string
def CrearCompra(request):
	if request.POST:
		form = CrearCompraForm(request.POST)
		if form.is_valid():
			#conversion a string
			num_compra = str(request.POST['No_compra'])
			#Carga de campos
			Fecha=request.POST['Fecha']
			Observaciones=request.POST['Observaciones']
			#Almacenamiento
			compra= Compra_Material(No_compra=num_compra,Fecha=Fecha,Observaciones=Observaciones)
			#form.save()
			compra.save()
			return HttpResponseRedirect('/web/inventario/crear/detallecompra')
	# Despliegue del formulario antes de enviar
	else:
		form = CrearCompraForm()
	args = {}
	args.update(csrf(request))
	
	args['form'] = form
	# Renderizar a la vista
	#return render_to_response('web/crear_compra.html', args)
	return render(request, 'web/crear_compra.html', args)
# Vista para crear detalle de compra
# Fecha creado: 05/09/2014
# Fecha actualizado: 11/09/2014
# Cambio realizado: Corregir redireccion, de tal manera que permita realizar pedido por varios materiales, Ln 57
# Observaciones: Para el metodo CargarInventario(), se le envia el proceso Entrante al inventario (ENT)
# Fecha actualizado: 17/09/2014
# Cambio realizado: Renderizar el template con el CSS del frontend, Ln 89
# Fecha actualizado: 22/09/2014
# Cambio realizado: Derivar los eventos, para causar el cierre de la Orden de compra (FUENTE: http://stackoverflow.com/questions/866272/how-can-i-build-multiple-submit-buttons-django-form), Ln 79
def CrearDetalleCompra(request):
	if 'crearprod' in request.POST:
		form = CrearDetalleCompraForm(request.POST)
		if form.is_valid():
			form.save()
			# Gestion del inventario - Adicionar unidades a la entidad Gestion_Inventario
			#return HttpResponseRedirect('/web/inventario/')
			bod = request.POST['No_Posicion']
			prod = request.POST['Ref_Producto']
			estado = CargarInventario(request, 'ENT', bod, prod)
			return HttpResponseRedirect('detallecompra')
	elif 'cierreoc' in request.POST:
		CerrarOrden(request)
		inventario = Inventario.objects.select_related('Producto')	
		return render(request,'web/inventario.html',{'inventario_lst':inventario})
		
	# Despliegue del formulario antes de enviar
	else:
		form = CrearDetalleCompraForm()
	args={}
	args.update(csrf(request))
	args['form'] = form
	# Renderizar a la vista (template)
	#return render_to_response('web/crear_detalle_compra.html', args)
	return render(request, 'web/crear_detalle_compra.html', args)
# Metodo para implementar el cargue de inventario. Paso de la cantidad, el proceso (si es entrada o salida)
# Fecha creado: 08/09/2014
# Fecha actualizado: 11/09/2014
# Cambio realizado: Formular pseudocodigo para el proceso de inventario entrante, Ln 73-75
# Fecha actualizado: 12/09/2014
# Cambio realizado: Finalizar la rutina, para asignarla a la entidad de movimiento de inventario, Ln 80-81
def CargarInventario (request, proc, bod, prod):	
	cant = request.POST['Cantidad']
	if proc == 'ENT':
		# El inventario registra un entrante a la cantidad, al producto, y a la bodega
		bod=Bodega.objects.get(No_Posicion=bod)
		fhora= datetime.today()		
		prod=Producto.objects.get(Ref_Producto=prod)
		inv = Inventario(Cantidad=cant, Operacion=proc, Fecha_Hora=fhora, No_Posicion=bod, Ref_Producto=prod)
		inv.save()
		# Actualizo el inventario, sumando la cantidad pedida a la original
		ActualizarInventario(request, proc)
	#return true
	
# Vista para descargar elementos del inventario
# Fecha creado: 03/09/2014 

def DescargarInventario(request, proc, bod, prod):
	pass
# Proposito: Actualizar el inventario, sumando (o restando) la cantidad asociado al producto.
# Fecha creado: 22/09/2014
# Observaciones: 1.Acceso a queries mediante manual en la URL: https://docs.djangoproject.com/en/1.7/ref/models/queries/ 2.Conversion unicode a integer mediante la URL: http://bytes.com/topic/python/answers/164011-convert-unicode-int	
def ActualizarInventario(request, proc):
	#Cargar la cantidad actual
	Prod=Producto.objects.get(Ref_Producto=request.POST['Ref_Producto'])
	if proc == 'ENT':		
		#Actualizar la cantidad en la base
		Prod.Cantidad += int(request.POST['Cantidad'])
	elif proc == 'SAL':
		#Actualizar la cantidad en la base
		Prod.Cantidad -= int(request.POST['Cantidad'])
	#Actualizamos en la base
	Prod.save()

# Proposito: Cerrar la orden de compra, para no visualizarla al realizar la orden de pedido.
# Fecha creado: 22/09/2014
def CerrarOrden(request):
	ocompra=request.POST['No_compra']
	Compra=Compra_Material.objects.get(No_compra=ocompra)
	Compra.OC_cerrada=str(1)
	#Actualizamos en la base
	Compra.save()