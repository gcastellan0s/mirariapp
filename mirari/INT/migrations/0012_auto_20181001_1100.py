# Generated by Django 2.0.5 on 2018-10-01 16:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('INT', '0011_auto_20180928_1528'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='channel',
            name='mail',
        ),
        migrations.AddField(
            model_name='channel',
            name='send_mail',
            field=models.BooleanField(default=True, help_text='Se notifica via mail a los destinatarios?', verbose_name='Se notifica por mail?'),
        ),
    ]
