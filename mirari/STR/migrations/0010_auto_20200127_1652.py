# Generated by Django 2.0.5 on 2020-01-27 22:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('STR', '0009_auto_20200127_1446'),
    ]

    operations = [
        migrations.AlterField(
            model_name='provider',
            name='contactEmail',
            field=models.CharField(blank=True, help_text='Correo donde llegarán las notificaciones de facturación', max_length=100, null=True, verbose_name='Email contacto'),
        ),
    ]
