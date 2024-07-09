from django.db import models
from django import forms
from .models import User,Producto
from django.contrib.auth.forms import UserCreationForm
from django.forms import ValidationError
from django.core.validators import RegexValidator

class UserForm(UserCreationForm):
    rut = forms.CharField(label='RUT', max_length=12, validators=[
        RegexValidator(
            regex=r'^\d{7,8}[-]?[\dkK]$',
            message='El RUT ingresado no es válido',
            code='invalid_rut'
        ),
    ])

    class Meta:
        model = User
        fields = ['username','rut','first_name','last_name','email','direccion','password1','password2']

    def clean_first_name(self):
        first_name = self.cleaned_data['first_name']
        if not first_name.isalpha():
            raise forms.ValidationError("El nombre debe contener solo letras.")
        return first_name

    def clean_last_name(self):
        last_name = self.cleaned_data['last_name']
        if not last_name.isalpha():
            raise forms.ValidationError("El apellido debe contener solo letras.")
        return last_name
    

class UpdUserForm(forms.ModelForm):
    rut = forms.CharField(label='RUT', max_length=12, validators=[
        RegexValidator(
            regex=r'^\d{7,8}[-]?[\dkK]$',
            message='El RUT ingresado no es válido',
            code='invalid_rut'
        ),
    ])

    old_password = forms.CharField(label='Contraseña Antigua', widget=forms.PasswordInput, required=False)
    new_password1 = forms.CharField(label='Nueva Contraseña', widget=forms.PasswordInput, required=False)
    new_password2 = forms.CharField(label='Confirmar Nueva Contraseña', widget=forms.PasswordInput, required=False)

    class Meta:
        model = User
        fields = ['username', 'rut', 'first_name', 'last_name', 'email', 'direccion']

    def __init__(self, *args, **kwargs):
        super(UpdUserForm, self).__init__(*args, **kwargs)
        self.fields['username'].disabled = True  # Para evitar que se modifique el nombre de usuario

    def clean_first_name(self):
        first_name = self.cleaned_data['first_name']
        if not first_name.isalpha():
            raise forms.ValidationError("El nombre debe contener solo letras.")
        return first_name

    def clean_last_name(self):
        last_name = self.cleaned_data['last_name']
        if not last_name.isalpha():
            raise forms.ValidationError("El apellido debe contener solo letras.")
        return last_name

    def clean(self):
        cleaned_data = super().clean()
        old_password = cleaned_data.get('old_password')
        new_password1 = cleaned_data.get('new_password1')
        new_password2 = cleaned_data.get('new_password2')

        if new_password1 and new_password1 != new_password2:
            raise forms.ValidationError("Las contraseñas nuevas no coinciden.")

        return cleaned_data

    def save(self, commit=True):
        user = super().save(commit=False)

        # Guardar la contraseña si se proporciona una nueva
        new_password = self.cleaned_data.get('new_password1')
        if new_password:
            user.set_password(new_password)

        if commit:
            user.save()

        return user

class ProductoForm(forms.ModelForm):
    codigo_producto=forms.CharField(min_length=2,max_length=50,required=True)
    nombre_producto=forms.CharField(min_length=2,max_length=50,required=True)
    precio= forms.IntegerField(min_value=1, max_value=150000000)

    class Meta:
        model = Producto
        fields = ['codigo_producto','nombre_producto','cantidad','tipo','precio','imagen']

class UpdProductoForm(forms.ModelForm):
       
    class Meta:
        model = Producto
        fields = ['nombre_producto','cantidad','tipo','precio','imagen']