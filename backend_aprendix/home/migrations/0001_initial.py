# Generated by Django 4.2.7 on 2023-12-02 02:06

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='ActividadIA',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contenido_actividades', models.TextField()),
                ('promt', models.TextField(blank=True, null=True)),
                ('archivos', models.FileField(upload_to='actividades')),
            ],
        ),
        migrations.CreateModel(
            name='Curso',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_curso', models.CharField(max_length=50)),
                ('descripcion_curso', models.CharField(max_length=200)),
                ('duracion_curso', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Perfil',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('foto', models.ImageField(blank=True, null=True, upload_to='usuarios')),
                ('web', models.CharField(blank=True, max_length=50, null=True)),
                ('documento', models.CharField(blank=True, max_length=50, null=True)),
                ('id_usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Pregunta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('texto_pregunta', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Respuesta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('texto_respuesta', models.CharField(max_length=200)),
                ('estilo', models.CharField(choices=[('kinestesico', 'Kinestesico'), ('auditivo', 'Auditivo'), ('visual', 'Visual')], max_length=20)),
                ('id_pregunta', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.pregunta')),
            ],
        ),
        migrations.CreateModel(
            name='Tematica',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_tematica', models.CharField(max_length=50)),
                ('contenido_tematica', models.TextField()),
                ('id_curso', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.curso')),
            ],
        ),
        migrations.CreateModel(
            name='Resultado',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_resultado', models.DateField(auto_now_add=True)),
                ('id_perfil', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.perfil')),
                ('id_respuesta', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.respuesta')),
            ],
        ),
        migrations.CreateModel(
            name='RespuestaAct',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_perfil', models.PositiveBigIntegerField(blank=True, null=True)),
                ('fecha_progreso', models.DateField(auto_now=True)),
                ('comentario', models.TextField(blank=True, null=True)),
                ('calificacion_progreso', models.BooleanField(default=False)),
                ('id_actividadIA', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.actividadia')),
            ],
        ),
        migrations.CreateModel(
            name='Inscripcion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_inscripcion', models.DateField()),
                ('id_curso', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.curso')),
                ('id_usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.perfil')),
            ],
        ),
        migrations.AddField(
            model_name='actividadia',
            name='id_tematica',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.tematica'),
        ),
    ]
