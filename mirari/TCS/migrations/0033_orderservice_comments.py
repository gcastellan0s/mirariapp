# Generated by Django 2.0.5 on 2019-03-11 19:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TCS', '0032_auto_20190308_1454'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderservice',
            name='comments',
            field=models.TextField(blank=True, verbose_name='Comentarios'),
        ),
    ]
