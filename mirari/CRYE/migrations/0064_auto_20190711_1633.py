# Generated by Django 2.0.5 on 2019-07-11 21:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CRYE', '0063_auto_20190709_1715'),
    ]

    operations = [
        migrations.AlterField(
            model_name='walletcredit',
            name='walletcredit_tipo',
            field=models.CharField(choices=[('ARRENDAMIENTO', 'ARRENDAMIENTO'), ('CREDITO', 'CREDITO')], default='CREDITO', max_length=250, verbose_name='Tipo de cartera'),
        ),
    ]