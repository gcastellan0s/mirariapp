# Generated by Django 2.0.5 on 2019-07-04 18:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mirari', '0031_organization_color'),
        ('TCS', '0037_auto_20190704_1316'),
    ]

    operations = [
        migrations.CreateModel(
            name='OrderServiceInformation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('active', models.BooleanField(default=True)),
                ('organization', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='+', to='mirari.Organization')),
            ],
            options={
                'verbose_name': 'Informacion de Orden',
                'verbose_name_plural': 'Informacion de Orden',
                'ordering': ['-id'],
                'permissions': [('Can_View__Modelo', 'Ve informacion de orden'), ('Can_Update__Modelo', 'Modifica informacion de orden')],
                'abstract': False,
                'default_permissions': [],
            },
        ),
    ]