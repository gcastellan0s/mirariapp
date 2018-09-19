# Generated by Django 2.0.5 on 2018-09-17 20:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SV', '0002_auto_20180911_1551'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='menu',
        ),
        migrations.AddField(
            model_name='product',
            name='menu',
            field=models.ManyToManyField(help_text='Elige el o los menus donde se vende este producto', related_name='_product_menu_+', to='SV.Menu', verbose_name=''),
        ),
        migrations.AlterField(
            model_name='product',
            name='sellpoints',
            field=models.ManyToManyField(help_text='Se vende en estas sucursales', related_name='_product_sellpoints_+', to='SV.Sellpoint', verbose_name=''),
        ),
    ]
