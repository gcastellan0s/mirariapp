# Generated by Django 2.0.5 on 2019-05-13 22:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CRYE', '0040_auto_20190508_1938'),
    ]

    operations = [
        migrations.AlterField(
            model_name='walletcredit',
            name='walletcredit_tipo',
            field=models.CharField(choices=[('CREDITO', 'CREDITO'), ('ARRENDAMIENTO', 'ARRENDAMIENTO')], default='CREDITO', max_length=250, verbose_name='Tipo de cartera'),
        ),
    ]
