# Generated by Django 5.0.2 on 2024-02-17 01:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_alter_inscripcion_usuario_alter_perfil_usuario_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Docente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('correo', models.EmailField(max_length=254)),
                ('telefono', models.CharField(max_length=15)),
                ('especialidad', models.CharField(max_length=100)),
            ],
        ),
    ]
