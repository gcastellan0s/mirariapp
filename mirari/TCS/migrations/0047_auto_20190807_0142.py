# Generated by Django 2.0.5 on 2019-08-07 06:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TCS', '0046_auto_20190807_0123'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderservicecomment',
            name='creation_date',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='orderserviceconcept',
            name='creation_date',
            field=models.DateTimeField(),
        ),
    ]
