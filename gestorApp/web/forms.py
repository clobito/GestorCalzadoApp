# Definicion de formularios
# Fecha creado: 03/09/2014
# Proposito: Definir el contenedor donde se definen los metodos para renderizar los formularios en Django
# Modulo asociado: Inventarios

from django import forms
from models import Bodega, Usuario

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