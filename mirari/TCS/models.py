# -*- coding: utf-8 -*-
from mirari.mirari.models import *
from .vars import *

VARS = {
	'NAME':'Empresa',
	'PLURAL':'Empresas',
	'MODEL':'Company',
	'NEW':'NUEVA',
	'NEW_GENDER': 'una nueva',
	'THIS': 'esta',
	'APP':APP,
	'EXCLUDE_PERMISSIONS': ['all'],
}
class Company(Model_base):
	organization = models.ForeignKey('mirari.Organization', blank=True, null=True, on_delete=models.CASCADE, related_name='+',)
	name = models.CharField('Nombre de la empresa', max_length=250)
	VARS = VARS
	class Meta(Model_base.Meta):
		verbose_name = VARS['NAME']
		verbose_name_plural = VARS['PLURAL']
		permissions = permissions(VARS)
	def __str__(self):
		return self.name

VARS = {
	'NAME':'Tienda',
	'PLURAL':'Tiendas',
	'MODEL':'Store',
	'NEW':'NUEVA',
	'NEW_GENDER': 'una nueva',
	'THIS': 'esta',
	'APP':APP,
	'EXCLUDE_PERMISSIONS': ['all'],
	'SELECTQ': {
		'company': {
			'plugin': 'select2',
		},
	},
}
class Store(Model_base):
	organization = models.ForeignKey('mirari.Organization', blank=True, null=True, on_delete=models.CASCADE, related_name='+',)
	company = models.ForeignKey('Company', on_delete=models.CASCADE, related_name='+', verbose_name="Compañia")
	name = models.CharField('Nombre de la tienda', max_length=250)
	VARS = VARS
	class Meta(Model_base.Meta):
		verbose_name = VARS['NAME']
		verbose_name_plural = VARS['PLURAL']
		permissions = permissions(VARS)
	def __str__(self):
		return self.name

VARS = {
	'NAME':'Marca',
	'PLURAL':'Marcas',
	'MODEL':'Brand',
	'NEW':'NUEVA',
	'NEW_GENDER': 'una nueva',
	'THIS': 'esta',
	'APP':APP,
	'SELECTQ': {
		'store': {
			'plugin': 'selectmultiple',
		},
	},
	'EXCLUDE_PERMISSIONS': ['all'],
}
class Brand(Model_base):
	organization = models.ForeignKey('mirari.Organization', blank=True, null=True, on_delete=models.CASCADE, related_name='+',)
	store = models.ManyToManyField('Store', verbose_name="Tienda donde se vende")
	name = models.CharField('Marca', max_length=250)
	VARS = VARS
	class Meta(Model_base.Meta):
		verbose_name = VARS['NAME']
		verbose_name_plural = VARS['PLURAL']
		permissions = permissions(VARS)
	def __str__(self):
		return self.name

VARS = {
	'NAME':'Modelo',
	'PLURAL':'Modelos',
	'MODEL':'Modelo',
	'NEW':'NUEVO',
	'NEW_GENDER': 'un nuevo',
	'THIS': 'este',
	'APP':APP,
	'SELECTQ': {
		'brand': {
			'plugin': 'select2',
		},
	},
	'EXCLUDE_PERMISSIONS': ['all'],
}
class Modelo(Model_base):
	organization = models.ForeignKey('mirari.Organization', blank=True, null=True, on_delete=models.CASCADE, related_name='+',)
	brand = models.ForeignKey('Brand', on_delete=models.SET_NULL, null=True, verbose_name="Marca")
	name = models.CharField('Nombre del modelo', max_length=250)
	VARS = VARS
	class Meta(Model_base.Meta):
		verbose_name = VARS['NAME']
		verbose_name_plural = VARS['PLURAL']
		permissions = permissions(VARS)
	def __str__(self):
		return self.name

VARS = {
	'NAME':'Orden de servicio',
	'PLURAL':'Ordenes de servicio',
	'MODEL':'OrderService',
	'NEW':'NUEVA',
	'NEW_GENDER': 'una nueva',
	'THIS': 'esta',
	'APP':APP,
	'EXCLUDE_PERMISSIONS': ['all'],
	'SELECTQ': {
		'technical': {
			'model': ['mirari', 'User'],
			'plugin': 'select2',
			'query': [
				(
					('organization__pk', 'self.request.session.get("organization")'),
				),
			],
			'sercheable': ('visible_username__icontains','email__icontains'),
			'limits': 50,
			'placeholder': 'Elige un técnico',
			'field_filter': (('zone', """$("input[name='zone']:checked").val()"""),)
		},
		'company': {
			'model': ['TCS', 'Company'],
			'plugin': 'select2',
			'query': 'all',
		},
		'store': {
			'model': ['TCS', 'Store'],
			'plugin': 'select2',
			'query': 'none',
		},
		'brand': {
			'model': ['TCS', 'Brand'],
			'plugin': 'select2',
			'query': 'none',
		},
		'modelo': {
			'model': ['TCS', 'Modelo'],
			'plugin': 'select2',
			'query': 'none',
		},
	},
	'FORM': [
		Div(
			Div(
				InlineRadios('service'),
				css_class="col-md-4"
			),
			Div(
				InlineRadios('zone'),
				css_class="col-md-4"
			),
			Div('service_date', css_class="col-md-4"),
			Div(
				InlineRadios('concept'),
				css_class="col-md-8"
			),
			Div('technical', css_class="col-md-4"),
			css_class="form-group m-form__group row"
		),
		Div(
			Div('client_name', css_class="col-md-4"),
			Div('email', css_class="col-md-4"),
			Div('contact_phone1', css_class="col-md-4"),
			Div('contact_phone2', css_class="col-md-4"),
			Div('address', css_class="col-md-8"),
			Div('client_notes', css_class="col-md-8"),
			Div('company', css_class="col-md-4"),
			css_class="form-group m-form__group row"
		),
		Div(
			Div('store', css_class="col-md-4"),
			Div('brand', css_class="col-md-4"),
			Div('modelo', css_class="col-md-4"),
			Div('report_name', css_class="col-md-3"),
			Div('serial_number', css_class="col-md-3"),
			Div('buy_date', css_class="col-md-3"),
			Div('delivery_date', css_class="col-md-3"),
			css_class="form-group m-form__group row"
		),
		Div(
			Div(
				Div('icon_os'),
				Div('icon_ics'),
				Div('icon_ics_2'),
				Div('icon_ics_3'),
				Div('icon_on'),
				Div('icon_cn'),
				css_class="col-md-4"
			),
			Div(
				Div('hidden_notes'),
				Div('order_notes'),
				css_class="col-md-8"
			),
			css_class="form-group m-form__group row"
		),
	],
	'FORM_CLASS': 'small_form',
	'FORM_SIZE': 'col-xl-9',
}
class OrderService(Model_base):
	organization = models.ForeignKey('mirari.Organization', blank=True, null=True, on_delete=models.CASCADE, related_name='+',)
	serial = models.ForeignKey('mirari.Serial', related_name='+', on_delete=models.SET_NULL, null=True)
	creation_date = models.DateTimeField(auto_now_add=True, editable=True)
	user = models.ForeignKey('mirari.User', related_name='+', on_delete=models.SET_NULL, null=True)
	technical = models.ForeignKey('mirari.User', related_name='+', on_delete=models.SET_NULL, null=True, verbose_name="Tecnico")
	status = models.CharField(max_length=250, choices=ESTATUS, verbose_name="Estatus")
	service = models.CharField(max_length=250, choices=SERVICIO, default="Icon", verbose_name="Tipo de servicio")
	zone = models.CharField(max_length=250, choices=ZONAS, default="Local", verbose_name="Zona")
	concept = models.CharField(max_length=250, choices=CONCEPTO, default="Armado", verbose_name="Concepto")
	service_date = models.DateField(verbose_name="Fecha programada")
	buy_date = models.DateField(blank=True, null=True, verbose_name="Fecha de compra")
	delivery_date = models.DateField(blank=True, null=True, verbose_name="Fecha de entrega")
	client_name = models.CharField(max_length=500, verbose_name="Nombre completo del cliente")
	email = models.CharField(max_length=250, blank=True, verbose_name="Email del cliente")
	contact_phone1 = models.CharField(max_length=250, blank=True, verbose_name="Teléfono de contacto del cliente")
	contact_phone2 = models.CharField(max_length=250, blank=True, verbose_name="Teléfono de contacto del cliente")
	address = models.CharField(max_length=500, blank=True, verbose_name="Calle")
	address_lat = models.FloatField(blank=True, null=True)
	address_lng = models.FloatField(blank=True, null=True)
	client_notes = models.TextField(blank=True, verbose_name="Notas sobre el cliente")
	company = models.ForeignKey('Company', on_delete=models.SET_NULL, null=True, verbose_name="Empresa")
	store = models.ForeignKey('Store', on_delete=models.SET_NULL, null=True, verbose_name="Tienda")
	brand = models.ForeignKey('Brand', on_delete=models.SET_NULL, null=True, verbose_name="Marca")
	report_name = models.CharField(max_length=250, blank=True, verbose_name="Nombre de quien reporta")
	modelo = models.ForeignKey('Modelo', on_delete=models.SET_NULL, null=True, verbose_name="Modelo")
	serial_number = models.CharField(max_length=250, blank=True, verbose_name="Numero de serie")
	hidden_notes = models.TextField(blank=True, verbose_name="Notas <small>(No se imprimen en la orden)</small>")
	order_notes = models.TextField(blank=True, verbose_name="Notas <small>(Impresas en la orden)</small>")
	icon_os = models.CharField(max_length=250, blank=True)
	icon_ics = models.CharField('icon ics 1', max_length=250, blank=True)
	icon_ics_2 = models.CharField('icon ics 2', max_length=250, blank=True, default="")
	icon_ics_3 = models.CharField('icon ics 3', max_length=250, blank=True, default="")
	icon_on = models.CharField(max_length=250, blank=True)
	icon_cn = models.CharField(max_length=250, blank=True)
	VARS = VARS
	class Meta(Model_base.Meta):
		verbose_name = VARS['NAME']
		verbose_name_plural = VARS['PLURAL']
		permissions = permissions(VARS)
	def __str__(self):
		return self.name
	def url_add(self):
		return reverse('mirari:Generic__CreateView', kwargs={'app': self.VARS['APP'], 'model': self.VARS['MODEL']}) + '?HTMLPage=OrderService__CreateView'
	def url_update(self):
		return reverse('mirari:Generic__UpdateView', kwargs={'app': self.VARS['APP'], 'model': self.VARS['MODEL'], 'pk': self.pk}) + '?HTMLPage=OrderService__CreateView'
	def select2filter(self, query):
		if self.request.GET.get('field') == 'technical':
			team = apps.get_model('INT', 'Team').objects.filter(code=self.request.GET.get('zone'), organization__id=self.request.session['organization']).first()
			#if team:
				#query = query.filter( pk__in = list(team.members.all().values_list('pk', flat=True)) )
			#else:
				#query = None
			#query = query.filter()
			#model = apps.get_model('INT', 'Team')
			#self.request.GET.get('zone')
		#if self.request.GET.get('field') == 'technical':
			#query = 
		#if self.request.GET.get('field') == 'technical':
			#query = 
		return query