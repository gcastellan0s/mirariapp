# Generated by Django 2.0.5 on 2018-10-09 18:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mirari', '0005_hostemail'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='hostemail',
            name='app',
        ),
        migrations.RemoveField(
            model_name='hostemail',
            name='name',
        ),
        migrations.AddField(
            model_name='hostemail',
            name='module',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='mirari.Module'),
            preserve_default=False,
        ),
    ]
