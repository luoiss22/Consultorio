# Generated by Django 5.1.2 on 2024-10-12 00:01

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cita',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Diagnostico',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descripcion', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Medicamento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='HistorialMedico',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('antecedentes', models.TextField()),
                ('alergias', models.CharField(max_length=255)),
                ('notas', models.TextField()),
                ('diagnosticos', models.ManyToManyField(to='Consultorio_app.diagnostico')),
            ],
        ),
        migrations.CreateModel(
            name='Medico',
            fields=[
                ('idMedico', models.AutoField(primary_key=True, serialize=False)),
                ('nombreCompleto', models.CharField(max_length=255)),
                ('especialidad', models.CharField(max_length=255)),
                ('citas', models.ManyToManyField(related_name='medicos', to='Consultorio_app.cita')),
            ],
        ),
        migrations.AddField(
            model_name='cita',
            name='medico',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='citas_medico', to='Consultorio_app.medico'),
        ),
        migrations.CreateModel(
            name='Paciente',
            fields=[
                ('idPaciente', models.AutoField(primary_key=True, serialize=False)),
                ('nombreCompleto', models.CharField(max_length=255)),
                ('edad', models.IntegerField()),
                ('fechaNac', models.DateField()),
                ('historialMedico', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='paciente', to='Consultorio_app.historialmedico')),
            ],
        ),
        migrations.AddField(
            model_name='cita',
            name='paciente',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='citas_paciente', to='Consultorio_app.paciente'),
        ),
        migrations.CreateModel(
            name='Recepcion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=255)),
                ('mediosDeContacto', models.JSONField()),
                ('citas', models.ManyToManyField(related_name='recepcion_citas', to='Consultorio_app.cita')),
                ('pacientes', models.ManyToManyField(related_name='recepcion_pacientes', to='Consultorio_app.paciente')),
            ],
        ),
        migrations.CreateModel(
            name='Receta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('indicaciones', models.TextField()),
                ('medicamentos', models.ManyToManyField(to='Consultorio_app.medicamento')),
            ],
        ),
        migrations.AddField(
            model_name='medico',
            name='recetas',
            field=models.ManyToManyField(related_name='recetas_medico', to='Consultorio_app.receta'),
        ),
        migrations.CreateModel(
            name='Tratamiento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descripcion', models.TextField()),
                ('duracion', models.IntegerField()),
                ('medicamentos', models.ManyToManyField(to='Consultorio_app.medicamento')),
            ],
        ),
        migrations.AddField(
            model_name='historialmedico',
            name='tratamientos',
            field=models.ManyToManyField(to='Consultorio_app.tratamiento'),
        ),
    ]
