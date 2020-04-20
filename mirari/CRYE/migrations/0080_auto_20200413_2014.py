# Generated by Django 2.0.5 on 2020-04-14 01:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CRYE', '0079_auto_20200323_0003'),
    ]

    operations = [
        migrations.AlterField(
            model_name='walletcredit',
            name='walletcredit_tipo',
            field=models.CharField(choices=[('ARRENDAMIENTO', 'ARRENDAMIENTO'), ('CREDITO', 'CREDITO')], default='CREDITO', max_length=250, verbose_name='Tipo de cartera'),
        ),
    ]
