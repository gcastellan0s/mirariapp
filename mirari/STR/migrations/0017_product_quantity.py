# Generated by Django 2.0.5 on 2020-03-23 06:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('STR', '0016_product_location'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='quantity',
            field=models.IntegerField(default=0, verbose_name='Cantidad'),
        ),
    ]
