# Generated by Django 2.0.5 on 2019-04-06 21:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('SV', '0038_auto_20190406_1415'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ticket',
            name='isOrder',
        ),
    ]
