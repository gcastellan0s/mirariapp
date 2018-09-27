# -*- coding: utf-8 -*-
from mirari.mirari.models import *
from .vars import *

########################################################################################
########################################################################################
VARS = {
	'NAME':'Notificación PLD',
	'PLURAL':'Notificaciones PLD',
	'MODEL':'PLDNotifications',
	'NEW':'NUEVA',
	'NEW_GENDER': 'una nueva',
	'THIS': 'esta',
	'APP':APP,
	'LIST': [
		{
			'field': 'title',
			'title': 'Titulo',
		},
	],
	'SEARCH': ['title'],
    'SELECTQ': {
		'readed_by': {
			'model': ['mirari', 'User'],
			'order_by': '-id',
			'plugin': 'selectmultiple',
		},
	},
    'SORTEABLE': ['creation_date'],
}
def path_PLDNotifications_file(self, filename):
    upload_to = "companys/%s_%s/CRYE/PLDNotifications/%s" % (self.organization.id, self.organization.slug, filename)
    return upload_to
class PLDNotifications(Model_base):
    organization = models.ForeignKey('mirari.Organization', on_delete=models.CASCADE, related_name='+')
    title = models.CharField('Titulo', max_length=250)
    description = models.TextField('Notas', max_length=500)
    file = models.FileField('Archivo adjunto', upload_to=path_PLDNotifications_file, blank=True, null=True)
    is_active = models.BooleanField('Esta activo?', default=True)
    readed_by = models.ManyToManyField('mirari.User', blank=True, related_name='+', verbose_name='Leido por...')
    creation_date = models.DateTimeField(auto_now_add=True)
    VARS = VARS
    class Meta(Model_base.Meta):
        verbose_name = VARS['NAME']
        verbose_name_plural = VARS['PLURAL']
        permissions = permissions(VARS)
    def __str__(self):
        return '{0}'.format(self.title)