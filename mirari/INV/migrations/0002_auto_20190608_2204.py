# Generated by Django 2.0.5 on 2019-06-09 03:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('INV', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='fiscalmx',
            old_name='nocer',
            new_name='noCer',
        ),
    ]