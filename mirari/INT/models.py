# -*- coding: utf-8 -*-
from mirari.mirari.models import *
from .vars import *



########################################################################################
########################################################################################
VARS = {
	'NAME':'Catálogo',
	'PLURAL':'Catálogos',
	'MODEL':'Catalogue',
	'NEW':'NUEVO',
	'NEW_GENDER': 'un nuevo',
	'THIS': 'este',
	'APP':APP,
	'LIST': [
		{
			'field': 'code',
			'title': 'Código',
			'width': '50',
			'url': 'property_url_update'
		},
		{
			'field': 'name',
			'title': 'Nombre',
			'template': '{{property_get_name_with_color}}',
		},
		{
			'field': 'description',
			'title': 'Descripción',
			'template': '<div class="m--regular-font-size-sm5" style="line-height:15px;">{{property_get_description}}</div>',
		},
	],
	'SERIALIZER': ('get_description','get_name_with_color'),
	'SEARCH': ['name','code'],
	'SORTEABLE': ['code'],
	'SUMMERNOTE': ['description'],
}
class Catalogue(Model_base):
	organization = models.ForeignKey('mirari.Organization', blank=True, null=True, on_delete=models.CASCADE, related_name='+',)
	code = models.CharField('Código del documento', max_length=25, blank=True, null=True)
	name = models.CharField('Nombre del documento', max_length=500)
	description = models.TextField('Notas', max_length=500, blank=True, null=True)
	is_active = models.BooleanField('Esta activo?', default=True)
	VARS = VARS
	class Meta(Model_base.Meta):
		verbose_name = VARS['NAME']
		verbose_name_plural = VARS['PLURAL']
		permissions = permissions(VARS)
	def __str__(self):
		return '{0}'.format(self.name)
	def QUERY(self, view):
		if view.request.user.has_perm(self.model.VARS['APP']+'.Can_Update__'+self.model.VARS['MODEL']):
			return Catalogue.objects.filter(organization__pk=view.request.session.get('organization'), active=True)
		else:
			return Catalogue.objects.filter(organization__pk=view.request.session.get('organization'), is_active=True, active=True)
	def get_description(self):
		return self.render_if(self.description)
	def get_name_with_color(self):
		class_color = ''
		if not self.is_active:
			class_color = 'm--font-danger'
		return '<div class="{1}">{0}</div>'.format(self, class_color)
			


########################################################################################
########################################################################################
VARS = {
	'NAME':'Equipo',
	'PLURAL':'Equipos',
	'MODEL':'Team',
	'NEW':'NUEVO',
	'NEW_GENDER': 'un nuevo',
	'THIS': 'este',
	'APP':APP,
	'LIST': [
		{
			'field': 'name',
			'title': 'Nombre',
			'url': 'property_url_update',
			'width':'100',
		},
		{
			'field': 'property_get_members',
			'title': 'Miebros',
			'template': '<div class="m--regular-font-size-sm5" style="line-height:15px;">{{property_get_members}}</div>',
		},
	],
	'SERIALIZER': ('get_members',),
	'SEARCH': ['name'],
	'SORTEABLE': ['name'],
	'SELECTQ': {
		'members': {
			'plugin': 'select2',
		},
	},
}
class Team(Model_base):
	organization = models.ForeignKey('mirari.Organization', blank=True, null=True, on_delete=models.CASCADE, related_name='+',)
	name = models.CharField('Nombre', max_length=250)
	members = models.ManyToManyField('mirari.User', blank=True, related_name='+', verbose_name='Miembros de equipo')
	VARS = VARS
	class Meta(Model_base.Meta):
		verbose_name = VARS['NAME']
		verbose_name_plural = VARS['PLURAL']
		permissions = permissions(VARS)
	def __str__(self):
		return '{0}'.format(self.name)
	def get_members(self):
		return self.render_list(self.members, 'visible_username')


########################################################################################
########################################################################################
VARS = {
	'NAME':'Manual',
	'PLURAL':'Manuales',
	'MODEL':'Handbook',
	'NEW':'NUEVO',
	'NEW_GENDER': 'un nuevo',
	'THIS': 'este',
	'APP':APP,
	'LIST': [
		{
			'field': 'name',
			'title': 'Nombre',
			'template': 
				"""
					<span>
						<a href="{{file}}" target="_blank">
							{{property_get_name_with_color}}
						</a>
						<br />
						<small>
							{{property_get_notes}}
						</small>
					</span>
				""",
		},
	],
	'SEARCH': ['name'],
	'SORTEABLE': ['name'],
	'SERIALIZER': ['get_notes','get_name_with_color'],
}
def path_Handbook_file(self, filename):
	upload_to = "companys/%s_%s/INT/Handbook/%s" % (self.organization.id, self.organization.code, filename)
	return upload_to
class Handbook(Model_base):
	organization = models.ForeignKey('mirari.Organization', blank=True, null=True, on_delete=models.CASCADE, related_name='+',)
	name = models.CharField('Nombre', max_length=250)
	file = models.FileField('Archivo', upload_to=path_Handbook_file)
	notes = models.TextField('Notas', blank=True, null=True)
	is_active = models.BooleanField(default=True)
	creation_date = models.DateTimeField(auto_now_add=True)
	VARS = VARS
	class Meta(Model_base.Meta):
		verbose_name = VARS['NAME']
		verbose_name_plural = VARS['PLURAL']
		permissions = permissions(VARS)
	def __str__(self):
		return '{0}'.format(self.name)
	def QUERY(self, view):
		if view.request.user.has_perm(self.model.VARS['APP']+'.Can_Update__'+self.model.VARS['MODEL']):
			return Handbook.objects.filter(organization__pk=view.request.session.get('organization'), active=True)
		else:
			return Handbook.objects.filter(organization__pk=view.request.session.get('organization'), is_active=True, active=True)
	def get_notes(self):
		return self.render_if(self.notes)
	def get_name_with_color(self):
		class_color = ''
		if not self.is_active:
			class_color = 'm--font-danger'
		return '<div class="{1}">{0}</div>'.format(self, class_color)



########################################################################################
########################################################################################
VARS = {
	'NAME':'Canal de comunicación',
	'PLURAL':'Canales de comunicación',
	'MODEL':'Channel',
	'NEW':'NUEVO',
	'NEW_GENDER': 'un nuevo',
	'THIS': 'esta',
	'APP':APP,
	'LIST': [
		{
			'field': 'name',
			'title': 'Nombre',
		},
	],
	'SEARCH': ['title'],
	'SELECTQ': {
		'user_admin': {
			'model': ['mirari','User'],
			'plugin': 'selectmultiple',
		},
		'team_admin': {
			'model': ['INT','Team'],
			'plugin': 'selectmultiple',
		},
		'notify_user': {
			'model': ['mirari','User'],
			'plugin': 'selectmultiple',
		},
		'notify_team': {
			'model': ['INT','Team'],
			'plugin': 'selectmultiple',
		},
	},
	'SORTEABLE': ['name'],
}
class Channel(Model_base):
	organization = models.ForeignKey('mirari.Organization', on_delete=models.CASCADE, related_name='+')
	name = models.CharField('Nombre del canal', max_length=250)
	user_admin = models.ManyToManyField('mirari.User', blank=True, related_name='+', verbose_name='Lo administran usuarios')
	team_admin = models.ManyToManyField('Team', blank=True, related_name='+', verbose_name='Lo administran equipos')
	send_mail = models.BooleanField('Se notifica por mail?', default=True, help_text="Se notifica via mail a los destinatarios?")
	mandatory = models.BooleanField('Obligatorio?', default=True, help_text="Es obligatorio leerlo y se envian notificaciones constantes")
	notify_user = models.ManyToManyField('mirari.User', blank=True, related_name='+', verbose_name='Destinado a usuarios')
	notify_team = models.ManyToManyField('Team', blank=True, related_name='+', verbose_name='Destinado a equipos', help_text="Si el campo anterior y este estan vacios, se notificara a todos los equipos.")
	is_active = models.BooleanField('Canal activo', default=True)
	VARS = VARS
	class Meta(Model_base.Meta):
		verbose_name = VARS['NAME']
		verbose_name_plural = VARS['PLURAL']
		permissions = permissions(VARS)
	def __str__(self):
		return '{0}'.format(self.name)



#######################################################################################
#######################################################################################
VARS = {
	'NAME':'Notificación',
	'PLURAL':'Notificaciones',
	'MODEL':'Notification',
	'NEW':'NUEVA',
	'NEW_GENDER': 'una nueva',
	'THIS': 'esta',
	'APP':APP,
	'LIST': [
		{
			'field': 'name',
			'title': 'Nombre',
		},
	],
	'SEARCH': ['name'],
	'SELECTQ': {
		'channel': {
			'plugin': 'select2',
		},
		'readed_by': {
			'plugin': 'selectmultiple',
		},
	},
	'SORTEABLE': ['creation_date'],
	'SUMMERNOTE': ['message'],
	'DATE': ['datetime_expire'],
}
def path_Notification_file(self, filename):
	upload_to = "companys/%s_%s/INT/Notification/%s" % (self.organization.id, self.organization.code, filename)
	return upload_to
class Notification(Model_base):
	uuid = models.UUIDField(default=uuid.uuid4, editable=False)
	organization = models.ForeignKey('mirari.Organization', on_delete=models.CASCADE, related_name='+')
	channel = models.ForeignKey('Channel', on_delete=models.PROTECT, related_name='+', verbose_name="Canal(es) por donde envias")
	name = models.CharField('Nombre', max_length=250)
	message = models.TextField('Mensaje', max_length=500)
	files = models.FileField('Archivo(s) adjunto(s)', upload_to=path_Notification_file, blank=True, null=True)
	status = models.CharField('Estatus', max_length=250, choices=NOTIFICATION_STATUS, default='draft')
	datetime_expire = models.DateTimeField('Fecha de expiración', blank=True, null=True, help_text='Este mensaje expira?, dejalo vacio si no expira.')
	sended = models.BooleanField('Enviado?', default=False, help_text="Indica si esta notificación ya fue enviada.", editable=False)
	creation_date = models.DateTimeField(auto_now_add=True)
	readed_by = models.ManyToManyField('mirari.User', blank=True, related_name='+', verbose_name='Leido por...')
	VARS = VARS
	class Meta(Model_base.Meta):
		verbose_name = VARS['NAME']
		verbose_name_plural = VARS['PLURAL']
		permissions = permissions(VARS)
	def __str__(self):
		return '{0}'.format(self.name)
	def QUERY(self, view):
		#if view.request.user.is_superuser:
			#channel = Channel.objects.filter(organization__pk=view.request.session.get('organization'), is_active=True, active=True)
		#else:
		channel = Channel.objects.filter(Q(team_admin__members=view.request.user, is_active=True, active=True) | Q(user_admin=view.request.user, is_active=True, active=True))
		return Notification.objects.filter(channel__in=channel)
	def SELECTQ__channel(self, model=None, view=None):
		if not view and not model:
			return True
		if view.request.user.is_superuser:
			return model.objects.filter(organization__pk=view.request.session.get('organization'), is_active=True, active=True)
		else:
			return model.objects.filter(Q(team_admin__members=view.request.user, is_active=True, active=True) | Q(user_admin=view.request.user, is_active=True, active=True))
	#######		
	def get_user_notifications(self, user):
		return Notification.objects.all()