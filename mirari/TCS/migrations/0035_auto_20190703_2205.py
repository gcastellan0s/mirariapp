# Generated by Django 2.0.5 on 2019-07-04 03:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TCS', '0034_auto_20190311_1412'),
    ]

    operations = [
        migrations.AlterField(
            model_name='brand',
            name='id_bckp',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='company',
            name='id_bckp',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='modelo',
            name='id_bckp',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='orderservice',
            name='id_bckp',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='orderservicecomment',
            name='creation_date',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='orderservicecomment',
            name='id_bckp',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='store',
            name='id_bckp',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]