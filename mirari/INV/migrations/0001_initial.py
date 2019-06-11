# Generated by Django 2.0.5 on 2019-06-09 00:53

from django.db import migrations, models
import django.db.models.deletion
import localflavor.mx.models
import mirari.INV.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('mirari', '0027_auto_20190319_1636'),
    ]

    operations = [
        migrations.CreateModel(
            name='FiscalMX',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('active', models.BooleanField(default=True)),
                ('rfc', localflavor.mx.models.MXRFCField(blank=True, max_length=13, null=True, verbose_name='RFC')),
                ('razon_social', models.CharField(blank=True, help_text='Razón social de persona Física o Moral', max_length=255, null=True, verbose_name='Razón social')),
                ('persona', models.CharField(blank=True, choices=[('FISICA', 'FISICA'), ('MORAL', 'MORAL')], default='Física', max_length=100, null=True, verbose_name='Tipo de persona')),
                ('curp', localflavor.mx.models.MXCURPField(blank=True, max_length=18, null=True, verbose_name='C.U.R.P.')),
                ('phone', models.CharField(blank=True, max_length=100, null=True, verbose_name='Teléfono contacto')),
                ('contactName', models.CharField(blank=True, max_length=255, null=True, verbose_name='Nombre contacto')),
                ('contactEmail', models.EmailField(blank=True, max_length=100, null=True, verbose_name='Email contacto')),
                ('street', models.CharField(blank=True, max_length=255, null=True, verbose_name='Calle')),
                ('extNumber', models.CharField(blank=True, max_length=150, null=True, verbose_name='No. EXT')),
                ('intNumber', models.CharField(blank=True, max_length=150, null=True, verbose_name='No. INT')),
                ('region', models.CharField(blank=True, max_length=255, null=True, verbose_name='Colonia')),
                ('province', models.CharField(blank=True, max_length=150, null=True, verbose_name='Municipio o Delegación')),
                ('state', models.CharField(blank=True, choices=[('Aguascalientes', 'Aguascalientes'), ('Baja California', 'Baja California'), ('Baja California Sur', 'Baja California Sur'), ('Campeche', 'Campeche'), ('Chihuahua', 'Chihuahua'), ('Chiapas', 'Chiapas'), ('Coahuila', 'Coahuila'), ('Colima', 'Colima'), ('CDMX', 'CDMX'), ('Durango', 'Durango'), ('Guerrero', 'Guerrero'), ('Guanajuato', 'Guanajuato'), ('Hidalgo', 'Hidalgo'), ('Jalisco', 'Jalisco'), ('Estado de México', 'Estado de México'), ('Michoacán', 'Michoacán'), ('Morelos', 'Morelos'), ('Nayarit', 'Nayarit'), ('Nuevo León', 'Nuevo León'), ('Oaxaca', 'Oaxaca'), ('Puebla', 'Puebla'), ('Querétaro', 'Querétaro'), ('Quintana Roo', 'Quintana Roo'), ('Sinaloa', 'Sinaloa'), ('San Luis Potosí', 'San Luis Potosí'), ('Sonora', 'Sonora'), ('Tabasco', 'Tabasco'), ('Tamaulipas', 'Tamaulipas'), ('Tlaxcala', 'Tlaxcala'), ('Veracruz', 'Veracruz'), ('Yucatán', 'Yucatán'), ('Zacatecas', 'Zacatecas')], max_length=100, null=True, verbose_name='Estado')),
                ('zipcode', localflavor.mx.models.MXZipCodeField(blank=True, max_length=5, null=True, verbose_name='CP.')),
                ('country', models.CharField(default='México', max_length=100, verbose_name='País')),
                ('cer', models.FileField(blank=True, null=True, upload_to=mirari.INV.models.path_FiscalMX, verbose_name='CERTIFICADO')),
                ('key', models.FileField(blank=True, null=True, upload_to=mirari.INV.models.path_FiscalMX, verbose_name='LLAVE')),
                ('password', models.CharField(blank=True, help_text='Contraseña de la llave privada', max_length=50, null=True, verbose_name='PASSWORD')),
                ('nocer', models.CharField(blank=True, help_text='Numero de certificado', max_length=50, null=True, verbose_name='')),
                ('organization', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='+', to='mirari.Organization')),
            ],
            options={
                'verbose_name': 'Dato Fiscal',
                'verbose_name_plural': 'Datos Fiscales',
                'ordering': ['-id'],
                'permissions': [('Can_View__FiscalMX', 'Ve datos fiscales'), ('Can_Create__FiscalMX', 'Crea datos fiscales'), ('Can_Update__FiscalMX', 'Modifica datos fiscales'), ('Can_Delete__FiscalMX', 'Elimina datos fiscales')],
                'abstract': False,
                'default_permissions': [],
            },
        ),
        migrations.CreateModel(
            name='Invoice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('active', models.BooleanField(default=True)),
                ('organization', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='+', to='mirari.Organization')),
            ],
            options={
                'verbose_name': 'Factura',
                'verbose_name_plural': 'Facturas',
                'ordering': ['-id'],
                'permissions': [('Can_View__Invoice', 'Ve facturas'), ('Can_Create__Invoice', 'Crea facturas'), ('Can_Update__Invoice', 'Modifica facturas'), ('Can_Delete__Invoice', 'Elimina facturas')],
                'abstract': False,
                'default_permissions': [],
            },
        ),
    ]