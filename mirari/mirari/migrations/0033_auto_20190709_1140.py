# Generated by Django 2.0.5 on 2019-07-09 16:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mirari', '0032_user_needchangepassword'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.EmailField(blank=True, max_length=254, null=True, verbose_name='email address'),
        ),
    ]
