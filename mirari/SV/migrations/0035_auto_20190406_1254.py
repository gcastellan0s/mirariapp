# Generated by Django 2.0.5 on 2019-04-06 18:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SV', '0034_auto_20190406_1202'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='email',
            field=models.CharField(blank=True, help_text='Email de contacto', max_length=255, null=True, verbose_name='Correo'),
        ),
    ]