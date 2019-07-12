# Generated by Django 2.0.5 on 2019-07-11 21:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SV', '0070_product_photo'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='recipe',
            field=models.ManyToManyField(help_text='Se compone de estos productos', related_name='_product_recipe_+', to='SV.Product', verbose_name='Receta'),
        ),
        migrations.AddField(
            model_name='productattributes',
            name='quantity',
            field=models.FloatField(default=0),
        ),
    ]
