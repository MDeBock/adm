# Generated by Django 4.2.3 on 2023-07-08 09:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('proveedores', '0002_rename_factura_proveedor_facturat_compra'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ususario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50, verbose_name='Nombre')),
                ('apellido', models.CharField(max_length=50, verbose_name='Apellido')),
                ('user_name', models.CharField(max_length=20, unique=True, verbose_name='Nombre de Ususario')),
                ('password', models.CharField(max_length=20, verbose_name='Contraseña')),
                ('email', models.EmailField(max_length=254, verbose_name='Email')),
                ('tipo', models.CharField(default='proveedor', max_length=20, verbose_name='Tipo')),
                ('estado', models.BooleanField(default=True, verbose_name='Estado')),
            ],
        ),
    ]
