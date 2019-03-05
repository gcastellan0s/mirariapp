# -*- coding: utf-8 -*-
from mirari.mirari.models import *
from .vars import *



VARS = {
	'NAME':'Desbloqueo Siebel',
	'PLURAL':'Desbloqueo Siebel',
	'MODEL':'SiebelUnblock',
	'NEW':'NUEVO',
	'NEW_GENDER': 'un nuevo',
	'THIS': 'este',
	'APP':APP,
	'EXCLUDE_PERMISSIONS':['create','update','delete',],
}
class SiebelUnblock(Model_base):
	VARS = VARS
	class Meta(Model_base.Meta):
		verbose_name = VARS['NAME']
		verbose_name_plural = VARS['PLURAL']
		permissions = permissions(VARS)
	def __str__(self):
		return '{0}'.format(self.VARS['NAME'])



VARS = {
	'NAME':'Cartera',
	'PLURAL':'Carteras',
	'MODEL':'WalletCredit',
	'NEW':'NUEVA',
	'NEW_GENDER': 'una nueva',
	'THIS': 'esta',
	'APP':APP,
	'LIST': [
			{
				'field': 'obligacion',
				'title': 'Obligación',
				'width': 100,
				'url': 'property_url_update',
			},
			{
				'field': 'nombre',
				'title': 'Nombre',
				'width': 300,
				'url': 'property_url_update',
			},
			{
				'field': 'rfc',
				'title': 'RFC',
			},
			{
				'field': 'plazo',
				'title': 'property_get_Plazo',
			},
			{
				'field': 'monto',
				'title': 'property_get_Monto',
			},
		],
	'SEARCH': ['nombre','rfc','obligacion'],
	'SORTEABLE': ['nombre','fecha_otorgado','fecha_vencimiento'],
	'FORM': [
		Div(
			Div('numero', css_class="col-md-3"),
			Div('nombre', css_class="col-md-9"),
			
			css_class="form-group m-form__group row"
		),
		Div(
			Div('obligacion', css_class="col-md-4"),
			Div('clasificacion', css_class="col-md-4"),
			Div('clasificacion_contable', css_class="col-md-4"),
			css_class="form-group m-form__group row"
		),
		Div(
			Div('rfc', css_class="col-md-4"),
			Div('producto', css_class="col-md-4"),
			Div('forma_pago', css_class="col-md-4"),
			css_class="form-group m-form__group row"
		),
		Div(
			Div('fecha_otorgado', css_class="col-md-6"),
			Div('fecha_vencimiento', css_class="col-md-6"),
			css_class="form-group m-form__group row"
		),
		
		Div(
			Div('tipo_tasa', css_class="col-md-4"),
			Div('tasa', css_class="col-md-4"),
			css_class="form-group m-form__group row"
		),
		Div(
			Div('plazo', css_class="col-md-4"),
			Div('monto', css_class="col-md-4"),
			Div('fondeador', css_class="col-md-4"),
			css_class="form-group m-form__group row"
		),
	],
}
class WalletCredit(Model_base):
	organization = models.ForeignKey('mirari.Organization', blank=True, null=True, on_delete=models.CASCADE, related_name='+',)
	numero = models.IntegerField('ID CLiente', blank=True, null=True	)
	obligacion = models.CharField('Obligación', max_length=250, blank=True, null=True)
	clasificacion = models.CharField('Clasificación', max_length=250, blank=True, null=True)
	clasificacion_contable = models.CharField('Clasificación contable', max_length=250, choices=CLASIFICACION_CONTABLE, blank=True, null=True)
	nombre = models.CharField('Nombre', max_length=250, blank=True, null=True)
	tipo = models.CharField('Tipo de persona', max_length=250, blank=True, null=True)
	rfc = models.CharField('RFC', max_length=250, blank=True, null=True)
	producto = models.CharField('Producto', max_length=250, blank=True, null=True)
	forma_pago = models.CharField('Forma de pago', max_length=250, choices=FORMA_PAGO, blank=True, null=True)
	tipo_tasa = models.CharField('Tipo de tasa', max_length=250, choices=TIPO_TASA, blank=True, null=True)
	tasa = models.CharField('Tasa', max_length=250, blank=True, null=True)
	fecha_otorgado = models.DateField('Fecha otorgado', blank=True, null=True)
	fecha_vencimiento = models.DateField('Fecha vencimiento', blank=True, null=True)
	plazo = models.CharField('Plazo', max_length=250, blank=True, null=True)
	monto = models.CharField('Monto', max_length=250, blank=True, null=True)
	fondeador = models.CharField('Fondeador', max_length=250, blank=True, null=True)
	VARS = VARS
	class Meta(Model_base.Meta):
		verbose_name = VARS['NAME']
		verbose_name_plural = VARS['PLURAL']
		permissions = permissions(VARS)
	def __str__(self):
		return '{0}'.format(self.VARS['NAME'])
	def get_Plazo(self):
		return '{0} meses'.format(int(self.plazo))
	def get_Monto(self):
		return Money(self.monto, 'MXN')



VARS = {
	'NAME':'Tabla de amortización',
	'PLURAL':'Tablas de amortización',
	'MODEL':'TablaAmortizacion',
	'NEW':'NUEVO',
	'NEW_GENDER': 'un nuevo',
	'THIS': 'este',
	'APP':APP,
	'EXCLUDE_PERMISSIONS':['all'],
}
class TablaAmortizacion(Model_base):
	VARS = VARS
	class Meta(Model_base.Meta):
		verbose_name = VARS['NAME']
		verbose_name_plural = VARS['PLURAL']
		permissions = permissions(VARS)
	def __str__(self):
		return '{0}'.format(self.VARS['NAME'])



VARS = {
	'NAME':'Tasa de interés',
	'PLURAL':'Tasas de interés',
	'MODEL':'TasasInteres',
	'NEW':'NUEVO',
	'NEW_GENDER': 'una nueva',
	'THIS': 'esta',
	'APP':APP,
}
class TasasInteres(Model_base):
	VARS = VARS
	class Meta(Model_base.Meta):
		verbose_name = VARS['NAME']
		verbose_name_plural = VARS['PLURAL']
		permissions = permissions(VARS)
	def __str__(self):
		return '{0}'.format(self.VARS['NAME'])




		