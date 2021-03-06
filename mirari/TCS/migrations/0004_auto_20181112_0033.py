# Generated by Django 2.0.5 on 2018-11-12 06:33

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mirari', '0007_auto_20181025_1307'),
        ('TCS', '0003_auto_20181107_1151'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='orderservice',
            name='reporta',
        ),
        migrations.RemoveField(
            model_name='orderservice',
            name='street',
        ),
        migrations.RemoveField(
            model_name='orderservice',
            name='street_notes',
        ),
        migrations.AddField(
            model_name='brand',
            name='organization',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='mirari.Organization'),
        ),
        migrations.AddField(
            model_name='modelo',
            name='organization',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='mirari.Organization'),
        ),
        migrations.AddField(
            model_name='orderservice',
            name='address',
            field=models.CharField(blank=True, max_length=500, verbose_name='Calle'),
        ),
        migrations.AddField(
            model_name='orderservice',
            name='address_lat',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='orderservice',
            name='address_lng',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='orderservice',
            name='client_notes',
            field=models.TextField(blank=True, verbose_name='Notas sobre el cliente'),
        ),
        migrations.AddField(
            model_name='orderservice',
            name='organization',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='mirari.Organization'),
        ),
        migrations.AddField(
            model_name='orderservice',
            name='report_name',
            field=models.CharField(blank=True, max_length=250, verbose_name='Numero de serie'),
        ),
        migrations.AddField(
            model_name='store',
            name='organization',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='mirari.Organization'),
        ),
        migrations.AlterField(
            model_name='orderservice',
            name='brand',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='TCS.Brand', verbose_name='Marca'),
        ),
        migrations.AlterField(
            model_name='orderservice',
            name='buy_date',
            field=models.DateField(blank=True, null=True, verbose_name='Fecha de compra'),
        ),
        migrations.AlterField(
            model_name='orderservice',
            name='client_name',
            field=models.CharField(max_length=500, verbose_name='Nombre completo del cliente'),
        ),
        migrations.AlterField(
            model_name='orderservice',
            name='concept',
            field=models.CharField(choices=[('Armado', 'Armado'), ('Revision', 'Revision'), ('OrdenesIcon', 'OrdenesIcon'), ('Mantenimiento', 'Mantenimiento'), ('Servicio', 'Servicio')], default='Armado', max_length=250, verbose_name='Concepto'),
        ),
        migrations.AlterField(
            model_name='orderservice',
            name='contact_phone1',
            field=models.CharField(blank=True, max_length=250, verbose_name='Teléfono de contacto del cliente'),
        ),
        migrations.AlterField(
            model_name='orderservice',
            name='contact_phone2',
            field=models.CharField(blank=True, max_length=250, verbose_name='Teléfono de contacto del cliente'),
        ),
        migrations.AlterField(
            model_name='orderservice',
            name='delivery_date',
            field=models.DateField(blank=True, null=True, verbose_name='Fecha de entrega'),
        ),
        migrations.AlterField(
            model_name='orderservice',
            name='email',
            field=models.CharField(blank=True, max_length=250, verbose_name='Email del cliente'),
        ),
        migrations.AlterField(
            model_name='orderservice',
            name='hidden_notes',
            field=models.TextField(blank=True, verbose_name='Notas <small>(No se imprimen en la orden)</small>'),
        ),
        migrations.AlterField(
            model_name='orderservice',
            name='modelo',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='TCS.Modelo', verbose_name='Modelo'),
        ),
        migrations.AlterField(
            model_name='orderservice',
            name='order_notes',
            field=models.TextField(blank=True, verbose_name='Notas <small>(Impresas en la orden)</small>'),
        ),
        migrations.AlterField(
            model_name='orderservice',
            name='serial_number',
            field=models.CharField(blank=True, max_length=250, verbose_name='Numero de serie'),
        ),
        migrations.AlterField(
            model_name='orderservice',
            name='service',
            field=models.CharField(choices=[('Icon', 'Icon'), ('Tecnoservicio', 'Tecnoservicio')], default='Icon', max_length=250, verbose_name='Tipo de servicio'),
        ),
        migrations.AlterField(
            model_name='orderservice',
            name='service_date',
            field=models.DateField(verbose_name='Fecha programada'),
        ),
        migrations.AlterField(
            model_name='orderservice',
            name='status',
            field=models.CharField(choices=[('Nueva', 'Nueva'), ('Alerta', 'Alerta'), ('Espera de refacciones', 'Espera de refacciones'), ('Terminada', 'Terminada'), ('Cancelada', 'Cancelada'), ('Especial', 'Especial')], max_length=250, verbose_name='Estatus'),
        ),
        migrations.AlterField(
            model_name='orderservice',
            name='store',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='TCS.Store', verbose_name='Tienda'),
        ),
        migrations.AlterField(
            model_name='orderservice',
            name='technical',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL, verbose_name='Tecnico'),
        ),
        migrations.AlterField(
            model_name='orderservice',
            name='zone',
            field=models.CharField(choices=[('Local', 'Local'), ('Foraneo', 'Foraneo')], default='Local', max_length=250, verbose_name='Zona'),
        ),
    ]
