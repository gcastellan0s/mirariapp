# Generated by Django 2.0.5 on 2019-04-25 03:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SV', '0050_auto_20190424_1315'),
    ]

    operations = [
        migrations.AddField(
            model_name='ticketproducts',
            name='offerprice',
            field=models.FloatField(default=0),
        ),
    ]