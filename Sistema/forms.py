from django import forms

# Formulario para el Login
class LoginForm(forms.Form):
    username=forms.CharField(widget=forms.TextInput(),label="Rut de Usuario")
    password=forms.CharField(widget=forms.PasswordInput(),label="Contraseña")

# Formulario para Email Restablece Contraseña
class RecuperacionForm(forms.Form):
    username=forms.CharField(widget=forms.TextInput(),label="Rut")

# Formulario para Restablecer Contraseña
class RestablecerForm(forms.Form):
    password_A=forms.CharField(widget=forms.PasswordInput(),label="Nueva Contraseña")
    password_B=forms.CharField(widget=forms.PasswordInput(),label="Repita Contraseña")

