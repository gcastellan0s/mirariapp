# Generated by Django 2.0.5 on 2018-10-02 21:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mirari', '0002_auto_20180918_1515'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='extention',
        ),
        migrations.RemoveField(
            model_name='user',
            name='origin',
        ),
    ]
