# Generated by Django 4.1.7 on 2023-02-25 21:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('padron', '0003_alter_padron_monto_desembolso'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sucursal',
            name='descripcion',
            field=models.CharField(max_length=200),
        ),
    ]
