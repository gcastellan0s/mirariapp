# Generated by Django 2.0.5 on 2019-04-07 19:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CRYE', '0030_auto_20190406_1546'),
    ]

    operations = [
        migrations.AlterField(
            model_name='walletcredit',
            name='walletcredit_tipo',
            field=models.CharField(choices=[('CREDITO', 'CREDITO'), ('ARRENDAMIENTO', 'ARRENDAMIENTO')], default='CREDITO', max_length=250, verbose_name='Tipo de cartera'),
        ),
    ]