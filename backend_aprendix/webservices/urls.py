from django.urls import path, include
from rest_framework import routers
from home.models import *
from webservices.views import *

router = routers.DefaultRouter()
router.register(r'users', UserViewSet, basename='Usuario')
router.register(r'cursos', CursoViewSet, basename='curso')
router.register(r'tematicas', TematicaViewSet, basename='tematica')
router.register(r'preguntas', PreguntaViewSet, basename='pregunta')
router.register(r'respuestas', RespuestaViewSet, basename='respuesta')
router.register(r'usuarios', PerfilViewSet, basename='usuario')
router.register(r'resultados', ResultadoViewSet, basename='resultado')
router.register(r'inscripciones', InscripcionViewSet, basename='inscripcion')
router.register(r'actividadesia', ActividadIAViewSet, basename='actividadia')
router.register(r'respuestasact', RespuestaActViewSet, basename='respuestaact')

urlpatterns = [
    path('api/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]
