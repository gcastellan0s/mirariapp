# Generated by Django 2.0.5 on 2019-01-04 17:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TCS', '0008_auto_20181203_1228'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='brand',
            name='organization',
        ),
        migrations.RemoveField(
            model_name='brand',
            name='store',
        ),
        migrations.RemoveField(
            model_name='modelo',
            name='organization',
        ),
        migrations.RemoveField(
            model_name='store',
            name='organization',
        ),
        migrations.AddField(
            model_name='brand',
            name='company',
            field=models.ManyToManyField(to='TCS.Company', verbose_name='Empresas que la venden'),
        ),
    ]
