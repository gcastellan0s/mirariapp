# Generated by Django 2.0.5 on 2019-02-28 06:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('TCS', '0026_remove_orderservice_serial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='orderservice',
            options={'default_permissions': [], 'ordering': ['-serial'], 'permissions': [], 'verbose_name': 'Orden de servicio', 'verbose_name_plural': 'Ordenes de servicio'},
        ),
        migrations.RenameField(
            model_name='orderservice',
            old_name='s',
            new_name='serial',
        ),
    ]
