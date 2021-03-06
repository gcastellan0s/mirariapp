# Generated by Django 2.0.5 on 2019-03-26 06:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CRYE', '0018_auto_20190326_0006'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tablaamortizacion',
            name='balanceInsoluto',
        ),
        migrations.RemoveField(
            model_name='tablaamortizacion',
            name='estatus',
        ),
        migrations.RemoveField(
            model_name='tablaamortizacion',
            name='pagado',
        ),
        migrations.RemoveField(
            model_name='tablaamortizacion',
            name='renta',
        ),
        migrations.AddField(
            model_name='tablaamortizacion',
            name='activo',
            field=models.CharField(blank=True, max_length=15, null=True, verbose_name='Activo'),
        ),
        migrations.AddField(
            model_name='tablaamortizacion',
            name='dias_periodo',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='tablaamortizacion',
            name='id_amortizacion',
            field=models.CharField(blank=True, max_length=250, null=True, verbose_name='ID amortizacion'),
        ),
        migrations.AddField(
            model_name='tablaamortizacion',
            name='iva_capital',
            field=models.FloatField(default=0, verbose_name='Iva Capital'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='tablaamortizacion',
            name='iva_interes',
            field=models.FloatField(default=0, verbose_name='Iva Interes'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='tablaamortizacion',
            name='pago',
            field=models.CharField(blank=True, max_length=15, null=True, verbose_name='Pago'),
        ),
        migrations.AddField(
            model_name='tablaamortizacion',
            name='renta_mensual',
            field=models.FloatField(default=0, verbose_name='Renta Mensual'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='tablaamortizacion',
            name='renta_total',
            field=models.FloatField(default=0, verbose_name='Renta Total'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='tablaamortizacion',
            name='saldo_insoluto',
            field=models.FloatField(default=0, verbose_name='Saldo Insoluto'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='walletcredit',
            name='id_tabla',
            field=models.CharField(blank=True, max_length=250, null=True, verbose_name='id_tabla'),
        ),
        migrations.AlterField(
            model_name='walletcredit',
            name='walletcredit_tipo',
            field=models.CharField(choices=[('CREDITO', 'CREDITO'), ('ARRENDAMIENTO', 'ARRENDAMIENTO')], default='CREDITO', max_length=250, verbose_name='Obligación'),
        ),
    ]
