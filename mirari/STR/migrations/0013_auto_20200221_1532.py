# Generated by Django 2.0.5 on 2020-02-21 21:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('STR', '0012_auto_20200210_1930'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='description',
            field=models.TextField(blank=True, verbose_name='DESCRIPCIÓN'),
        ),
        migrations.AlterField(
            model_name='product',
            name='codebar',
            field=models.CharField(blank=True, max_length=30, null=True, unique=True, verbose_name='Código de barras o QR'),
        ),
        migrations.AlterField(
            model_name='product',
            name='deliveryTerm',
            field=models.IntegerField(blank=True, null=True, verbose_name='Plazo entrega (días)'),
        ),
        migrations.AlterField(
            model_name='product',
            name='volume',
            field=models.FloatField(blank=True, null=True, verbose_name='Volumen (m2)'),
        ),
        migrations.AlterField(
            model_name='product',
            name='weight',
            field=models.FloatField(blank=True, null=True, verbose_name='Peso (kg)'),
        ),
    ]
