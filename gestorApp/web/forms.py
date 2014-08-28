from django import forms
class UsuariosForm(forms.ModelForm):
	Clave=forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model = Usuarios