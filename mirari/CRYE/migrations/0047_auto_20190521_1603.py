# Generated by Django 2.0.5 on 2019-05-21 21:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CRYE', '0046_auto_20190521_1559'),
    ]

    operations = [
        migrations.AlterField(
            model_name='walletcredit',
            name='walletcredit_tipo',
            field=models.CharField(choices=[('CREDITO', 'CREDITO'), ('ARRENDAMIENTO', 'ARRENDAMIENTO')], default='CREDITO', max_length=250, verbose_name='Tipo de cartera'),
        ),
    ]