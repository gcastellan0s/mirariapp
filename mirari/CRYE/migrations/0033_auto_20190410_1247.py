# Generated by Django 2.0.5 on 2019-04-10 17:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CRYE', '0032_auto_20190408_1226'),
    ]

    operations = [
        migrations.AlterField(
            model_name='walletcredit',
            name='walletcredit_tipo',
            field=models.CharField(choices=[('CREDITO', 'CREDITO'), ('ARRENDAMIENTO', 'ARRENDAMIENTO')], default='CREDITO', max_length=250, verbose_name='Tipo de cartera'),
        ),
    ]