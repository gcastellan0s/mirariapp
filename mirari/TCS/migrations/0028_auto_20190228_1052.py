# Generated by Django 2.0.5 on 2019-02-28 16:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TCS', '0027_auto_20190228_0057'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='orderservice',
            options={'default_permissions': [], 'ordering': ['-serial'], 'permissions': [('Can_View__OrderService', 'Ve ordenes de servicio'), ('Can_Create__OrderService', 'Crea ordenes de servicio'), ('Can_Update__OrderService', 'Modifica ordenes de servicio'), ('Can_Delete__OrderService', 'Elimina ordenes de servicio')], 'verbose_name': 'Orden de servicio', 'verbose_name_plural': 'Ordenes de servicio'},
        ),
        migrations.AlterField(
            model_name='orderservice',
            name='creation_date',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
