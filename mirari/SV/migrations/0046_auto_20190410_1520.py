# Generated by Django 2.0.5 on 2019-04-10 20:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('SV', '0045_client_code'),
    ]

    operations = [
        migrations.RenameField(
            model_name='client',
            old_name='code',
            new_name='uid',
        ),
    ]