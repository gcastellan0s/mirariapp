# Generated by Django 2.0.5 on 2019-02-26 20:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TCS', '0018_auto_20190226_1359'),
    ]

    operations = [
        migrations.AddField(
            model_name='store',
            name='adress',
            field=models.CharField(blank=True, max_length=250, null=True, verbose_name='Domicilio'),
        ),
        migrations.AddField(
            model_name='store',
            name='phone',
            field=models.CharField(blank=True, max_length=250, null=True, verbose_name='Teléfono'),
        ),
        migrations.AddField(
            model_name='store',
            name='state',
            field=models.CharField(blank=True, max_length=250, null=True, verbose_name='Estado'),
        ),
    ]