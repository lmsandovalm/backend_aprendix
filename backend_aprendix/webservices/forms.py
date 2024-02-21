from django import forms
from home.models import Docente



# Definir un formulario para el modelo de datos de Docente
class DocenteForm(forms.ModelForm):
    class Meta:
        model = Docente  # Especificar el modelo al que está asociado el formulario
        fields = ['nombre', 'correo', 'telefono', 'especialidad']  # Definir los campos del formulario