# Generated by Django 2.0.5 on 2019-02-28 06:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TCS', '0024_auto_20190227_1701'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderservice',
            name='s',
            field=models.IntegerField(default=1, verbose_name='Folio de la orden'),
            preserve_default=False,
        ),
    ]
