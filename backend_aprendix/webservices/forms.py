from django import forms
from home.models import Docente

# Definir un formulario para el modelo de datos de Docente
class DocenteForm(forms.ModelForm):
    class Meta:
        model = Docente  # Especificar el modelo al que está asociado el formulario
        fields = ['nombre', 'correo', 'telefono', 'especialidad']  # Definir los campos del formulario

        # Definir clases CSS para los campos del formulario
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'correo': forms.EmailInput(attrs={'class': 'form-control'}),
            'telefono': forms.TextInput(attrs={'class': 'form-control'}),
            'especialidad': forms.TextInput(attrs={'class': 'form-control'}),
        }