# Generated by Django 2.0.5 on 2019-12-20 21:44

from django.db import migrations, models
import django.db.models.deletion
import localflavor.mx.models


class Migration(migrations.Migration):

    dependencies = [
        ('mirari', '0034_auto_20190709_1256'),
        ('STR', '0005_auto_20191220_1457'),
    ]

    operations = [
        migrations.CreateModel(
            name='Storehouse',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('active', models.BooleanField(default=True)),
                ('name', models.CharField(help_text='Nombre con el que identificas al proveedor', max_length=250, verbose_name='Alias')),
                ('street', models.CharField(blank=True, max_length=255, null=True, verbose_name='Calle')),
                ('extNumber', models.CharField(blank=True, max_length=150, null=True, verbose_name='No. EXT')),
                ('intNumber', models.CharField(blank=True, max_length=150, null=True, verbose_name='No. INT')),
                ('region', models.CharField(blank=True, max_length=255, null=True, verbose_name='Colonia')),
                ('province', models.CharField(blank=True, max_length=150, null=True, verbose_name='Municipio o Delegación')),
                ('state', models.CharField(blank=True, choices=[('Aguascalientes', 'Aguascalientes'), ('Baja California', 'Baja California'), ('Baja California Sur', 'Baja California Sur'), ('Campeche', 'Campeche'), ('Chihuahua', 'Chihuahua'), ('Chiapas', 'Chiapas'), ('Coahuila', 'Coahuila'), ('Colima', 'Colima'), ('CDMX', 'CDMX'), ('Durango', 'Durango'), ('Guerrero', 'Guerrero'), ('Guanajuato', 'Guanajuato'), ('Hidalgo', 'Hidalgo'), ('Jalisco', 'Jalisco'), ('Estado de México', 'Estado de México'), ('Michoacán', 'Michoacán'), ('Morelos', 'Morelos'), ('Nayarit', 'Nayarit'), ('Nuevo León', 'Nuevo León'), ('Oaxaca', 'Oaxaca'), ('Puebla', 'Puebla'), ('Querétaro', 'Querétaro'), ('Quintana Roo', 'Quintana Roo'), ('Sinaloa', 'Sinaloa'), ('San Luis Potosí', 'San Luis Potosí'), ('Sonora', 'Sonora'), ('Tabasco', 'Tabasco'), ('Tamaulipas', 'Tamaulipas'), ('Tlaxcala', 'Tlaxcala'), ('Veracruz', 'Veracruz'), ('Yucatán', 'Yucatán'), ('Zacatecas', 'Zacatecas')], default='CDMX', max_length=100, null=True, verbose_name='Estado')),
                ('zipcode', localflavor.mx.models.MXZipCodeField(blank=True, max_length=5, null=True, verbose_name='CP')),
                ('country', models.CharField(default='México', max_length=100, verbose_name='País')),
                ('organization', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='+', to='mirari.Organization')),
            ],
            options={
                'permissions': [('Can_View__Storehouse', 'Ve almacenes'), ('Can_Create__Storehouse', 'Crea almacenes'), ('Can_Update__Storehouse', 'Modifica almacenes'), ('Can_Delete__Storehouse', 'Elimina almacenes')],
                'verbose_name_plural': 'Almacenes',
                'verbose_name': 'Almacén',
                'ordering': ['-id'],
                'abstract': False,
                'default_permissions': [],
            },
        ),
        migrations.AlterField(
            model_name='provider',
            name='name',
            field=models.CharField(help_text='Nombre con el que identificas al proveedor', max_length=250, verbose_name='Alias'),
        ),
    ]
