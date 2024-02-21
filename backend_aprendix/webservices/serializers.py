from rest_framework import serializers
from home.models import *


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

class CursoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Curso
        fields = '__all__'
        
class TematicaSerializer(serializers.HyperlinkedModelSerializer): 
    class Meta:
        model = Tematica
        fields = '__all__'
        depth = 1

class PreguntaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pregunta
        fields = '__all__'

class RespuestaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Respuesta 
        fields = '__all__'
        
class PerfilSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Perfil
        fields = '__all__'
        
class ResultadoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Resultado
        fields = '__all__'
        
class InscripcionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Inscripcion
        fields = '__all__'
        depth = 2
        
class ActividadIASerializer(serializers.ModelSerializer):
    class Meta:
        model = ActividadIA 
        fields = '__all__'
        
class RespuestaActSerializer(serializers.ModelSerializer):
    class Meta:
        model = RespuestaAct
        fields = '__all__'