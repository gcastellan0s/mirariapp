# Generated by Django 2.0.5 on 2019-03-28 01:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SV', '0031_auto_20190327_1904'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ticket',
            name='haveCredit',
        ),
        migrations.RemoveField(
            model_name='ticket',
            name='haveReturn',
        ),
        migrations.AddField(
            model_name='client',
            name='haveCredit',
            field=models.BooleanField(default=True, verbose_name='Tiene crédito?'),
        ),
        migrations.AddField(
            model_name='client',
            name='haveReturn',
            field=models.BooleanField(default=True, verbose_name='Puede devolver='),
        ),
    ]
