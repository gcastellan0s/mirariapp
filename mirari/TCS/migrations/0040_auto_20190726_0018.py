# Generated by Django 2.0.5 on 2019-07-26 05:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('TCS', '0039_auto_20190704_1401'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderservice',
            name='brandName',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
        migrations.AlterField(
            model_name='orderservice',
            name='companyName',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
        migrations.AlterField(
            model_name='orderservice',
            name='modelo',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='TCS.Modelo', verbose_name='Modelo'),
        ),
        migrations.AlterField(
            model_name='orderservice',
            name='modeloName',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
        migrations.AlterField(
            model_name='orderservice',
            name='service',
            field=models.CharField(choices=[('Icon', 'Icon'), ('Tecnoservicio', 'Tecnoservicio'), ('Tc2', 'Tc2'), ('MexicoF', 'MexicoF')], default='Icon', max_length=250, verbose_name='Tipo de servicio'),
        ),
        migrations.AlterField(
            model_name='orderservice',
            name='storeName',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
    ]
