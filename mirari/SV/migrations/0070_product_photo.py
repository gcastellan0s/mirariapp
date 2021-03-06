# Generated by Django 2.0.5 on 2019-07-09 22:15

from django.db import migrations
import imagekit.models.fields
import mirari.SV.models


class Migration(migrations.Migration):

    dependencies = [
        ('SV', '0069_auto_20190709_1559'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='photo',
            field=imagekit.models.fields.ProcessedImageField(blank=True, help_text='Esta imagen se muestra en el botón del punto de venta', null=True, upload_to=mirari.SV.models.pathProductImage, verbose_name='Imagen del producto'),
        ),
    ]
