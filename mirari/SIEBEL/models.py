# -*- coding: utf-8 -*-
from mirari.mirari.models import *
from .vars import *

VARS = {
	'NAME':'Credito',
	'PLURAL':'Credito',
	'MODEL':'Credit',
	'NEW':'NUEVO',
	'NEW_GENDER': 'un nuevo',
	'THIS': 'este',
	'APP':APP,
}
class Credit(Model_base):
	VARS = VARS
	name = models.CharField(max_length=255)
	class Meta(Model_base.Meta):
		verbose_name = VARS['NAME']
		verbose_name_plural = VARS['PLURAL']
		permissions = permissions(VARS)
	def __str__(self):
		return '{0}'.format(self.VARS['NAME'])

VARS = {
	'NAME':'Actor',
	'PLURAL':'Actores',
	'MODEL':'Actor',
	'NEW':'NUEVO',
	'NEW_GENDER': 'un nuevo',
	'THIS': 'este',
	'APP':APP,
}
class Actor(Model_base):
	name = models.CharField(max_length=255)
	VARS = VARS
	class Meta(Model_base.Meta):
		verbose_name = VARS['NAME']
		verbose_name_plural = VARS['PLURAL']
		permissions = permissions(VARS)
	def __str__(self):
		return '{0}'.format(self.VARS['NAME'])