from django.urls import path, include
from rest_framework import routers
from home.models import *
from webservices.views import *
from . import views

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
    path('', views.docentes, name='docentes'),  # URL para la página inicial (docentes.html)
    path('listar-docentes/', views.listar_docentes, name='listar_docentes'),  # URL para listar docentes
    path('agregar-docente/', views.agregar_docente, name='agregar_docente'),  # URL para agregar docente
    path('buscar/', views.buscar_docente, name='buscar_docente'),
    path('editar-docente/<int:pk>/', views.editar_docente, name='editar_docente'),
    path('eliminar-docente/<int:pk>/', views.eliminar_docente, name='eliminar_docente'),
  ]