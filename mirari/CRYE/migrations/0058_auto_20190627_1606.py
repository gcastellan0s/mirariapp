# Generated by Django 2.0.5 on 2019-06-27 21:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CRYE', '0057_auto_20190626_1610'),
    ]

    operations = [
        migrations.AlterField(
            model_name='walletcredit',
            name='walletcredit_tipo',
            field=models.CharField(choices=[('ARRENDAMIENTO', 'ARRENDAMIENTO'), ('CREDITO', 'CREDITO')], default='CREDITO', max_length=250, verbose_name='Tipo de cartera'),
        ),
    ]
