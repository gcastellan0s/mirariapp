# Generated by Django 2.0.5 on 2018-10-01 18:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('INT', '0014_auto_20181001_1127'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notification',
            name='channel',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='+', to='INT.Channel', verbose_name='Canal(es) por donde envias'),
        ),
    ]
