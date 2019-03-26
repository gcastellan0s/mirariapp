# Generated by Django 2.0.5 on 2019-03-25 20:58

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('SV', '0020_auto_20190321_1210'),
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('active', models.BooleanField(default=True)),
                ('name', models.CharField(max_length=250, verbose_name='Nombre del descuento')),
                ('contacto', models.CharField(blank=True, help_text='Correo o teléfono de contacto', max_length=255, null=True, verbose_name='Correo o teléfono de contacto')),
                ('sellpoint', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='SV.Sellpoint')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL, verbose_name='')),
            ],
            options={
                'verbose_name': 'Cliente',
                'verbose_name_plural': 'Clientes',
                'ordering': ['-id'],
                'permissions': [('Can_View__Client', 'Ve clientes'), ('Can_Create__Client', 'Crea clientes'), ('Can_Update__Client', 'Modifica clientes'), ('Can_Delete__Client', 'Elimina clientes')],
                'abstract': False,
                'default_permissions': [],
            },
        ),
    ]