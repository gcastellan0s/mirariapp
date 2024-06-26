# Generated by Django 2.0.5 on 2020-02-26 19:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TCS', '0051_merge_20200210_1930'),
    ]

    operations = [
        migrations.CreateModel(
            name='OrderServiceReport',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('active', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name': 'Reporte de Orden',
                'permissions': [],
                'default_permissions': [],
                'verbose_name_plural': 'Reportes de Ordenes',
                'abstract': False,
                'ordering': ['-id'],
            },
        ),
    ]
