from rest_framework import viewsets
from home.models import *
from .serializers import *

class UserViewSet(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()
    
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


