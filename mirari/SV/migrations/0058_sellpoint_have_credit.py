# Generated by Django 2.0.5 on 2019-05-21 20:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SV', '0057_auto_20190521_1549'),
    ]

    operations = [
        migrations.AddField(
            model_name='sellpoint',
            name='have_credit',
            field=models.BooleanField(default=False, help_text='Tiene credito', verbose_name='Tiene credito?'),
        ),
    ]
