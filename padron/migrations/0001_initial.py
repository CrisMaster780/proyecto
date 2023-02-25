# Generated by Django 4.1.7 on 2023-02-25 17:29

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
            name='Ciudad',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descripcion', models.CharField(max_length=200)),
                ('estado', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Mesa',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descripcion', models.CharField(max_length=200)),
                ('estado', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Orden',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descripcion', models.BooleanField(default=True)),
                ('estado', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Sucursal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descripcion', models.CharField(default=1, max_length=200)),
                ('estado', models.BooleanField(default=True)),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Persona',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=200)),
                ('apellido', models.CharField(max_length=200)),
                ('cedula', models.CharField(max_length=200)),
                ('telefono', models.CharField(max_length=200)),
                ('correo', models.CharField(max_length=200)),
                ('estado', models.BooleanField(default=True)),
                ('ciudad', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='padron.ciudad')),
                ('mesa', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='padron.mesa')),
                ('orden', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='padron.orden')),
                ('sucursal', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='padron.sucursal')),
            ],
        ),
        migrations.CreateModel(
            name='Padron',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mesa', models.CharField(max_length=200)),
                ('orden', models.CharField(max_length=200)),
                ('monto_desembolso', models.FloatField()),
                ('estado', models.BooleanField(default=True)),
                ('se_acerco', models.BooleanField(default=True)),
                ('fecha', models.DateField()),
                ('persona', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='padron.persona')),
                ('sucursal', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='padron.sucursal')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]