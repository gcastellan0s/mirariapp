# Generated by Django 2.0.5 on 2019-04-06 17:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SV', '0032_auto_20190327_1905'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='client',
            name='haveCredit',
        ),
        migrations.RemoveField(
            model_name='client',
            name='haveReturn',
        ),
        migrations.AddField(
            model_name='offer',
            name='clients',
            field=models.ManyToManyField(blank=True, related_name='_offer_clients_+', to='SV.Client', verbose_name='Clientes a los que aplica'),
        ),
    ]
