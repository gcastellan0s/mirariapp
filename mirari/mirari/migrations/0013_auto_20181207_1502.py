# Generated by Django 2.0.5 on 2018-12-07 21:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mirari', '0012_remove_user_first_login'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='visible_username',
            field=models.CharField(help_text='Obligatorio. Longitud máxima 30 caracteres alfanuméricos (letras, dígitos y @/./+/-/_) solamente.', max_length=50, verbose_name='Nombre de usuario'),
        ),
    ]
