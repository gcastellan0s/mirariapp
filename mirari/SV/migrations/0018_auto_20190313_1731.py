# Generated by Django 2.0.5 on 2019-03-13 23:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mirari', '0026_remove_profile_y'),
        ('SV', '0017_auto_20190313_1135'),
    ]

    operations = [
        migrations.CreateModel(
            name='Offer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('active', models.BooleanField(default=True)),
                ('name', models.CharField(max_length=250, verbose_name='Nombre del descuento')),
                ('discountType', models.CharField(choices=[('productPercent', 'Porcentaje del producto'), ('productValue', 'Valor fijo del producto')], default='% del producto', max_length=250, verbose_name='Forma de aplicar el descuento')),
                ('discountValue', models.PositiveIntegerField(verbose_name='Valor del descuento')),
                ('conditionType', models.CharField(choices=[('productQuantity', 'Cantidad de productos mínima'), ('productValue', 'Valor fijo del producto')], default='% del producto', max_length=250, verbose_name='Forma de generar el descuento')),
                ('conditionValue', models.PositiveIntegerField(verbose_name='Valor del descuento')),
                ('initialDate', models.DateTimeField(blank=True, help_text='Fecha y hora del inicio', null=True, verbose_name='Fecha inicial')),
                ('finalDate', models.DateTimeField(blank=True, help_text='Fecha y hora del fin', null=True, verbose_name='Fecha final')),
                ('is_active', models.BooleanField(default=True, help_text='Desactivar Descuento?', verbose_name='Esta activo?')),
                ('conditionMenus', models.ManyToManyField(blank=True, help_text='Si no eliges ninguno usa los mismos que afecta el descuento', related_name='_offer_conditionMenus_+', to='SV.Menu', verbose_name='Menus que generan el descuento')),
                ('conditionProducts', models.ManyToManyField(blank=True, help_text='Si no eliges ninguno usa los mismos que afecta el descuento', related_name='_offer_conditionProducts_+', to='SV.Product', verbose_name='Productos que generan el descuento')),
                ('discountMenus', models.ManyToManyField(blank=True, related_name='_offer_discountMenus_+', to='SV.Menu', verbose_name='Menus a los que afecta el descuento')),
                ('discountProducts', models.ManyToManyField(blank=True, related_name='_offer_discountProducts_+', to='SV.Product', verbose_name='Productos a los que afecta el descuento')),
                ('organization', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='+', to='mirari.Organization')),
                ('sellpoints', models.ManyToManyField(blank=True, help_text='Si no eliges ninguno afecta a todas', related_name='_offer_sellpoints_+', to='SV.Sellpoint', verbose_name='Puntos de venta que afect')),
            ],
            options={
                'verbose_name': 'Descuento',
                'verbose_name_plural': 'Descuentos',
                'ordering': ['-id'],
                'permissions': [('Can_View__Offer', 'Ve descuentos'), ('Can_Create__Offer', 'Crea descuentos'), ('Can_Update__Offer', 'Modifica descuentos'), ('Can_Delete__Offer', 'Elimina descuentos')],
                'abstract': False,
                'default_permissions': [],
            },
        ),
        migrations.RemoveField(
            model_name='offers',
            name='conditionMenus',
        ),
        migrations.RemoveField(
            model_name='offers',
            name='conditionProducts',
        ),
        migrations.RemoveField(
            model_name='offers',
            name='discountMenus',
        ),
        migrations.RemoveField(
            model_name='offers',
            name='discountProducts',
        ),
        migrations.RemoveField(
            model_name='offers',
            name='organization',
        ),
        migrations.RemoveField(
            model_name='offers',
            name='sellpoints',
        ),
        migrations.DeleteModel(
            name='Offers',
        ),
        migrations.AddField(
            model_name='ticketproducts',
            name='offers',
            field=models.ManyToManyField(blank=True, related_name='_ticketproducts_offers_+', to='SV.Offer'),
        ),
    ]
