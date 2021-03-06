# Generated by Django 2.0.5 on 2018-09-27 17:47

from django.db import migrations, models
import django.db.models.deletion
import mirari.INT.models


class Migration(migrations.Migration):

    dependencies = [
        ('mirari', '0002_auto_20180918_1515'),
        ('INT', '0002_team'),
    ]

    operations = [
        migrations.CreateModel(
            name='Handbook',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('active', models.BooleanField(default=True)),
                ('file', models.FileField(upload_to=mirari.INT.models.path_Handbook_file, verbose_name='Archivo')),
                ('notes', models.TextField(blank=True, null=True, verbose_name='Notas')),
                ('creation_date', models.DateTimeField(auto_now_add=True)),
                ('organization', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='mirari.Organization')),
            ],
            options={
                'verbose_name': 'Manual',
                'verbose_name_plural': 'Manuales',
                'ordering': ['-id'],
                'permissions': [('Can_View__Handbook', 'Ve manuales'), ('Can_Create__Handbook', 'Crea manuales'), ('Can_Update__Handbook', 'Modifica manuales'), ('Can_Delete__Handbook', 'Elimina manuales')],
                'abstract': False,
                'default_permissions': [],
            },
        ),
    ]
