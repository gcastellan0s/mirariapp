# Generated by Django 2.0.5 on 2019-03-25 21:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mirari', '0027_auto_20190319_1636'),
        ('SV', '0023_auto_20190325_1517'),
    ]

    operations = [
        migrations.AddField(
            model_name='client',
            name='organization',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='mirari.Organization'),
            preserve_default=False,
        ),
    ]
