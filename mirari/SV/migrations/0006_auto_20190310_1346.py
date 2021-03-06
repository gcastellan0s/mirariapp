# Generated by Django 2.0.5 on 2019-03-10 19:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SV', '0005_auto_20190305_0116'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cut',
            name='user',
        ),
        migrations.AlterField(
            model_name='cut',
            name='serial',
            field=models.IntegerField(default=1),
        ),
        migrations.AlterField(
            model_name='ticketproducts',
            name='alias',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
        migrations.AlterField(
            model_name='ticketproducts',
            name='ieps',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='ticketproducts',
            name='iva',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='ticketproducts',
            name='price',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='ticketproducts',
            name='productName',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
        migrations.AlterField(
            model_name='ticketproducts',
            name='quantity',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='ticketproducts',
            name='total',
            field=models.FloatField(default=0),
        ),
    ]
