from django.shortcuts import render, redirect
from rest_framework import viewsets
from home.models import Docente  # Importar la clase Docente del archivo models.py en la carpeta home

from .forms import DocenteForm
from .serializers import UserSerializer, CursoSerializer, TematicaSerializer, PreguntaSerializer, RespuestaSerializer, PerfilSerializer, ResultadoSerializer, InscripcionSerializer, ActividadIASerializer, RespuestaActSerializer

from .serializers import *


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    
class CursoViewSet(viewsets.ModelViewSet):
    queryset = Curso.objects.all()
    serializer_class = CursoSerializer

class TematicaViewSet(viewsets.ModelViewSet):
    queryset = Tematica.objects.all()
    serializer_class = TematicaSerializer
    
class PreguntaViewSet(viewsets.ModelViewSet):
    queryset = Pregunta.objects.all()
    serializer_class = PreguntaSerializer

class RespuestaViewSet(viewsets.ModelViewSet): 
    queryset = Respuesta.objects.all()
    serializer_class = RespuestaSerializer

class PerfilViewSet(viewsets.ModelViewSet):
    queryset = Perfil.objects.all()
    serializer_class = PerfilSerializer
    
class ResultadoViewSet(viewsets.ModelViewSet):
    queryset = Resultado.objects.all()
    serializer_class = ResultadoSerializer

class InscripcionViewSet(viewsets.ModelViewSet):
    queryset = Inscripcion.objects.all()
    serializer_class = InscripcionSerializer

class ActividadIAViewSet(viewsets.ModelViewSet):
    queryset = ActividadIA.objects.all()
    serializer_class = ActividadIASerializer

class RespuestaActViewSet(viewsets.ModelViewSet):
    queryset = RespuestaAct.objects.all()
    serializer_class = RespuestaActSerializer



def docentes(request):
    # Obtiene todos los docentes de la base de datos
    docentes = Docente.objects.all()

    # Renderiza la plantilla docentes.html y pasa los docentes como contexto
    return render(request, 'docentes.html', {'docentes': docentes})



# Vista para listar todos los docentes
def listar_docentes(request):
    docentes = Docente.objects.all()  
    return render(request, 'listar_docentes.html', {'docentes': docentes})  

# Vista para agregar un nuevo docente
def agregar_docente(request):
    if request.method == 'POST':
        form = DocenteForm(request.POST)  
        if form.is_valid():
            form.save()  
            return redirect('listar_docentes')  
    else:
        form = DocenteForm()  
    return render(request, 'agregar_docente.html', {'form': form})

def buscar_docente(request):
    # Si se envía un formulario de búsqueda
    if request.method == 'POST':
        # Obtener el término de búsqueda del formulario
        termino_busqueda = request.POST.get('termino_busqueda', '')
        # Realizar la búsqueda de docentes que coincidan con el término de búsqueda
        docentes = Docente.objects.filter(nombre__icontains=termino_busqueda)
        # Renderizar la plantilla con los resultados de la búsqueda
        return render(request, 'buscar_docente.html', {'docentes': docentes, 'termino_busqueda': termino_busqueda})
    # Si no se envía un formulario de búsqueda, mostrar la página de búsqueda vacía
    else:
        return render(request, 'buscar_docente.html')
    
# Vista para editar un docente
def editar_docente(request, pk):
    docente = Docente.objects.get(pk=pk)
    if request.method == 'POST':
        form = DocenteForm(request.POST, instance=docente)
        if form.is_valid():
            form.save()
            return redirect('listar_docentes')
    else:
        form = DocenteForm(instance=docente)
    return render(request, 'editar_docente.html', {'form': form})


# Vista para eliminar un docente
def eliminar_docente(request, pk):
    docente = Docente.objects.get(pk=pk)
    if request.method == 'POST':
        docente.delete()
        return redirect('listar_docentes')
    return render(request, 'eliminar_docente.html', {'docente': docente})