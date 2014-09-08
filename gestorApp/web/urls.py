from django.conf.urls import patterns, url
from web import views
# Fecha creado: 25/08/2014
# Fecha actualizado: 05/09/2014
# Cambio realizado: Redefinir el metodo de carga de inventario, por la URL, Ln 9-13
urlpatterns = patterns('',
                        url(r'^$', views.index, name='index'),
						url(r'^inventario/$', views.inventario, name='inventario'),
						url(r'^inventario/crear/compra$', views.CrearCompra, name='crearcompra'),
						url(r'^inventario/crear/detallecompra$', views.CrearDetalleCompra,name='creardetallecompra'),
						url(r'^inventario/cargar$',views.CargarInventario,name='cargarinventario'),
						url(r'^inventario/descargar$',views.DescargarInventario,name='descargarinventario')
                       )