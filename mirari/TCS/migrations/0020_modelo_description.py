# Generated by Django 2.0.5 on 2019-02-26 22:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TCS', '0019_auto_20190226_1428'),
    ]

    operations = [
        migrations.AddField(
            model_name='modelo',
            name='description',
            field=models.CharField(blank=True, max_length=250, null=True, verbose_name='Descripción'),
        ),
    ]
