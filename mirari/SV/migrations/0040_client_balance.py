# Generated by Django 2.0.5 on 2019-04-07 19:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SV', '0039_remove_ticket_isorder'),
    ]

    operations = [
        migrations.AddField(
            model_name='client',
            name='balance',
            field=models.FloatField(blank=True, default=0, null=True),
        ),
    ]
