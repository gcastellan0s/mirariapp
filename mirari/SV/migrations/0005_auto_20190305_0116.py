# Generated by Django 2.0.5 on 2019-03-05 07:17

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('SV', '0004_auto_20180918_1445'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cut',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('initial_time', models.DateTimeField(auto_now_add=True)),
                ('final_time', models.DateTimeField(blank=True, null=True)),
                ('ras', models.PositiveIntegerField(default=100)),
                ('serial', models.IntegerField(blank=True, default=1, null=True)),
                ('show', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name': 'Corte',
                'verbose_name_plural': 'Cortes',
                'ordering': ['-id'],
                'permissions': [('Can_View__Cut', 'Ve cortes'), ('Can_Create__Cut', 'Crea cortes'), ('Can_Update__Cut', 'Modifica cortes'), ('Can_Delete__Cut', 'Elimina cortes')],
                'abstract': False,
                'default_permissions': [],
            },
        ),
        migrations.CreateModel(
            name='Ticket',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('barcode', models.CharField(default='0000000000000', max_length=13)),
                ('key', models.CharField(max_length=12)),
                ('username', models.CharField(blank=True, max_length=250, null=True)),
                ('status', models.CharField(choices=[('COBRADO', 'COBRADO'), ('PENDIENTE', 'PENDIENTE')], default='PENDIENTE', max_length=50)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('format_time', models.CharField(blank=True, max_length=50, null=True)),
                ('format_date', models.CharField(blank=True, max_length=50, null=True)),
                ('total', models.FloatField(default=0)),
                ('iva', models.FloatField(default=0)),
                ('ieps', models.FloatField(default=0)),
                ('cut', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='SV.Cut')),
            ],
            options={
                'verbose_name': 'Ticket',
                'verbose_name_plural': 'Tickets',
                'ordering': ['-id'],
                'permissions': [('Can_View__Ticket', 'Ve tickets'), ('Can_Create__Ticket', 'Crea tickets'), ('Can_Update__Ticket', 'Modifica tickets'), ('Can_Delete__Ticket', 'Elimina tickets')],
                'abstract': False,
                'default_permissions': [],
            },
        ),
        migrations.CreateModel(
            name='TicketProducts',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('productName', models.CharField(max_length=250)),
                ('alias', models.CharField(max_length=250)),
                ('quantity', models.FloatField()),
                ('price', models.FloatField()),
                ('total', models.FloatField()),
                ('iva', models.FloatField()),
                ('ieps', models.FloatField()),
                ('product', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='SV.ProductAttributes')),
                ('ticket', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='SV.Ticket')),
            ],
            options={
                'verbose_name': 'Producto del ticket',
                'verbose_name_plural': 'Productos del ticket',
                'ordering': ['-id'],
                'permissions': [('Can_View__TicketProducts', 'Ve productos del ticket'), ('Can_Create__TicketProducts', 'Crea productos del ticket'), ('Can_Update__TicketProducts', 'Modifica productos del ticket'), ('Can_Delete__TicketProducts', 'Elimina productos del ticket')],
                'abstract': False,
                'default_permissions': [],
            },
        ),
        migrations.AddField(
            model_name='sellpoint',
            name='orders',
            field=models.ManyToManyField(blank=True, related_name='_sellpoint_orders_+', to=settings.AUTH_USER_MODEL, verbose_name='Pedidos'),
        ),
        migrations.AddField(
            model_name='ticket',
            name='sellpoint',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='SV.Sellpoint'),
        ),
        migrations.AddField(
            model_name='ticket',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='cut',
            name='sellpoint',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='SV.Sellpoint'),
        ),
        migrations.AddField(
            model_name='cut',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
    ]