# Generated by Django 2.0.5 on 2019-03-11 20:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TCS', '0033_orderservice_comments'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderservicecomment',
            name='id_bckp',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='orderservicecomment',
            name='creation_date',
            field=models.DateTimeField(),
        ),
    ]
