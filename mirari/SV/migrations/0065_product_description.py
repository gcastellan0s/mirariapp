# Generated by Django 2.0.5 on 2019-05-27 20:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SV', '0064_auto_20190521_1606'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='description',
            field=models.CharField(blank=True, max_length=250, null=True, verbose_name='Muy breve descripción'),
        ),
    ]
