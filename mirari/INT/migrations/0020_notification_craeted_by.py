# Generated by Django 2.0.5 on 2018-10-03 21:48

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('INT', '0019_auto_20181003_1221'),
    ]

    operations = [
        migrations.AddField(
            model_name='notification',
            name='craeted_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL, verbose_name='Canal(es) por donde envias'),
        ),
    ]
