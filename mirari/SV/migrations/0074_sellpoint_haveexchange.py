# Generated by Django 2.0.5 on 2019-08-06 16:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SV', '0073_auto_20190727_1316'),
    ]

    operations = [
        migrations.AddField(
            model_name='sellpoint',
            name='haveExchange',
            field=models.BooleanField(default=True, help_text='Entrega cámbio?', verbose_name='Entrega cambio'),
        ),
    ]