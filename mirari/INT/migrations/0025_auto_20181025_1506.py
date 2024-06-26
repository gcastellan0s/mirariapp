# Generated by Django 2.0.5 on 2018-10-25 20:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('INT', '0024_auto_20181025_1307'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='channel',
            name='mandatory',
        ),
        migrations.RemoveField(
            model_name='channel',
            name='send_mail',
        ),
        migrations.AlterField(
            model_name='notification',
            name='hide_content',
            field=models.BooleanField(default=True, help_text='Si ocultas el contenido el usuario deberá ingresar usuario y contraseña para ver el contenido.', verbose_name='Ocultar contenido?'),
        ),
    ]
