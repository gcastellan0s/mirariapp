# Generated by Django 2.0.5 on 2019-08-06 04:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CRYE', '0067_auto_20190726_0147'),
    ]

    operations = [
        migrations.AlterField(
            model_name='walletcredit',
            name='walletcredit_tipo',
            field=models.CharField(choices=[('ARRENDAMIENTO', 'ARRENDAMIENTO'), ('CREDITO', 'CREDITO')], default='CREDITO', max_length=250, verbose_name='Tipo de cartera'),
        ),
    ]
