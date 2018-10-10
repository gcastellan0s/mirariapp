# -*- encoding: utf-8 -*-
from .modelbase import *


########################################################################################
########################################################################################
VARS = {
		'NAME': 'Módulo',
		'PLURAL': 'Módulos',
		'MODEL': 'Module',
		'NEW': 'NUEVO',
		'NEW_GENDER': 'un nuevo',
		'THIS': 'este',
		'APP': APP,
		'EXCLUDE_PERMISSIONS': ['all'],
	}
class Module(Model_base):
	name = models.CharField(max_length=100)
	code = models.CharField(max_length=100)
	VARS = VARS
	class Meta(Model_base.Meta):
		verbose_name = VARS['NAME']
		verbose_name_plural = VARS['PLURAL']
		permissions = permissions(VARS)
	def __str__(self):
		return """[ {0} ] {1}""".format(self.code, self.name)


########################################################################################
########################################################################################
VARS = {
		'NAME':"Organización",
		'PLURAL':"Organizaciones",
		'MODEL':"Organization",
		'NEW':"NUEVA",
		'NEW_GENDER': "una nueva",
		'THIS':"esta",
		'APP':APP,
		'EXCLUDE_PERMISSIONS': ['create', 'update', 'delete'],
		'QUERY':{
			'query': [
				(
					('pk','self.request.session.get("organization")'),
				)
			],
		},
		'LIST': [
			{
				'field': 'code',
				'title': 'Código',
			},
			{
				'field': 'name',
				'title': 'Nombre',
			},
			{
				'field': 'property_get_parent',
				'title': 'Depende de',
			},
			{
				'field': 'property_get_domains',
				'title': 'Dominio(s)',
			},
		],
		'SEARCH': ['name','code'],
		'SORTEABLE': ['name','code'],
		'FORM': ['name','code','default_mail','contact_mail', 'sites'],
	}
def path_system(self, filename):
	upload_to = "companys/%s_%s/SYSTEM/%s" % (self.id, self.slug, filename)
	return upload_to
class Organization(MPTTModel, Model_base):
	parent = TreeForeignKey('self', null=True, blank=True, related_name='+', db_index=True, on_delete=models.CASCADE)
	nivel = models.PositiveIntegerField(default=1)
	sites = models.ManyToManyField(Site)
	name = models.CharField('Nombre de la organización', max_length=50)
	code = models.CharField(max_length=150, unique=True)
	default_mail = models.EmailField('Email de la sucursal', blank=True, null=True)
	contact_mail = models.EmailField('Email de contacto para clientes', blank=True, null=True)
	creation_date = models.DateTimeField(auto_now_add=True)
	modules = models.ManyToManyField('Module', blank=True, related_name='+',)
	TITLE = models.CharField(max_length=255, blank=True, null=True)
	SLOGAN = models.CharField(max_length=255, blank=True, null=True)
	LAYOUT = models.CharField(max_length=255, blank=True, null=True)
	STYLE = models.CharField(max_length=255, blank=True, null=True)
	ICO = ProcessedImageField(upload_to=path_system, blank=True, null=True, options={'quality': 100}, help_text="Logo 100x100")
	LOGO = ProcessedImageField(upload_to=path_system, blank=True, null=True, options={'quality': 100}, help_text="Logo 600x600")
	LOGO_WHITE = ProcessedImageField(upload_to=path_system, blank=True, null=True, options={'quality': 100}, help_text="Logo 600x600")
	LOGO_BG = ProcessedImageField(upload_to=path_system, blank=True, null=True)
	LOGO_BG_WHITE = ProcessedImageField(upload_to=path_system, blank=True, null=True)
	REGISTER = models.BooleanField(default=True)
	FACEBOOK = models.BooleanField(default=True)
	VARS = VARS
	class Meta(Model_base.Meta):
		verbose_name = VARS['NAME']
		verbose_name_plural = VARS['PLURAL']
		permissions = permissions(VARS)
	def __str__(self):
		return self.name
	def save(self, *args, **kwargs):
		self.name = self.name.upper()
		self.slug = slugify(self.name)
		super().save()
	def my_organization(self):
		return self
	def get_parent(self):
		return self.render_if(self.parent)
	def get_root(self):
		return self.render_if(self.parent)
	def get_domains(self):
		return self.render_list(self.sites, 'domain')
	def get_my_domains(self):
		return self.sites.all().first()
	def get_modules_code(self):
		return self.modules.all().values_list('code', flat=True)


########################################################################################
########################################################################################
VARS = {
	'NAME': 'Usuario',
	'PLURAL': 'Usuarios',
	'MODEL': 'User',
	'NEW': 'NUEVO',
	'NEW_GENDER': 'un nuevo',
	'THIS': 'este',
	'APP': APP,
	'EXTEND_PERMISSIONS': [('Can_Change__Password', 'Modifica contraseñas'),],
	'LIST': [
		{
			'field': 'visible_username',
			'title': 'Usuario',
		},
		{
			'field': 'property_get_groups',
			'title': 'Perfiles',
		},
		{
			'field': 'property_get_is_active',
			'title': 'Activo?',
		},
	],
	'SEARCH': ['visible_username', 'first_name', 'last_name', 'email'],
	'SORTEABLE': ['visible_username'],
	'SERIALIZER': ('url_password',),
	'FORM': ('visible_username', 'first_name', 'last_name', 'email', 'is_active', 'groups', 'user_permissions', 'birthday', 'phone',),
	'SELECTQ': {
		'groups': {
			'model': ['mirari', 'Profile'],
			'plugin': 'selectmultiple',
		},
		'user_permissions': {
			'model': ['auth', 'Permission'],
			'plugin': 'selectmultiple',
			'query': [
				(
					('content_type__app_label__in', 'Organization.objects.get(pk=self.request.session.get("organization")).get_modules_code()'),
				),
			],
		},
	},
	'RULES': """
		email: {
			required: true,
			email: true,
		},
	""",
}
class User(AbstractUser, Model_base):
	organization = models.ForeignKey('Organization', blank=True, null=True, on_delete=models.CASCADE, related_name='+',)
	visible_username = models.CharField('Usuario', max_length=50, help_text="Obligatorio. Longitud máxima 30 caracteres alfanuméricos (letras, dígitos y @/./+/-/_) solamente.")
	birthday = models.DateField('Fecha nacimiento', blank=True, null=True)
	first_login = models.BooleanField(default=False)
	phone = models.CharField('Telefono de contacto', max_length=50, blank=True, null=True)
	gender = models.CharField('Género', choices=GENDER, max_length=50, blank=True, null=True)
	VARS = VARS
	class Meta(Model_base.Meta):
		verbose_name = VARS['NAME']
		verbose_name_plural = VARS['PLURAL']
		permissions = permissions(VARS)
	def __str__(self):
		if self.visible_username:
			return self.visible_username
		else:
			return """{0}""".format(self.username, self.email)
	def url_list(self):
		return reverse('mirari:User__ListView', kwargs={'app': self.VARS['APP'], 'model': self.VARS['MODEL']})
	def url_add(self):
		return reverse('mirari:User__CreateView', kwargs={'app': self.VARS['APP'], 'model': self.VARS['MODEL']})
	def url_update(self):
		return reverse('mirari:User__UpdateView', kwargs={'app': self.VARS['APP'], 'model': self.VARS['MODEL'], 'pk': self.pk})
	def url_password(self):
		return reverse('mirari:UserPassword__UpdateView', kwargs={'app': self.VARS['APP'], 'model': self.VARS['MODEL'], 'pk': self.pk})
	def my_organizations(self):
		if self.is_superuser:
			return Organization.objects.all()
		return self.organization.get_descendants(include_self=True)
	def get_full_name(self):
		return self.first_name + ' ' + self.last_name
	def get_is_active(self):
		return self.render_boolean(self.is_active)
	def get_email(self):
		return self.render_if(self.email)
	def get_phone(self):
		return self.render_if(self.phone)
	def get_extension(self):
		return self.render_if(self.extention)
	def get_groups(self):
		return self.render_list(self.groups, 'name')
	def get_all_permissions(self):
		if self.is_superuser:
			return Permission.objects.all()
		return self.user_permissions.all() | Permission.objects.filter(group__user=self)
	def get_available_permissions_pk(self):
		if self.is_superuser:
			myperms = Permission.objects.all()
		else:
			myperms = self.user_permissions.all() | Permission.objects.filter(group__user=self)
		myperms = myperms.filter(content_type__app_label__in=self.organization.get_modules_code())
		return myperms.values_list('pk', flat=True)
	############ INT ###############################################################
	def get_my_notifications(self):
		return apps.get_model('INT','Notification')().get_user_notifications(self)




########################################################################################
########################################################################################
VARS = {
	'NAME': 'Perfil',
	'PLURAL': 'Perfiles',
	'MODEL': 'Profile',
	'NEW': 'NUEVO',
	'NEW_GENDER': 'un nuevo',
	'THIS': 'este',
	'APP': APP,
	'QUERY': {
		'query': [
			(
				('organization', 'Organization.objects.get(pk=self.request.session.get("organization"))'),
				('active', 'True'),
			)
		],
	},
	'LIST': [
		{
			'field': 'name',
			'title': 'Nombre',
		},
		{
			'field': 'property_get_permissions',
			'title': 'Permisos',
			'width': 600,
			'template': '<div class="m--regular-font-size-sm5" style="line-height:15px;">{{property_get_permissions}}</div>',
		},
	],
	'SEARCH': ['name'],
	'SORTEABLE': ['name'],
	'SELECTQ': {
		'permissions': {
			'model': ['auth', 'Permission'],
			'order_by': '-id',
			'plugin': 'selectmultiple',
			'query': [
				(
					#('pk__in','self.request.user.get_available_permissions_pk()'),
					('content_type__app_label__in', 'Organization.objects.get(pk=self.request.session.get("organization")).get_modules_code()'),
				),
			],
		},
	},
}
class Profile(Group, Model_base):
	organization = models.ForeignKey('Organization', blank=True, null=True, on_delete=models.CASCADE, related_name='+',)
	VARS = VARS
	class Meta(Model_base.Meta):
		verbose_name = VARS['NAME']
		verbose_name_plural = VARS['PLURAL']
		permissions = permissions(VARS)
	def save(self, *args, **kwargs):
		self.name = self.name.upper()
		super().save()
	def get_permissions(self):
		return self.render_list(self.permissions, 'name')


########################################################################################
########################################################################################
VARS = {
	'NAME': 'Serie',
	'PLURAL': 'Series',
	'MODEL': 'Serial',
	'NEW': 'NUEVA',
	'NEW_GENDER': 'una nueva',
	'THIS': 'esta',
	'APP': APP,
	'EXCLUDE_PERMISSIONS': ['ALL'],
}
class Serial(Model_base):
	organization = models.ForeignKey('Organization', blank=True, null=True, on_delete=models.CASCADE, related_name='+',)
	name = models.CharField('Nombre con el que identificas la serie', max_length=120)
	content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
	serial = models.PositiveIntegerField(default=1)
	is_global = models.BooleanField('Serie compartida?', default=False)
	is_visible = models.BooleanField('Esta disponible?', default=False)
	VARS = VARS
	class Meta(Model_base.Meta):
		verbose_name = VARS['NAME']
		verbose_name_plural = VARS['PLURAL']
		permissions = permissions(VARS)
	def __str__(self):
		return '{0} [{1}]'.format(self.name, self.serial)
	#def assign(self):
		#self.serial += 1
		#self.save()
		#return self.serial - 1


########################################################################################
########################################################################################
VARS = {
	'NAME':'Producto o Servicio',
	'PLURAL':'Productos o servicios',
	'MODEL':'ProductsServicesSAT',
	'NEW':'NUEVO',
	'NEW_GENDER':'un nuevo',
	'THIS':'este',
	'APP':APP,
	'EXCLUDE_PERMISSIONS': ['ALL'],
}
class ProductsServicesSAT(Model_base):
	code = models.CharField('Código de producto o servicio',max_length=120)
	name = models.CharField('Nombre de producto o servicio',max_length=255)
	VARS = VARS
	class Meta(Model_base.Meta):
		verbose_name = VARS['NAME']
		verbose_name_plural = VARS['PLURAL']
		permissions = permissions(VARS)
	def __str__(self):
		return '{1} [{0}]'.format(self.code, self.name)


########################################################################################
########################################################################################
VARS = {
	'NAME':'Clave Unidad',
	'PLURAL': 'Clave de Unidades',
	'MODEL':'UnitsCodesSat',
	'NEW':'NUEVA',
	'NEW_GENDER': 'una nueva',
	'THIS':'esta',
	'APP':APP,
	'EXCLUDE_PERMISSIONS': ['ALL'],
}
class UnitsCodesSat(Model_base):
	code = models.CharField('Código de producto o servicio',max_length=120)
	name = models.CharField('Nombre de producto o servicio',max_length=255)
	class Meta(Model_base.Meta):
		verbose_name = VARS['NAME']
		verbose_name_plural = VARS['PLURAL']
		permissions = permissions(VARS)
	def __str__(self):
		return '{1} [{0}]'.format(self.code, self.name)

########################################################################################
########################################################################################
VARS = {
	'NAME':'DBConnection',
	'PLURAL':'DBConnection',
	'MODEL':'DBConnection',
	'NEW':'NUEVO',
	'NEW_GENDER': 'un nuevo',
	'THIS': 'este',
	'APP':APP,
	'EXCLUDE_PERMISSIONS':['ALL'],
}
class DBConnection(Model_base):
	organization = models.ForeignKey('mirari.Organization', on_delete=models.CASCADE, related_name='+',)
	name = models.CharField(max_length=250, blank=True, null=True)
	db_name = models.CharField(max_length=250, blank=True, null=True)
	db_host = models.CharField(max_length=250, blank=True, null=True)
	db_user = models.CharField(max_length=250, blank=True, null=True)
	db_password = models.CharField(max_length=250, blank=True, null=True)
	db_datatable = models.CharField(max_length=250, blank=True, null=True)
	VARS = VARS
	class Meta(Model_base.Meta):
		verbose_name = VARS['NAME']
		verbose_name_plural = VARS['PLURAL']
		permissions = permissions(VARS)
	def __str__(self):
		return '{0}'.format(self.name)

########################################################################################
########################################################################################
VARS = {
	'NAME':'HostEmail',
	'PLURAL':'HostEmail',
	'MODEL':'HostEmail',
	'NEW':'NUEVO',
	'NEW_GENDER': 'un nuevo',
	'THIS': 'este',
	'APP':APP,
	'EXCLUDE_PERMISSIONS':['ALL'],
}
class HostEmail(Model_base):
	company = models.ForeignKey('Organization', on_delete=models.CASCADE, related_name='+',)
	module = models.ForeignKey('Module', on_delete=models.CASCADE, related_name='+',)
	host = models.CharField(max_length=250)
	port = models.CharField(max_length=250, default='')
	username = models.CharField(max_length=250)
	password = models.CharField(max_length=250)
	email = models.CharField(max_length=250)
	prefix = models.CharField(max_length=250)
	is_available = models.BooleanField(default=True)
	default = models.BooleanField(default=False)
	VARS = VARS
	class Meta(Model_base.Meta):
		verbose_name = VARS['NAME']
		verbose_name_plural = VARS['PLURAL']
		permissions = permissions(VARS)
	def __str__(self):
		return '{0}'.format(self.module)
