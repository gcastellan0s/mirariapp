# Generated by Django 2.0.5 on 2019-02-27 17:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TCS', '0021_orderservice_serial'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderservice',
            name='address_reference',
            field=models.CharField(blank=True, max_length=500, verbose_name='Referencias'),
        ),
        migrations.AddField(
            model_name='orderservice',
            name='city',
            field=models.CharField(blank=True, max_length=250, verbose_name='Ciudad'),
        ),
        migrations.AddField(
            model_name='orderservice',
            name='colony',
            field=models.CharField(blank=True, max_length=250, verbose_name='Colonia'),
        ),
        migrations.AddField(
            model_name='orderservice',
            name='cp',
            field=models.CharField(blank=True, max_length=250, verbose_name='CP'),
        ),
        migrations.AlterField(
            model_name='orderservice',
            name='address',
            field=models.CharField(blank=True, max_length=500, verbose_name='Dirección'),
        ),
    ]
