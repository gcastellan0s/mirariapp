# Generated by Django 2.0.5 on 2018-12-10 23:06

from django.db import migrations, models
import django.db.models.deletion
import localflavor.mx.models


class Migration(migrations.Migration):

    dependencies = [
        ('mirari', '0013_auto_20181207_1502'),
        ('SIEBEL', '0003_auto_20181207_1549'),
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('active', models.BooleanField(default=True)),
                ('name', models.CharField(blank=True, max_length=255, null=True, verbose_name='Nombre')),
                ('legal_representative', models.CharField(blank=True, max_length=255, null=True, verbose_name='Nombre del representante legal de la empresa')),
                ('contact_representative', models.CharField(blank=True, max_length=255, null=True, verbose_name='Nombre del contacto en la empresa')),
                ('rfc', localflavor.mx.models.MXRFCField(blank=True, max_length=13, null=True, verbose_name='RFC')),
                ('type_company', models.CharField(blank=True, choices=[('Sector público de pasajeros', 'Sector público de pasajeros'), ('Turismo', 'Turismo'), ('Transporte de personal', 'Transporte de personal'), ('Servicio Público Federal', 'Servicio Público Federal'), ('Agropecuario', 'Agropecuario'), ('Materiales y residuos peligrosos', 'Materiales y residuos peligrosos'), ('Forestal', 'Forestal'), ('Pesquero', 'Pesquero'), ('Agricola', 'Agricola')], max_length=255, null=True, verbose_name='Tipo de empresa')),
                ('business_activity', models.CharField(blank=True, choices=[('Agricultura', 'Agricultura'), ('Cultivo de alpiste', 'Cultivo de alpiste'), ('Construccion de inmuebles', 'Construccion de inmuebles'), ('Cultivo de arroz', 'Cultivo de arroz'), ('Cultivo de avena', 'Cultivo de avena'), ('Cultivo de cebada', 'Cultivo de cebada'), ('Fabricación de guantes', 'Fabricación de guantes'), ('Distribucion de otros productos', 'Distribucion de otros productos'), ('Agencia aduanal', 'Agencia aduanal'), ('Cultivo de aguacate', 'Cultivo de aguacate'), ('Fabricación otros art de metal', 'Fabricación otros art de metal'), ('Construcción no residencial', 'Construcción no residencial'), ('Fabricacion de uniformes', 'Fabricacion de uniformes')], max_length=255, null=True, verbose_name='Actividad empresarial')),
                ('contact1', models.CharField(blank=True, max_length=255, null=True, verbose_name='Contacto')),
                ('contact2', models.CharField(blank=True, max_length=255, null=True, verbose_name='Contacto')),
                ('contact3', models.CharField(blank=True, max_length=255, null=True, verbose_name='Contacto')),
                ('email', models.CharField(blank=True, max_length=255, null=True, verbose_name='Email')),
                ('address', models.CharField(blank=True, max_length=255, null=True, verbose_name='Dirección')),
                ('organization', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='mirari.Organization')),
                ('parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='SIEBEL.Company', verbose_name='Depende de:')),
            ],
            options={
                'verbose_name': 'Empresa',
                'verbose_name_plural': 'Empresas',
                'ordering': ['-id'],
                'permissions': [('Can_View__Company', 'Ve empresas'), ('Can_Create__Company', 'Crea empresas'), ('Can_Update__Company', 'Modifica empresas'), ('Can_Delete__Company', 'Elimina empresas')],
                'abstract': False,
                'default_permissions': [],
            },
        ),
        migrations.CreateModel(
            name='SBCredit',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('active', models.BooleanField(default=True)),
                ('stage', models.CharField(editable=False, max_length=255, verbose_name='Etapa del crédito')),
            ],
            options={
                'verbose_name': 'Credito',
                'verbose_name_plural': 'Creditos',
                'ordering': ['-id'],
                'permissions': [('Can_View__SBCredit', 'Ve creditos'), ('Can_Create__SBCredit', 'Crea creditos'), ('Can_Update__SBCredit', 'Modifica creditos'), ('Can_Delete__SBCredit', 'Elimina creditos')],
                'abstract': False,
                'default_permissions': [],
            },
        ),
        migrations.RemoveField(
            model_name='siebelcredit',
            name='creditType',
        ),
        migrations.RemoveField(
            model_name='siebelcredit',
            name='organization',
        ),
        migrations.AlterModelOptions(
            name='credittype',
            options={'default_permissions': [], 'ordering': ['-id'], 'permissions': [('Can_View__CreditType', 'Ve tipos de credito'), ('Can_Create__CreditType', 'Crea tipos de credito'), ('Can_Update__CreditType', 'Modifica tipos de credito'), ('Can_Delete__CreditType', 'Elimina tipos de credito')], 'verbose_name': 'Tipo de credito', 'verbose_name_plural': 'Tipos de credito'},
        ),
        migrations.AddField(
            model_name='person',
            name='birthday',
            field=models.DateField(blank=True, null=True, verbose_name='Fecha nacimiento'),
        ),
        migrations.AddField(
            model_name='person',
            name='business_activity',
            field=models.CharField(blank=True, choices=[('Persona física', 'Persona física'), ('Persona física con actividad empresarial', 'Persona física con actividad empresarial')], max_length=255, null=True, verbose_name='Actividad empresarial'),
        ),
        migrations.AddField(
            model_name='person',
            name='civil_status',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Estado civil'),
        ),
        migrations.AddField(
            model_name='person',
            name='contact1',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Contacto'),
        ),
        migrations.AddField(
            model_name='person',
            name='contact2',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Contacto'),
        ),
        migrations.AddField(
            model_name='person',
            name='contact3',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Contacto'),
        ),
        migrations.AddField(
            model_name='person',
            name='curp',
            field=localflavor.mx.models.MXCURPField(blank=True, max_length=18, null=True, verbose_name='CURP'),
        ),
        migrations.AddField(
            model_name='person',
            name='email',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Contacto'),
        ),
        migrations.AddField(
            model_name='person',
            name='gender',
            field=models.CharField(blank=True, choices=[('Hombre', 'Hombre'), ('Mujer', 'Mujer'), ('Otro', 'Otro')], max_length=255, null=True, verbose_name='Género'),
        ),
        migrations.AddField(
            model_name='person',
            name='mothers_last_name',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Apellido Materno'),
        ),
        migrations.AddField(
            model_name='person',
            name='occupation',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Ocupación'),
        ),
        migrations.AddField(
            model_name='person',
            name='rfc',
            field=localflavor.mx.models.MXRFCField(blank=True, max_length=13, null=True, verbose_name='RFC'),
        ),
        migrations.AlterField(
            model_name='creditactor',
            name='credit',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='+', to='SIEBEL.SBCredit'),
        ),
        migrations.AlterField(
            model_name='creditactor',
            name='person',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='+', to='SIEBEL.Person'),
        ),
        migrations.AlterField(
            model_name='person',
            name='first_name',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Nombre(s)'),
        ),
        migrations.AlterField(
            model_name='person',
            name='last_name',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Apellido Paterno'),
        ),
        migrations.DeleteModel(
            name='SIEBELCredit',
        ),
        migrations.AddField(
            model_name='sbcredit',
            name='creditType',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='+', to='SIEBEL.CreditType', verbose_name='Tipo de crédito'),
        ),
        migrations.AddField(
            model_name='sbcredit',
            name='organization',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='mirari.Organization'),
        ),
        migrations.AddField(
            model_name='creditactor',
            name='company',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='+', to='SIEBEL.Company'),
        ),
    ]
