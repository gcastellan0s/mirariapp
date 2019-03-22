# Generated by Django 2.0.5 on 2019-03-22 21:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CRYE', '0013_pagoamortizacion'),
    ]

    operations = [
        migrations.AddField(
            model_name='walletcredit',
            name='walletcredit_tipo',
            field=models.CharField(choices=[('ARRENDAMIENTO', 'ARRENDAMIENTO'), ('CREDITO', 'CREDITO')], default='CREDITO', max_length=250, verbose_name='Obligación'),
        ),
    ]
