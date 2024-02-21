from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models
from django.contrib.auth.models import User


class User(AbstractUser):
    groups = models.ManyToManyField(
        Group, 
        related_name='custom_groups'
    )

    user_permissions = models.ManyToManyField(
        Permission,
        related_name='custom_user_permissions'
    )
    ADMIN = 'A'
    INSTRUCTOR = 'I' 
    APRENDIZ = 'S'
    
    ROLE_CHOICES = [
        (ADMIN, 'Administrador'),
        (INSTRUCTOR, 'Instructor'),
        (APRENDIZ, 'Aprendiz')
    ]

    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)  
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=128)
    role = models.CharField(max_length=1, choices=ROLE_CHOICES)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Perfil(models.Model):
    usuario = models.OneToOneField(User, null=False, on_delete=models.CASCADE, default=1)
    foto = models.ImageField(upload_to='usuarios', null=True, blank=True)
    web = models.CharField(max_length=50, null=True, blank=True)
    documento = models.CharField(max_length=50, null=True, blank=True)

    def __str__(self):
        return f"Perfil de {self.usuario}"

class Pregunta(models.Model):
    texto_pregunta = models.CharField(max_length=200)

    def __str__(self):
        return self.texto_pregunta

class Respuesta(models.Model):
    estilos = (
        ("kinestesico","Kinestesico"),
        ("auditivo","Auditivo"),
        ("visual","Visual"),
    )
    id_pregunta = models.ForeignKey(Pregunta, on_delete=models.CASCADE)
    texto_respuesta = models.CharField(max_length=200)
    estilo = models.CharField(max_length=20, choices = estilos)

    def __str__(self):
        return self.texto_respuesta

class Resultado(models.Model):
    respuesta = models.ForeignKey(Respuesta, on_delete=models.CASCADE)
    usuario = models.ForeignKey(User, null=False, on_delete=models.CASCADE, default=1)
    fecha_resultado = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"Resultado de {self.usuario}: {self.respuesta}"

class Curso(models.Model):
    nombre_curso = models.CharField(max_length=50)
    descripcion_curso = models.CharField(max_length=200)
    duracion_curso = models.IntegerField()

    def __str__(self):
        return self.nombre_curso

class Inscripcion(models.Model): 
    usuario = models.ForeignKey(User, null=False, on_delete=models.CASCADE, default=1)
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE)
    fecha_inscripcion = models.DateField()

    def __str__(self):
        return f"Inscripción de {self.usuario} en curso {self.curso}"

class Tematica(models.Model):
    id_curso = models.ForeignKey(Curso, on_delete=models.CASCADE)
    nombre_tematica = models.CharField(max_length=50)
    contenido_tematica = models.TextField()

    def __str__(self):
        return f"Tema {self.nombre_tematica} del curso {self.id_curso}"

class ActividadIA(models.Model):
    id_tematica = models.ForeignKey(Tematica, on_delete=models.CASCADE)
    contenido_actividades = models.TextField()
    promt = models.TextField(null=True, blank=True)
    archivos = models.FileField(upload_to='actividades')

    def __str__(self):
        return f"Actividad de IA para el tema {self.id_tematica}"

class RespuestaAct(models.Model):
    id_actividadIA          = models.ForeignKey(ActividadIA, on_delete=models.CASCADE)
    id_perfil               = models.PositiveBigIntegerField(null=True, blank=True)  
    fecha_progreso          = models.DateField(auto_now=True)
    comentario              = models.TextField(null=True, blank=True)
    calificacion_progreso   = models.BooleanField(default=False)

    def __str__(self):
        return f"Respuesta a la actividad de IA ({self.id_actividadIA}): {self.calificacion_progreso}"

class Docente(models.Model):
    nombre = models.CharField(max_length=100)
    correo = models.EmailField()
    telefono = models.CharField(max_length=15)
    especialidad = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre