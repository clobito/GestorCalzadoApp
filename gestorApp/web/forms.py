# Definicion de formularios
# Fecha creado: 03/09/2014
# Proposito: Definir el contenedor donde se definen los metodos para renderizar los formularios en Django
# Modulo asociado: Inventarios

from django import forms
from models import Bodega, Usuario, Compra_Material, Detalle_Compra_Material

# Formulario de ejemplo para generar administrador de bodega
# Fecha creado: 03/09/2014
class BodegaForm(forms.ModelForm):
	class Meta:
		model=Bodega
# Formulario para descargar el inventario en funcion de la venta del producto
# Fecha creado: 03/09/2014
class DescargarInventarioForm(forms.ModelForm):
	pass
# Formulario para cargar el inventario en funcion de la compra del producto
# Fecha creado: 03/09/2014
class CargarInventarioForm(forms.ModelForm):
	pass
# Formulario para crear la compra
# Fecha creado: 05/09/2014
# Fecha actualizado: 15/09/2014
# Cambio realizado: Implementar formulario de compra, desplegando los 3 campos: Numero de compra, Fecha y Observaciones, Ln 29
# Fecha actualizado: 17/09/2014
# Cambio realizado: Colocar campo No_compra como entero y validandolo con valores > 0, Ln 29, 32
#class CrearCompraForm(forms.ModelForm):
class CompraForm(forms.ModelForm):		
	class Meta:
		model=Compra_Material
		fields=('Fecha','Observaciones')
# Fecha creado: 17/09/2014
# Proposito: Crear el numero de orden de compra que herede de la compra. FUENTE: https://code.djangoproject.com/wiki/CookBookNewFormsFieldOrdering
class CrearCompraForm(CompraForm):
	No_compra = forms.IntegerField(min_value=1)
	
	def __init__(self, *args, **kwargs):
		super(CrearCompraForm, self).__init__(*args, **kwargs)
		self.fields.keyOrder = ['No_compra','Fecha','Observaciones']		
# Formulario para crear detalle de compra, asociado a la compra.
# Fecha creado: 08/09/2014
# Fecha actualizado: 15/09/2014
# Cambio realizado: Implementar combo para las tallas, Ln 37,38. FUENTE: http://stackoverflow.com/questions/3463700/django-combobox
# Fecha realizado: 22/09/2014
# Cambio realizado: Desactivar control de lista, ya que se crea en el modelo (models.py, clase Detalle_Compra_Material()), Ln 50-57
class CrearDetalleCompraForm(forms.ModelForm):	
	class Meta:
		model=Detalle_Compra_Material
		"""SELECTED_VAL = (
		('S','S'),
		('M','M'),
		('L','L'),
		('XL','XL'),
		('XXL','XXL'),
		)
		Talla = forms.ChoiceField(choices=SELECTED_VAL)
		widgets={
			'Talla': forms.ChoiceField(),
			'choices': SELECTED_VAL,
		}"""
# Campo tipo password para el modulo de usuario
# Fecha creado: 05/09/2014.
# FUENTE: http://stackoverflow.com/questions/3532354/django-password-problems
class UsuarioForm(forms.ModelForm):
	Clave = forms.CharField(widget=forms.PasswordInput())
	class Meta:
		model = Usuario
		fields = ('Clave',)
		widgets={
		 'Clave': forms.PasswordInput(),
		}