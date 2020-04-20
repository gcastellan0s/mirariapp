# Generated by Django 2.0.5 on 2019-12-16 19:06

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('STR', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='deliveryDescription',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='product',
            name='receptionsDescription',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='product',
            name='users',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='product',
            name='volume',
            field=models.FloatField(blank=True, null=True, verbose_name='Volumen'),
        ),
        migrations.AddField(
            model_name='product',
            name='weight',
            field=models.FloatField(blank=True, null=True, verbose_name='Peso'),
        ),
        migrations.AlterField(
            model_name='product',
            name='canByBuy',
            field=models.BooleanField(default=True, verbose_name='Puede ser comprado?'),
        ),
        migrations.AlterField(
            model_name='product',
            name='canBySell',
            field=models.BooleanField(default=True, verbose_name='Puede ser vendido?'),
        ),
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='STR.CategoryProduct', verbose_name='Categoría del producto'),
        ),
        migrations.AlterField(
            model_name='product',
            name='codebar',
            field=models.CharField(max_length=30, verbose_name='Código de barras'),
        ),
        migrations.AlterField(
            model_name='product',
            name='costPrice',
            field=models.FloatField(blank=True, null=True, verbose_name='Costo'),
        ),
        migrations.AlterField(
            model_name='product',
            name='deliveryTerm',
            field=models.IntegerField(blank=True, null=True, verbose_name='Plazo de entrega'),
        ),
        migrations.AlterField(
            model_name='product',
            name='name',
            field=models.CharField(max_length=250, verbose_name='Nombre del producto'),
        ),
        migrations.AlterField(
            model_name='product',
            name='notes',
            field=models.TextField(blank=True, verbose_name='Notas internas'),
        ),
        migrations.AlterField(
            model_name='product',
            name='sellPrice',
            field=models.FloatField(blank=True, null=True, verbose_name='Precio de venta'),
        ),
        migrations.AlterField(
            model_name='product',
            name='typeProduct',
            field=models.CharField(choices=[('Consumible', 'Consumible'), ('Servicio', 'Servicio'), ('Almacenaje', 'Almacenaje')], default='productQuantity', max_length=250, verbose_name='Tipo de producto'),
        ),
        migrations.AlterField(
            model_name='product',
            name='uid',
            field=models.CharField(max_length=30, verbose_name='Referencia interna (PKU)'),
        ),
    ]
