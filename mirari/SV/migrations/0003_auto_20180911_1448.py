# Generated by Django 2.0.5 on 2018-09-11 19:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SV', '0002_auto_20180910_1322'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employeeaccess',
            name='profiles',
            field=models.CharField(choices=[('casher', 'Cajero'), ('supervisor', 'Supervisor'), ('vendor', 'Vendedor')], max_length=30, verbose_name='Perfil'),
        ),
    ]
