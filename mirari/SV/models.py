# -*- coding: utf-8 -*-
from mirari.mirari.models import *
from .vars import *

########################################################################################
########################################################################################
VARS = {
	'NAME':'Punto de venta',
	'PLURAL':'Puntos de venta',
	'MODEL':'Sellpoint',
	'NEW':'NUEVO',
	'NEW_GENDER': 'un nuevo',
	'THIS': 'este',
	'APP':APP,
	'LIST': [
		{
			'field': 'name',
			'title': 'Nombre',
		},
		{
			'field': 'property_get_have_cashier',
			'title': 'Tiene caja?',
		},
		{
			'field': 'number_tickets',
			'title': '# Tickets',
		},
		{
			'field': 'property_get_folio',
			'title': 'FOLIO',
		},
		{
			'field': 'property_get_color',
			'title': 'COLOR',
		},
	],
	'SEARCH': ['name'],
	'SORTEABLE': ['name'],
	'EXCLUDE_FORM': ['serial'],
}
class Sellpoint(Model_base):
	organization = models.ForeignKey('mirari.Organization', related_name='+', on_delete=models.CASCADE)
	name = models.CharField('Nombre del punto de venta', max_length=250)
	serial = models.ForeignKey('mirari.Serial', verbose_name="Serie de folios", related_name='+', on_delete=models.SET_NULL, null=True, blank=True, help_text='Asocia una serie a este punto de venta. <strong> Déjalo vacio para asignar folios aleatorios </strong>')
	creation_date = models.DateTimeField(auto_now_add=True)
	modified_date = models.DateTimeField(auto_now=True)
	have_cashier = models.BooleanField('Cobran vendedores?', default=False, help_text='Tienes vendedores autorizados para cobrar en esta sucursal?')
	color = models.CharField('Color del Punto de Venta', max_length=50, default='#191919')
	number_tickets = models.IntegerField('Numero de tickets que imprime', default=1)
	header_line_black_1 = models.CharField('Linea 1 del encabezado del ticket', max_length=80, blank=True, null=True)
	header_line_black_2 = models.CharField('Linea 2 del encabezado del ticket', max_length=80, blank=True, null=True)
	header_line_1 = models.CharField('Linea 1 del texto del ticket', max_length=80, blank=True, null=True)
	header_line_2 = models.CharField('Linea 2 del texto del ticket', max_length=80, blank=True, null=True)
	footer_line_1 = models.CharField('Linea 1 del pie del ticket', max_length=80, blank=True, null=True)
	is_active = models.BooleanField('Esta activo?', default=True, help_text='Desactiva este punto de venta')
	VARS = VARS
	class Meta(Model_base.Meta):
		verbose_name = VARS['NAME']
		verbose_name_plural = VARS['PLURAL']
		permissions = permissions(VARS)
	def __str__(self):
		return '{0}'.format(self.name)
	def get_have_cashier(self):
		return self.render_boolean(self.have_cashier)
	def get_color(self):
		return self.render_color(self.color)
	def get_folio(self):
		return self.serial.serial
	def save(self, *args, **kwargs):
		self.name = self.name.upper()
		super().save()
		if not self.serial:
			content_type = ContentType.objects.get(app_label=APP, model=self.VARS['MODEL'].lower())
			serial = Serial.objects.create(organization=self.organization, name=self.name.lower(), content_type=content_type)
			self.serial = serial
			self.save()


########################################################################################
########################################################################################
VARS = {
	'NAME':'Menu',
	'PLURAL':'Menus',
	'MODEL':'Menu',
	'NEW':'NUEVO',
	'NEW_GENDER':'un nuevo',
	'THIS':'este',
	'APP':APP,
	'LIST': [
		{
			'field': 'name',
			'title': 'Nombre',
		},
		{
			'field': 'property_get_parent',
			'title': 'Depende de',
		},
		{
			'field': 'property_get_color',
			'title': 'Color',
		},
		{
			'field': 'property_get_is_active',
			'title': 'Activo?',
		},
	],
	'SEARCH': ['name'],
	'SORTEABLE': ['name'],
	'SELECTQ': {
		'parent': {
			'plugin': 'select2',
		},
	},
	'FORM': ('name','color','parent','is_active'),
}
class Menu(Model_base, MPTTModel):
	organization = models.ForeignKey('mirari.Organization', on_delete=models.CASCADE)
	name = models.CharField('Nombre del menú', max_length=30)
	color = models.CharField('Color del menú', default='#3d3b56', max_length=100)
	is_active = models.BooleanField('Esta activo?', default=True, help_text='Desactiva todos los productos de un menú')
	parent = TreeForeignKey('self', null=True, blank=True, related_name='+', db_index=True, on_delete=models.PROTECT, verbose_name='', help_text='Elige otro menú solo si este menú depende de otro')
	nivel = models.PositiveIntegerField(default=1)
	VARS = VARS
	class Meta(Model_base.Meta):
		verbose_name = VARS['NAME']
		verbose_name_plural = VARS['PLURAL']
		permissions = permissions(VARS)
	def __str__(self):
		return '{0}'.format(self.name)
	def get_color(self):
		return self.render_color(self.color)
	def get_is_active(self):
		return self.render_boolean(self.is_active)
	def get_parent(self):
		if self.parent:
			return self.render_if(self.parent.str_obj())
		else:
			return self.render_if(self.parent)


########################################################################################
########################################################################################
VARS = {
	'NAME':'Producto',
	'PLURAL':'Productos',
	'MODEL':'Product',
	'NEW':'NUEVO',
	'NEW_GENDER':'un nuevo',
	'THIS':'este',
	'APP':APP,
	'QUERY':{
		'query': [
			(
				('menu__organization','Organization.objects.get(pk=self.request.session.get("organization"))'),
				('active','True'),
			)
		],
	},
	'LIST': [
		{
			'field': 'name',
			'title': 'Información de producto',
			'template': '<span><strong>{{name}} </strong> {{property_get_is_active}}<br /> {{property_get_menu}} <br /><small>{{property_get_code}}<br /> {{property_get_units}}</small></span>',
		},
		{
			'field': 'code',
			'title': 'Productos en sucursales',
			'template': '{{property_get_productattributes}}',
		},
	],
	'SEARCH': ['name'],
	'SORTEABLE': ['name'],
	'FILTERS': {
		'is_active': {
			'size':'4',
			'label':'Mostrar activos?',
			'list': [
				[1,'Mostrar activos'],
				[0,'Mostrar desactivados'],
			],
		},
		'menu': {
			'size':'4',
			'label':'Filtar Menu',
			'model':['SV','Menu'],
			'query':[
				(
					('organization','Organization.objects.get(pk=self.request.session.get("organization"))'),
					('active','True'),
				)
			],
		}
	},
	'SERIALIZER': ['get_code','get_units','get_is_active','get_productattributes','get_menu','get_color','get_sellpoint'],
	'SELECTQ': {
		'code': {
			'model': ['mirari', 'ProductsServicesSAT'],
			'query': 'NONE',
			'plugin': 'select2',
			'sercheable': ['code__icontains', 'name__icontains'],
			'limits': 50,
			'placeholder': 'Elige un producto o código del producto',
		},
		'units': {
			'model': ['mirari', 'UnitsCodesSat'],
			'query': 'NONE',
			'plugin': 'select2',
			'sercheable': ['code__icontains', 'name__icontains'],
			'limits': 50,
			'placeholder': 'Elige una unidad o código de la unidad',
		},
		'sellpoints': {
			'plugin': 'selectmultiple',
		},
		'menu': {
			'model': ['SV', 'Menu'],
			'plugin': 'select2',
			'query': [
				(
					('organization', 'Organization.objects.get(pk=self.request.session.get("organization"))'),
					('active', 'True'),
				),
			],
		},
	},
	'FORM': ('name','code','units','sellpoints','menu','is_active'),
	#'EXTRA_FORM': [{
		#'title': 'Atributos',
		#'atributes': ('hidden',),
		#'views': ('CreateView',),
		#'form':[
			#{
				#'label': 'Precio',
				#'type': 'number',
				#'name': 'price',
				#'rules': [],
			#},
			#{
				#'label': 'IVA',
				#'type': 'boolean',
				#'name': 'iva',
				#'rules': [],
			#},
			#{
				#'label': 'IEPS',
				#'type': 'boolean',
				#'name': 'ieps',
				#'rules': [],
			#},
			#{
				#'label': 'Código de barras',
				#'type': 'text',
				#'name': 'bar_code',
				#'rules': [],
			#},
			#{
				#'label': 'Es dinámico',
				#'type': 'boolean',
				#'name': 'is_dynamic',
				#'rules': [],
			#},
			#{
				#'label': 'Es favorito',
				#'type': 'boolean',
				#'name': 'is_favorite',
				#'rules': [],
			#},
		#]
	#}],
}
class Product(Model_base):
	name = models.CharField('Nombre del producto', max_length=250)
	code = models.ForeignKey('mirari.ProductsServicesSAT', blank=True, null=True,on_delete=models.PROTECT, verbose_name="Código de producto en el SAT", help_text='Código de registro ante el SAT', related_name='+')
	units = models.ForeignKey('mirari.UnitsCodesSat', blank=True, null=True,on_delete=models.PROTECT, verbose_name="Código de unidad en el SAT", help_text="Unidad de medida para este producto", related_name='+')
	sellpoints = models.ManyToManyField('Sellpoint', blank=True, related_name='+', verbose_name="", help_text="Se vende en estas sucursales")
	menu = models.ForeignKey('Menu', on_delete=models.PROTECT, verbose_name="", help_text="Elige el menú donde se vende este producto")
	is_active = models.BooleanField('Esta activo?', default=True, help_text='Desactivar producto?')
	VARS = VARS
	class Meta(Model_base.Meta):
		verbose_name = VARS['NAME']
		verbose_name_plural = VARS['PLURAL']
		permissions = permissions(VARS)
	def __str__(self):
		return '{0}'.format(self.name)
	def my_organization(self):
		return self.menu.organization
	def get_is_active(self):
		return self.render_boolean(self.is_active)
	def get_code(self):
		if self.code:
			return self.code.str_obj()
		else:
			'-'
	def get_units(self):
		if self.units:
			return self.units.str_obj()
		else:
			'-'
	def get_menu(self):
		return mark_safe(self.render_boolean_del('<small class="m--font-'+self.menu.render_string_color(self.menu.is_active)+'" style="color:'+self.menu.color+'!important">'+self.menu.name+'</small>', self.menu.is_active))
	def get_color(self):
		return self.menu.color
	def get_productattributes(self):
		string = ''
		for sellpoint in self.sellpoints.all():
			productattributes = ProductAttributes.objects.get(product=self,sellpoint=sellpoint)
			string += """
					<div class="m-portlet m-portlet--full-height" style="border-style:solid;border-width:1px;color:#e6e6e6;margin-bottom: .5rem;">
						<div class="m-portlet__body m--padding-5 m--padding-right-10 m--padding-left-10 ">
							<div class="m-widget3">
								<div class="m-widget3__item">
									<div class="m-widget3__header">
										<div class="m-widget3__info" style="padding-left: 0rem;">
											<span class="m-widget3__username">{8}</span>
											<span class="m-widget3__time m--margin-left-5">
												{1}
											</span>
										</div>
										<a href="{9}" class="btn btn-outline-brand m-btn m-btn--icon m-btn--icon-only m-btn--custom m-btn--pill btn-sm m--margin-right-25 m--margin-top-5 m--pull-right" title="Editar" style="width: 20px;height: 20px;">
											<i class="la la-edit" style="font-size:12px;"></i>
										</a>
									</div>
									<div class="m-widget3__body">
										<p class="m-widget3__text m--margin-bottom-5" style="font-size:11px;">
											<strong>{0}</strong> <i class="fa fa-barcode m--margin-left-10" style="font-size:12px;"></i> <strong>{4}</strong>
										</p>
										<p class="m-widget3__text" style="font-size:11px;">
											{2} {3} {7} {5} {6}
										</p>
									</div>
								</div>
							</div>
						</div>
					</div>
			""".format(
				productattributes.get_alias(),
				productattributes.get_format_price(),
				productattributes.get_badge_iva(),
				productattributes.get_badge_ieps(),
				productattributes.get_bar_code(),
				productattributes.get_badge_is_dynamic(),
				productattributes.get_badge_is_favorite(),
				productattributes.get_badge_is_active(),
				productattributes.get_sellpoint(),
				productattributes.url_update(),
			)
		if not string:
			string = '<strong>No hay puntos de venta asociados</strong>'
		return mark_safe(string)
def sellpoints_changed(sender, **kwargs):
	action = kwargs.pop('action', None)
	instance = kwargs.pop('instance', None)
	if action == 'post_add':
		for sellpoint in instance.sellpoints.all():
			productAttributes = ProductAttributes.objects.get_or_create(product=instance,sellpoint=sellpoint)[0]
			productAttributes.active=True
			productAttributes.save()
	if action == 'pre_remove':
		for sellpoint in instance.sellpoints.all():
			productAttributes = ProductAttributes.objects.get_or_create(product=instance,sellpoint=sellpoint)[0]
			productAttributes.active=False
			productAttributes.save()
m2m_changed.connect(sellpoints_changed, sender=Product.sellpoints.through)


########################################################################################
########################################################################################
VARS = {
	'NAME':'Atributo de producto',
	'PLURAL':'Atributos de producto',
	'MODEL':'ProductAttributes',
	'NEW':'NUEVO',
	'NEW_GENDER': 'un nuevo',
	'THIS':'este',
	'APP':APP,
	'EXCLUDE_PERMISSIONS': ['ALL'],
	#'EXTEND_PERMISSIONS': [('Can_Change__ProductAttributesSuVenta', 'Modifica atributos de producto')],
	'REDIRECT_MODEL':['SuVenta','Product'],
	'FORM': ('alias','price','bar_code','iva','ieps','is_dynamic','is_favorite','is_active',),
	'RULES': """
		price: {
			min: 0,
		},
	""",
}
class ProductAttributes(Model_base):
	product = models.ForeignKey('Product', related_name='Product', on_delete=models.CASCADE)
	sellpoint = models.ForeignKey('Sellpoint', related_name='Sellpoint', on_delete=models.CASCADE)
	alias = models.CharField(max_length=250, blank=True, null=True, help_text="Nombre con el que se imprime este producto", default="")
	price = models.FloatField('Precio en esta sucursal',default=0)
	iva = models.BooleanField('I.V.A.', default=True, help_text="Graba IVA?")
	ieps = models.BooleanField('IEPS.', default=True, help_text="Graba IEPS?")
	bar_code = models.CharField('Código de Barras', max_length=250, blank=True, null=True,)
	is_dynamic = models.BooleanField('Precio dinámico', default=False, help_text='Este producto tiene precio variable?')
	is_favorite = models.BooleanField('Es favorito?', default=False, help_text='Se muestra siempre este producto?')
	is_active = models.BooleanField('Esta activo?', default=True, help_text='Desactivar producto?')
	VARS = VARS
	class Meta(Model_base.Meta):
		verbose_name = VARS['NAME']
		verbose_name_plural = VARS['PLURAL']
		permissions = permissions(VARS)
	def __str__(self):
		return '{0} | {1}'.format(self.sellpoint, self.product.name)
	def my_organization(self):
		return self.sellpoint.organization
	def check_is_active(self):
		if not self.product.is_active:
			return False
		elif not self.product.menu.is_active:
			return False
		elif not self.sellpoint.is_active:
			return False
		return self.is_active
	def get_format_price(self):
		return '${:20,.2f}'.format(self.price)
	def get_alias(self):
		if self.alias:
			return self.alias
		return self.product.name
	def get_bar_code(self):
		return self.render_if(self.bar_code)
	def get_badge_iva(self):
		return mark_safe('<span class="m-badge m-badge--wide m-badge--rounded m-badge--'+self.render_string_color(self.iva)+' m-badge--wide">I.V.A.</span>')
	def get_badge_ieps(self):
		return mark_safe('<span class="m-badge m-badge--wide m-badge--rounded m-badge--'+self.render_string_color(self.ieps)+' m-badge--wide">IEPS</span>')
	def get_badge_is_dynamic(self):
		return mark_safe('<span class="m-badge m-badge--wide m-badge--rounded m-badge--'+self.render_string_color(self.is_dynamic)+' m-badge--wide">Dinámico</span>')
	def get_badge_is_favorite(self):
		return mark_safe('<span class="m-badge m-badge--wide m-badge--rounded m-badge--'+self.render_string_color(self.is_favorite)+' m-badge--wide">Favorito</span>')
	def get_badge_is_active(self):
		return mark_safe('<span class="m-badge m-badge--wide m-badge--rounded m-badge--'+self.render_string_color(self.is_active)+' m-badge--wide">Activo</span>')
	def get_sellpoint(self):
		return mark_safe(self.render_boolean_del('<span class="m--font-'+self.sellpoint.render_string_color(self.sellpoint.is_active)+'" style="color:'+self.sellpoint.color+'!important">'+self.sellpoint.name+'</span>', self.sellpoint.is_active))


########################################################################################
########################################################################################
VARS = {
	'NAME': 'Acceso de empleado',
	'PLURAL': 'Accesos de empleados',
	'MODEL': 'EmployeeAccess',
	'NEW': 'NUEVO',
	'NEW_GENDER': 'un nuevo',
	'THIS': 'este',
	'APP': APP,
	'QUERY': {
		'query': [
			(
				('user__organization', 'Organization.objects.get(pk=self.request.session.get("organization"))'),
				('active', 'True'),
			)
		],
	},
	'LIST': [
		{
			'field': 'property_get_user',
			'title': 'Usuario',
		},
		{
			'field': 'property_get_sellpoint',
			'title': 'Puntos de venta',
		},
		{
			'field': 'profiles',
			'title': 'Perfil',
		},
	],
	#'SEARCH': ['user', 'list_sellpoint', 'vire'],
	'SORTEABLE': ['id'],
	#'FILTERS': {
		#'is_active': {
			#'size': '4',
			#'label': 'Mostrar activos?',
			#'list': [
				#[1, 'Mostrar activos'],
				#[0, 'Mostrar desactivados'],
			#],
		#},
	#},
	'SELECTQ': {
		'user': {
			'model': ['mirari', 'User'],
			'plugin': 'select2',
			'query': [
				(
					('organization', 'Organization.objects.get(pk=self.request.session.get("organization"))'),
					('active', 'True'),
				),
			],
		},
		'sellpoints': {
			'model': ['SV', 'Sellpoint'],
			'plugin': 'select2',
			'query': [
				(
					('organization', 'Organization.objects.get(pk=self.request.session.get("organization"))'),
					('active', 'True'),
				),
			],
		},
		'profiles': {
			'plugin': 'select2',
		},
	},
	#'RULES': """
		#email: {
			#required: true,
			#email: true,
		#},
	#""",
}
class EmployeeAccess(Model_base):
	user = models.ForeignKey('mirari.User', on_delete=models.CASCADE, related_name='+', verbose_name="Usuario")
	sellpoints = models.ManyToManyField('Sellpoint', related_name='+', verbose_name="", help_text="Asignado a estas sucursales",)
	profiles = models.CharField('Perfil', max_length=30, choices={
            ('vendor', 'Vendedor'),
            ('casher', 'Cajero'),
            ('supervisor','Supervisor'),
        })
	VARS = VARS
	class Meta(Model_base.Meta):
		verbose_name = VARS['NAME']
		verbose_name_plural = VARS['PLURAL']
		permissions = permissions(VARS)
	def __str__(self):
		return '{0} | {1} | {2}'.format(self.user, self.sellpoints, self.profiles)
	def get_sellpoint(self):
		return self.render_list(self.sellpoints.all(), 'name')
	def get_user(self):
		return self.user.visible_username
