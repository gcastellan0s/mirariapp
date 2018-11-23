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
		#{
			#'field': 'code',
			#'title': 'Código',
			#'width': '50',
			#'url': 'property_url_update'
		#},
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
			return Catalogue.objects.filter(organization__pk=view.request.session.get('organization'), active=True).order_by('name')
		else:
			return Catalogue.objects.filter(organization__pk=view.request.session.get('organization'), is_active=True, active=True).order_by('name')
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
			'width':'200',
		},
		{
			'field': 'property_get_code',
			'title': 'Código',
			'width':'200',
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
	code = models.CharField('Código', max_length=250, blank=True, null=True)
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
	def get_user_team(self, user):
		return Team.objects.filter(members=user)
	def get_code(self):
		return self.render_if(self.code)


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
					<a href="{{file}}" target="_blank">
						{{property_get_name_with_color}}
					</a>
				""",
		},
		{
			'field': 'notes',
			'title': 'Notas',
			'template': 
				"""
						<small>
							{{property_get_notes}}
						</small>
				""",
		},
	],
	'SEARCH': ['name'],
	'SORTEABLE': ['name'],
	'SUMMERNOTE': ['notes'],
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
		return '<div class="{1}"><i class="fa fa-cloud-download-alt m--regular-font-size-sm2"></i> {0}</div>'.format(self, class_color)



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
		{
			'field': 'property_get_audience',
			'title': 'Audiencia',
		},
		{
			'field': 'property_get_list_administrators',
			'title': 'Administradores',
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
	def get_targets(self):
		users = []
		for team in self.notify_team.all():
			for member in team.members.all():
				if not member in users:
					users.append(member.pk)
		return (User.objects.filter(pk__in=users).all() | self.notify_user.all()).distinct()
	def get_audience(self):
		return len(self.get_targets())
	def get_list_administrators(self):
		users = []
		for team in self.team_admin.all():
			for member in team.members.all():
				if not member in users:
					users.append(member.pk)
		return self.render_list((User.objects.filter(pk__in=users).all() | self.user_admin.all()).distinct(), 'visible_username')



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
			'field': 'title',
			'title': 'Título',
		},
		{
			'field': 'property_get_channel',
			'title': 'Canal',
		},
		{
			'field': 'property_get_creation_date',
			'title': 'Creado',
		},
		{
			'field': 'property_get_expiration_date',
			'title': 'Expira',
		},
		{
			'field': 'property_get_status',
			'title': 'Estatus',
		},
	],
	'FORM': ('channel','title','message','files','status','datetime_expire','hide_content',),
	'SEARCH': ['name'],
	'SELECTQ': {
		'channel': {
			'plugin': 'select2',
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
	uuid = models.UUIDField(default=uuid.uuid4)
	organization = models.ForeignKey('mirari.Organization', on_delete=models.CASCADE, related_name='+')
	channel = models.ForeignKey('Channel', on_delete=models.PROTECT, related_name='+', verbose_name="Canal(es) por donde envias")
	title = models.CharField('Título', max_length=250)
	message = models.TextField('Mensaje')
	files = models.FileField('Archivo(s) adjunto(s)', upload_to=path_Notification_file, blank=True, null=True)
	status = models.CharField('Estatus', max_length=250, choices=NOTIFICATION_STATUS, default='Borrador')
	datetime_expire = models.DateTimeField('Fecha de expiración', blank=True, null=True, help_text='Este mensaje expira?, dejalo vacio si no expira.')
	sended = models.BooleanField('Enviado?', default=False, help_text="Indica si esta notificación ya fue enviada.")
	creation_date = models.DateTimeField(auto_now_add=True)
	craeted_by = models.ForeignKey('mirari.User', on_delete=models.SET_NULL, blank=True, null=True, related_name='+', verbose_name="Canal(es) por donde envias")
	sended_to = models.ManyToManyField('mirari.User', blank=True, related_name='+', verbose_name='Enviado a...')
	readed_by = models.ManyToManyField('mirari.User', blank=True, related_name='+', verbose_name='Leido por...')
	hide_content = models.BooleanField('Ocultar contenido?', default=True, help_text="Si ocultas el contenido el usuario deberá ingresar usuario y contraseña para ver el contenido.")
	VARS = VARS
	class Meta(Model_base.Meta):
		verbose_name = VARS['NAME']
		verbose_name_plural = VARS['PLURAL']
		permissions = permissions(VARS)
	def __str__(self):
		return '{0}'.format(self.title)
	def QUERY(self, view):
		if view.request.user.is_superuser:
			channel = Channel.objects.filter(organization__pk=view.request.session.get('organization'), is_active=True, active=True)
		else:
			channel = Channel.objects.filter(Q(team_admin__members=view.request.user, is_active=True, active=True) | Q(user_admin=view.request.user, is_active=True, active=True))
		return Notification.objects.filter(Q(channel__in=channel, datetime_expire__isnull=True, active=True, is_active=True)|Q(channel__in=channel, datetime_expire__gt=datetime.datetime.now(), active=True, is_active=True))
	def SELECTQ__channel(self, model=None, view=None):
		if view.request.user.is_superuser:
			query = model.objects.filter(organization__pk=view.request.session.get('organization'), is_active=True, active=True)
		else:
			query = model.objects.filter(Q(team_admin__members=view.request.user, is_active=True, active=True) | Q(user_admin=view.request.user, is_active=True, active=True))
		return query
	def url_detail(self):
		return reverse('INT:Notification__DetailView', kwargs={'uuid':self.uuid,})
	def url_update(self):
		if self.sended:
			return '#'
		if not 'update' in self.exclude_permissions():
			return reverse('mirari:Generic__UpdateView', kwargs={'app': self.VARS['APP'], 'model': self.VARS['MODEL'], 'pk': self.pk})
		else:
			return None
	#######		
	def get_user_notifications(self, user):
		return Notification.objects.all()
	def get_channel(self):
		return str(self.channel)
	def get_creation_date(self):
		return self.render_datetime(self.creation_date)
	def get_expiration_date(self):
		if self.datetime_expire:
			return self.render_datetime(self.datetime_expire)
		return '-'
	def get_sended(self):
		return self.render_boolean(self.sended)
	def get_status(self):
		return self.status
	def send_notifications(self):
		reminders = self.channel
		return True
	def get_targets(self):
		return self.channel.get_targets()
	def get_user_notification(self, user):
		return 	Notification.objects.filter(sended_to = user)[0:50]
	def send_mail(self):
		email_host = HostEmail.objects.filter(module__code=APP, company=self.organization).first()
		connection = get_connection(host=email_host.host , port=email_host.port, username=email_host.username, password=email_host.password, use_tls=True)
		connection.open()
		for target in self.get_targets():
			if target.email:
				context = {
					'notification': self,
					'destinatary': target
				}
				template = render_to_string('email/default/base_email.html', context)
				msg = EmailMultiAlternatives(
					subject=self.title,
					body=template,
					from_email=email_host.prefix +'<'+email_host.email+'>', 
					to=[target.email],
					connection=connection
				)
				msg.attach_alternative(template, "text/html")
				msg.send(True)
		transaction.on_commit(
			lambda: self.sended_to.add(*self.get_targets())
		)
		connection.close()
		return True

@receiver(post_save, sender=Notification)
def notification_post_save(sender, instance=None, created=None, **kwargs):
	if instance.sended == False and instance.status == 'Publicado':
		instance.sended = True
		instance.save()
		send_mail_task.delay(app='INT', model='Notification', pk=instance.pk)