# Generated by Django 2.0.5 on 2018-09-27 20:45

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('mirari', '0002_auto_20180918_1515'),
        ('INT', '0006_notification'),
    ]

    operations = [
        migrations.CreateModel(
            name='Channel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('active', models.BooleanField(default=True)),
                ('name', models.CharField(max_length=250, verbose_name='Nombre del canal')),
                ('mail', models.BooleanField(default=True, help_text='Se envia el contenido via mail a los destinatarios', verbose_name='Se envia por mail?')),
                ('mandatory', models.BooleanField(default=True, help_text='Es obligatorio leerlo y se envian notificaciones constantes', verbose_name='Obligatorio?')),
                ('notify_team', models.ManyToManyField(blank=True, help_text='Si el campo anterior y este estan vacios, se notificara a todos los equipos.', related_name='_channel_notify_team_+', to='INT.Team', verbose_name='Destinado a equipos')),
                ('notify_user', models.ManyToManyField(blank=True, related_name='_channel_notify_user_+', to=settings.AUTH_USER_MODEL, verbose_name='Destinado a usuarios')),
                ('organization', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='+', to='mirari.Organization')),
                ('team_admin', models.ManyToManyField(blank=True, related_name='_channel_team_admin_+', to='INT.Team', verbose_name='Lo administran equipos')),
                ('user_admin', models.ManyToManyField(blank=True, related_name='_channel_user_admin_+', to=settings.AUTH_USER_MODEL, verbose_name='Lo administran usuarios')),
            ],
            options={
                'verbose_name': 'Canales',
                'verbose_name_plural': 'Canal de comunicación',
                'ordering': ['-id'],
                'permissions': [('Can_View__Chanel', 'Ve canal de comunicación'), ('Can_Create__Chanel', 'Crea canal de comunicación'), ('Can_Update__Chanel', 'Modifica canal de comunicación'), ('Can_Delete__Chanel', 'Elimina canal de comunicación')],
                'abstract': False,
                'default_permissions': [],
            },
        ),
        migrations.RemoveField(
            model_name='chanel',
            name='notify_team',
        ),
        migrations.RemoveField(
            model_name='chanel',
            name='notify_user',
        ),
        migrations.RemoveField(
            model_name='chanel',
            name='organization',
        ),
        migrations.RemoveField(
            model_name='chanel',
            name='team_admin',
        ),
        migrations.RemoveField(
            model_name='chanel',
            name='user_admin',
        ),
        migrations.DeleteModel(
            name='Chanel',
        ),
        migrations.AddField(
            model_name='notification',
            name='channel',
            field=models.ManyToManyField(related_name='_notification_channel_+', to='INT.Channel'),
        ),
    ]
