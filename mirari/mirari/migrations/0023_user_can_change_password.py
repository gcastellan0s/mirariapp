# Generated by Django 2.0.5 on 2019-02-28 17:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mirari', '0022_remove_profile_visible_name2'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='can_change_password',
            field=models.BooleanField(default=True, help_text='Un usuario puede cambiar su propio passwrod desde su cuenta?', verbose_name='Puede cambiar su contraseña?'),
        ),
    ]
