# Generated by Django 2.0.5 on 2018-12-03 18:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Actor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('active', models.BooleanField(default=True)),
                ('name', models.CharField(max_length=255)),
            ],
            options={
                'verbose_name': 'Actor',
                'verbose_name_plural': 'Actores',
                'ordering': ['-id'],
                'permissions': [('Can_View__Actor', 'Ve actores'), ('Can_Create__Actor', 'Crea actores'), ('Can_Update__Actor', 'Modifica actores'), ('Can_Delete__Actor', 'Elimina actores')],
                'abstract': False,
                'default_permissions': [],
            },
        ),
        migrations.CreateModel(
            name='Credit',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('active', models.BooleanField(default=True)),
                ('name', models.CharField(max_length=255)),
            ],
            options={
                'verbose_name': 'Credito',
                'verbose_name_plural': 'Credito',
                'ordering': ['-id'],
                'permissions': [('Can_View__Credit', 'Ve credito'), ('Can_Create__Credit', 'Crea credito'), ('Can_Update__Credit', 'Modifica credito'), ('Can_Delete__Credit', 'Elimina credito')],
                'abstract': False,
                'default_permissions': [],
            },
        ),
    ]
