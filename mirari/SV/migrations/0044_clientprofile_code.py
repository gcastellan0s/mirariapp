# Generated by Django 2.0.5 on 2019-04-10 17:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SV', '0043_auto_20190408_1501'),
    ]

    operations = [
        migrations.AddField(
            model_name='clientprofile',
            name='code',
            field=models.CharField(default='Publico General', max_length=250, verbose_name='Código del perfil'),
            preserve_default=False,
        ),
    ]