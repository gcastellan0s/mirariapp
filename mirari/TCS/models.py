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
	company = models.ForeignKey('Company', on_delete=models.CASCADE, related_name='+', verbose_name="Compañia")
	name = models.CharField('Nombre de la tienda', max_length=250)
	VARS = VARS
	class Meta(Model_base.Meta):
		verbose_name = VARS['NAME']
		verbose_name_plural = VARS['PLURAL']
		permissions = permissions(VARS)
	def __str__(self):
		return self.name
	def QUERY(self, view):
		return Store.objects.filter(company__organization__pk=view.request.session.get('organization'), active=True)



VARS = {
	'NAME':'Marca',
	'PLURAL':'Marcas',
	'MODEL':'Brand',
	'NEW':'NUEVA',
	'NEW_GENDER': 'una nueva',
	'THIS': 'esta',
	'APP':APP,
	'SELECTQ': {
		'company': {
			'plugin': 'selectmultiple',
		},
	},
	'EXCLUDE_PERMISSIONS': ['all'],
}
class Brand(Model_base):
	company = models.ManyToManyField('Company', verbose_name="Empresas que la venden")
	name = models.CharField('Marca', max_length=250)
	VARS = VARS
	class Meta(Model_base.Meta):
		verbose_name = VARS['NAME']
		verbose_name_plural = VARS['PLURAL']
		permissions = permissions(VARS)
	def __str__(self):
		return self.name
	def QUERY(self, view):
		return Brand.objects.filter(company__organization__pk=view.request.session.get('organization'), active=True).distinct()



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
	brand = models.ForeignKey('Brand', on_delete=models.SET_NULL, null=True, verbose_name="Marca")
	name = models.CharField('Nombre del modelo', max_length=250)
	VARS = VARS
	class Meta(Model_base.Meta):
		verbose_name = VARS['NAME']
		verbose_name_plural = VARS['PLURAL']
		permissions = permissions(VARS)
	def __str__(self):
		return self.name
	def QUERY(self, view):
		return Modelo.objects.filter(brand__company__organization__pk=view.request.session.get('organization'), active=True).distinct()

VARS = {
	'NAME':'Orden de servicio',
	'PLURAL':'Ordenes de servicio',
	'MODEL':'OrderService',
	'NEW':'NUEVA',
	'NEW_GENDER': 'una nueva',
	'THIS': 'esta',
	'APP':APP,
	'EXCLUDE_PERMISSIONS': ['all'],
	'HIDE_CHECKBOX_LIST': True,
	'HIDE_BUTTONS_LIST': True,
	'SERIALIZER': ('get_service_date_html','get_client_name_html','get_contact_phone1_html','get_contact_phone2_html','get_id_html','get_creation_date_html','get_technical_html','get_concept_html', 'get_status_html'),
	'LIST': [
		{
			'field': 'pk',
			'title': 'Orden de servicio',
			'template': 
				"""
					<a href="{{property_url_update}}" style="color:inherit;text-decoration:none;">
						<span>
							{{property_get_id_html}}
							{{property_get_creation_date_html}}
							{{property_get_technical_html}}
							{{property_get_concept_html}}
						</span>
					</a>
				""",
		},
		{
			'field': 'service_date',
			'title': 'Cliente',
			'template': 
				"""
					<a href="{{property_url_update}}" style="color:inherit;text-decoration:none;">
						<span>
						
							{{property_get_service_date_html}}
							{{property_get_client_name_html}}
							{{property_get_contact_phone1_html}}
							{{property_get_contact_phone2_html}}
						</span>
					</a>
				""",
		},
		{
			'field': 'service_date',
			'title': 'Informacion',
			'template': 
				"""
					<a href="{{property_url_update}}" style="color:inherit;text-decoration:none;">
						<span>
							{{property_get_service_date_html}}
							{{property_get_client_name_html}}
							{{property_get_contact_phone1_html}}
							{{property_get_contact_phone2_html}}
						</span>
					</a>
				""",
		},
		{
			'field': 'service_date',
			'title': 'Extra',
			'template': 
				"""
					<a href="{{property_url_update}}" style="color:inherit;text-decoration:none;">
						<span>
							{{property_get_service_date_html}}
							{{property_get_client_name_html}}
							{{property_get_contact_phone1_html}}
							{{property_get_contact_phone2_html}}
						</span>
					</a>
				""",
		},
	],
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
			'field_filter': (
				('zone', """$("input[name='zone']:checked").val()"""),
			),
			'minimumInputLength': '0',
		},
		'company': {
			'model': ['TCS', 'Company'],
			'plugin': 'select2',
			'query': [
				(
					('organization__pk', 'self.request.session.get("organization")'),
				),
			],
			'placeholder': 'Elige una empresa',
		},
		'store': {
			'model': ['TCS', 'Store'],
			'plugin': 'select2',
			'query': 'none',
			'sercheable': ('name__icontains',),
			'limits': 50,
			'placeholder': 'Elige una tienda',
			'field_filter': (
				('company', """$("#id_company").val()"""),
			),
			'minimumInputLength': '0',
		},
		'brand': {
			'model': ['TCS', 'Brand'],
			'plugin': 'select2',
			'query': 'none',
			'sercheable': ('name__icontains',),
			'limits': 50,
			'placeholder': 'Elige una marca',
			'field_filter': (
				('company', """$("#id_company").val()"""),
			),
			'minimumInputLength': '0',
		},
		'modelo': {
			'model': ['TCS', 'Modelo'],
			'plugin': 'select2',
			'query': 'none',
			'sercheable': ('name__icontains',),
			'limits': 50,
			'placeholder': 'Elige un modelo',
			'field_filter': (
				('brand', """$("#id_brand").val()"""),
			),
			'minimumInputLength': '0',
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
				Div('status'),
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
	'FORM_SIZE': ('col-xl-8 offset-xl-2','col-xl-9'),
	'EXTRA_FORM': 'OrderService__EXTRAFORM.html',
}
class OrderService(Model_base):
	organization = models.ForeignKey('mirari.Organization', blank=True, null=True, on_delete=models.CASCADE, related_name='+',)
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
	hidden_notes = models.TextField(blank=True, verbose_name="Notas OCULTAS<small>(No se imprimen en la orden)</small>")
	order_notes = models.TextField(blank=True, verbose_name="Notas IMPRESAS<small>(Impresas en la orden)</small>")
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
		return str(self.pk)
	def url_add(self):
		return reverse('mirari:Generic__CreateView', kwargs={'app': self.VARS['APP'], 'model': self.VARS['MODEL']})
	def url_update(self):
		return reverse('mirari:Generic__UpdateView', kwargs={'app': self.VARS['APP'], 'model': self.VARS['MODEL'], 'pk': self.pk})
	def select2filter(self, query):
		if self.request.GET.get('field') == 'technical':
			team = apps.get_model('INT', 'Team').objects.filter(code=self.request.GET.get('zone'), organization__id=self.request.session['organization']).first()
			if team:
				query = query.filter( pk__in = list(team.members.all().values_list('pk', flat=True)) )
			else:
				query = None
		if self.request.GET.get('field') == 'store':
			if self.request.GET.get('company'):
				query = query.filter(company = apps.get_model('TCS', 'Company').objects.filter(pk=self.request.GET.get('company')).first())
			else:
				query = query.none()
		if self.request.GET.get('field') == 'brand':
			if self.request.GET.get('company'):
				query = query.filter(company = apps.get_model('TCS', 'Company').objects.filter(pk=self.request.GET.get('company')).first())
			else:
				query = query.none()
		if self.request.GET.get('field') == 'modelo':
			if self.request.GET.get('brand'):
				query = query.filter(brand = apps.get_model('TCS', 'Brand').objects.filter(pk=self.request.GET.get('brand')).first())
			else:
				query = query.none()
		return query
	def QUERY(self, view):
		return OrderService.objects.filter(organization__pk=view.request.session.get('organization'), active=True).distinct()
	def get_id_html(self):
		return '<strong class="mr-2 m--icon-font-size-lg3">{0}</strong> <small>[{1}]</small><br />'.format(self.id, self.service.upper())
	def get_creation_date_html(self):
		return """<i class="fa fa-calendar m--icon-font-size-sm5 mr-1"></i>{0}<br />""".format(self.creation_date.strftime('%d %b %Y %I:%M %p'))
	def get_technical_html(self):
		return """<i class="fa fa-user-cog m--icon-font-size-sm5 mr-1"></i> TEC: {0}<br />""".format(self.technical)
	def get_concept_html(self):
		return """<i class="fa fa-cog m--icon-font-size-sm5 mr-1"></i>{0}<br />""".format(self.concept)
	def get_service_date_html(self):
		if self.service_date:
			return """<i class="fa fa-calendar m--icon-font-size-sm5 mr-1"></i>{0}<br />""".format(self.service_date.strftime('%d %b %Y'))
		else:
			return '<i class="fa fa-calendar m--icon-font-size-sm5 mr-1"></i>'
	def get_client_name_html(self):
		if self.client_name:
			return """<i class="fa fa-user m--icon-font-size-sm5 mr-1"></i>{0}<br />""".format(self.client_name.title())
		else:
			return ''
	def get_contact_phone1_html(self):
		if self.contact_phone1:
			return """<i class="fa fa-mobile m--icon-font-size-sm5 mr-1"></i>CEL: {0}<br />""".format(self.contact_phone1)
		else:
			return ''
	def get_contact_phone2_html(self):
		if self.contact_phone2:
			return """<i class="fa fa-phone m--icon-font-size-sm5 mr-1"></i>TEL: {0}<br />""".format(self.contact_phone2)
		else:
			return ''


VARS = {
	'NAME':'Historial de Orden',
	'PLURAL':'Historial de Ordenes',
	'MODEL':'OrderServiceHistory',
	'NEW':'NUEVA',
	'NEW_GENDER': 'una nueva',
	'THIS': 'esta',
	'APP':APP,
	'EXCLUDE_PERMISSIONS': ['all'],
}
class OrderServiceHistory(Model_base):
	orderservice = models.ForeignKey('OrderService', blank=True, null=True, on_delete=models.CASCADE, related_name='+',)
	user = models.ForeignKey('mirari.User', related_name='+', on_delete=models.SET_NULL, null=True)
	notes = models.TextField(blank=True, verbose_name="Notas <small>(Impresas en la orden)</small>")
	VARS = VARS
	class Meta(Model_base.Meta):
		verbose_name = VARS['NAME']
		verbose_name_plural = VARS['PLURAL']
		permissions = permissions(VARS)
	def __str__(self):
		return str(self.pk)