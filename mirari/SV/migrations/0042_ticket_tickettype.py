# Generated by Django 2.0.5 on 2019-04-08 17:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SV', '0041_auto_20190407_1848'),
    ]

    operations = [
        migrations.AddField(
            model_name='ticket',
            name='ticketType',
            field=models.CharField(choices=[('VENTA', 'VENTA'), ('REMISION', 'REMISION'), ('DEVOLUCION', 'DEVOLUCION')], default='VENTA', max_length=100),
        ),
    ]
