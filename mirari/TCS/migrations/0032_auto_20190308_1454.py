# Generated by Django 2.0.5 on 2019-03-08 20:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TCS', '0031_auto_20190228_1417'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderservice',
            name='brandName',
            field=models.CharField(blank=True, max_length=250),
        ),
        migrations.AddField(
            model_name='orderservice',
            name='companyName',
            field=models.CharField(blank=True, max_length=250),
        ),
        migrations.AddField(
            model_name='orderservice',
            name='modeloName',
            field=models.CharField(blank=True, max_length=250),
        ),
        migrations.AddField(
            model_name='orderservice',
            name='storeName',
            field=models.CharField(blank=True, max_length=250),
        ),
    ]
