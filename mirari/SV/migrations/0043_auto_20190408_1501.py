# Generated by Django 2.0.5 on 2019-04-08 20:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SV', '0042_ticket_tickettype'),
    ]

    operations = [
        migrations.AlterField(
            model_name='offer',
            name='conditionValue',
            field=models.FloatField(verbose_name='Valor del descuento'),
        ),
        migrations.AlterField(
            model_name='offer',
            name='discountValue',
            field=models.FloatField(verbose_name='Valor del descuento'),
        ),
        migrations.AlterField(
            model_name='ticket',
            name='ticketType',
            field=models.CharField(choices=[('VENTA', 'VENTA'), ('REMISION', 'REMISION'), ('PAGO', 'PAGO'), ('DEVOLUCION', 'DEVOLUCION')], default='VENTA', max_length=100),
        ),
    ]