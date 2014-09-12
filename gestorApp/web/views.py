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
from django.shortcuts import render, render_to_response
from web.models import Bodega, Inventario, Producto
from forms import BodegaForm, CrearCompraForm, CrearDetalleCompraForm
from django.http import HttpResponseRedirect
from datetime import datetime
from django.core.context_processors import csrf

# Create your views here.
def index(request):
    context = {}
    return render(request, 'web/index.html', context)

# Vista para procesar listado del inventario
# Fecha creado: 03/09/2014
# Fecha actualizado: 08/09/2014
# Cambio realizado: Traer la data del sistema de inventario y visualizarla en el template, Ln 23, 24
# Fecha actualizado: 12/09/2014
# Cambio realizado: cambio metodo render_to_response => render, Ln 30
def inventario(request):
	inventario = Inventario.objects.all()
	return render(request,'web/inventario.html',{'inventario_lst':inventario})
	
# Vista para crear compra para surtir el inventario
# Fecha creado: 05/09/2014
def CrearCompra(request):
	if request.POST:
		form = CrearCompraForm(request.POST)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect('/web/inventario/crear/detallecompra')
	# Despliegue del formulario antes de enviar
	else:
		form = CrearCompraForm()
	args = {}
	args.update(csrf(request))
	
	args['form'] = form
	# Renderizar a la vista
	return render_to_response('web/crear_compra.html', args)
# Vista para crear detalle de compra
# Fecha creado: 05/09/2014
# Fecha actualizado: 11/09/2014
# Cambio realizado: Corregir redireccion, de tal manera que permita realizar pedido por varios materiales, Ln 57
# Observaciones: Para el metodo CargarInventario(), se le envia el proceso Entrante al inventario (ENT)
def CrearDetalleCompra(request):
	if request.POST:
		form = CrearDetalleCompraForm(request.POST)
		if form.is_valid():
			form.save()
			# Gestion del inventario - Adicionar unidades a la entidad Gestion_Inventario
			#return HttpResponseRedirect('/web/inventario/')
			bod = request.POST['No_Posicion']
			prod = request.POST['Ref_Producto']
			estado = CargarInventario(request, 'ENT', bod, prod)
			return HttpResponseRedirect('detallecompra')
	# Despliegue del formulario antes de enviar
	else:
		form = CrearDetalleCompraForm()
	args={}
	args.update(csrf(request))
	args['form'] = form
	# Renderizar a la vista (template)
	return render_to_response('web/crear_detalle_compra.html', args)
# Metodo para implementar el cargue de inventario. Paso de la cantidad, el proceso (si es entrada o salida)
# Fecha creado: 08/09/2014
# Fecha actualizado: 11/09/2014
# Cambio realizado: Formular pseudocodigo para el proceso de inventario entrante, Ln 73-75
# Fecha actualizado: 12/09/2014
# Cambio realizado: Finalizar la rutina, para asignarla a la entidad de movimiento de inventario, Ln 80-81
def CargarInventario (request, proc, bod, prod):
	#print("Cargue de inventario en proceso")
	cant = request.POST['Cantidad']
	if proc == 'ENT':
		# El inventario registra un entrante a la cantidad, al producto, y a la bodega
		bod=Bodega.objects.get(No_Posicion=bod)
		fhora= datetime.today();		
		prod=Producto.objects.get(Ref_Producto=prod)
		inv = Inventario(Cantidad=cant, Operacion=proc, Fecha_Hora=fhora, No_Posicion=bod, Ref_Producto=prod)
		inv.save()
		# Actualizo el inventario, sumando la cantidad pedida a la original 
    #return true
	
# Vista para descargar elementos del inventario
# Fecha creado: 03/09/2014 

def DescargarInventario(request, proc, bod, prod):
	pass