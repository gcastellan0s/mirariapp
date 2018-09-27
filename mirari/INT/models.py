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
		},
        {
			'field': 'get_is_active_',
			'title': 'Activo?',
		},
	],
	'SEARCH': ['name','code'],
	'SORTEABLE': ['code'],
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
		},
        #{
			#'field': 'get_leaders_',
			#'title': 'Líder(es)',
			#'width':'100',
		#},
	],
	'SEARCH': ['name'],
	'SORTEABLE': ['name'],
    'SELECTQ': {
		'members': {
			'model': ['mirari', 'User'],
			'order_by': '-id',
			'plugin': 'select2',
			#'query': [
				#(
					##('pk__in','self.request.user.get_available_permissions_pk()'),
					#('content_type__app_label__in', 'Organization.objects.get(pk=self.request.session.get("organization")).get_modules_code()'),
				#),
			#],
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
    #def get_members(self):
        #return self.render_list(self.members, 'full_name')


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
    'QUERY':{
        'query': [
            (
                ('is_active','True'),
            )
        ],
    },
	'LIST': [
		{
			'field': 'name',
			'title': 'Nombre',
            'template': 
                """
                    <span>
                        {{name}}<br />
                        <small>
                            {{property_get_notes}}
                        </small>
                    </span>
                """,
		},
	],
	'SEARCH': ['name'],
	'SORTEABLE': ['name'],
    'SERIALIZER': ['get_notes',],
}
def path_Handbook_file(self, filename):
    upload_to = "companys/%s_%s/INT/Handbook/%s" % (self.organization.id, self.organization.slug, filename)
    return upload_to
class Handbook(Model_base):
    organization = models.ForeignKey('mirari.Organization', blank=True, null=True, on_delete=models.CASCADE, related_name='+',)
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
    def get_notes(self):
        return self.render_if(self.notes)