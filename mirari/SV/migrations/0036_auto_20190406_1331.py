# Generated by Django 2.0.5 on 2019-04-06 19:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SV', '0035_auto_20190406_1254'),
    ]

    operations = [
        migrations.AddField(
            model_name='ticket',
            name='isOrder',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='ticket',
            name='payment',
            field=models.FloatField(default=0),
        ),
    ]