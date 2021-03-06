# Generated by Django 2.0.5 on 2019-03-12 20:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SV', '0012_auto_20190312_1300'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='offers',
            options={'default_permissions': [], 'ordering': ['-id'], 'permissions': [('Can_View__Offers', 'Ve descuentos'), ('Can_Create__Offers', 'Crea descuentos'), ('Can_Update__Offers', 'Modifica descuentos'), ('Can_Delete__Offers', 'Elimina descuentos')], 'verbose_name': 'Descuento', 'verbose_name_plural': 'Descuentos'},
        ),
        migrations.AlterField(
            model_name='offers',
            name='conditionType',
            field=models.CharField(choices=[('productQuantity', 'Cantidad de productos mínima'), ('productValue', 'Valor fijo del producto')], default='% del producto', max_length=250, verbose_name='Forma de generar el descuento'),
        ),
        migrations.AlterField(
            model_name='offers',
            name='finalDate',
            field=models.DateTimeField(blank=True, help_text='Fecha y hora del fin', null=True, verbose_name='Fecha final'),
        ),
        migrations.AlterField(
            model_name='offers',
            name='initialDate',
            field=models.DateTimeField(blank=True, help_text='Fecha y hora del inicio', null=True, verbose_name='Fecha inicial'),
        ),
    ]
