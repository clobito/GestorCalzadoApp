# Importacion de clases
# Fecha creado: 25/08/2014
# Fecha actualizado: 03/09/2014
# Cambio realizado: Importacion de forms
# Fecha actualizado: 05/09/2014
# Cambio realizado: Redefinicion del metodo CrearCompra() para inicio del cargue de inventario
# Fecha actualizado: 08/09/2014
# Cambio realizado: Carga de la clase Inventario procedente del modelo.
from django.shortcuts import render, render_to_response
from web.models import Bodega, Inventario
from forms import BodegaForm, CrearCompraForm, CrearDetalleCompraForm
from django.http import HttpResponseRedirect
from django.core.context_processors import csrf

# Create your views here.
def index(request):
    context = {}
    return render(request, 'web/index.html', context)

# Vista para procesar listado del inventario
# Fecha creado: 03/09/2014
# Fecha actualizado: 08/09/2014
# Cambio realizado: Traer la data del sistema de inventario y visualizarla en el template, Ln 23, 24
def inventario(request):
	inventario = Inventario.objects.all()
	return render_to_response('web/inventario.html',{'inventario_lst':inventario})
	
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
def CrearDetalleCompra(request):
	if request.POST:
		form = CrearDetalleCompraForm(request.POST)
		if form.is_valid():
			form.save()
			# Gestion del inventario - Adicionar unidades a la entidad Gestion_Inventario
			#return HttpResponseRedirect('/web/inventario/')
			CargarInventario()
			return HttpResponseRedirect('web/crear_detalle_compra.html')
	# Despliegue del formulario antes de enviar
	else:
		form = CrearDetalleCompraForm()
	args={}
	args.update(csrf(request))
	args['form'] = form
	# Renderizar a la vista
	return render_to_response('web/crear_detalle_compra.html', args)
# Método para implementar el cargue de inventario
# Fecha creado: 08/09/2014
def CargarInventario (request):
	print("Cargue de inventario en proceso")
# Vista para descargar elementos del inventario
# Fecha creado: 03/09/2014 
def DescargarInventario(request):
	pass