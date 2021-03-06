# Generated by Django 2.0.5 on 2018-12-03 18:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('TCS', '0007_auto_20181121_0210'),
    ]

    operations = [
        migrations.AlterField(
            model_name='modelo',
            name='brand',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='TCS.Brand', verbose_name='Marca'),
        ),
        migrations.AlterField(
            model_name='modelo',
            name='name',
            field=models.CharField(max_length=250, verbose_name='Nombre del modelo'),
        ),
        migrations.AlterField(
            model_name='store',
            name='company',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='TCS.Company', verbose_name='Compañia'),
            preserve_default=False,
        ),
    ]
