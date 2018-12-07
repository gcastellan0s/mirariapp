# -*- coding: utf-8 -*-
from mirari.mirari.models import *
from .vars import *

VARS = {
	'NAME':'Tipo de credito',
	'PLURAL':'Tipos de credito',
	'MODEL':'CreditType',
	'NEW':'NUEVO',
	'NEW_GENDER': 'un nuevo',
	'THIS': 'este',
	'APP':APP,
}
class CreditType(Model_base):
	organization = models.ForeignKey('mirari.Organization', blank=True, null=True, on_delete=models.CASCADE, related_name='+',)
	name = models.CharField('Nombre', max_length=255)
	VARS = VARS
	class Meta(Model_base.Meta):
		verbose_name = VARS['NAME']
		verbose_name_plural = VARS['PLURAL']
		permissions = permissions(VARS)
	def __str__(self):
		return '{0}'.format(self.name)

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
	organization = models.ForeignKey('mirari.Organization', blank=True, null=True, on_delete=models.CASCADE, related_name='+',)
	name = models.CharField('Nombre', max_length=255)
	VARS = VARS
	class Meta(Model_base.Meta):
		verbose_name = VARS['NAME']
		verbose_name_plural = VARS['PLURAL']
		permissions = permissions(VARS)
	def __str__(self):
		return '{0}'.format(self.name)

VARS = {
	'NAME':'Persona',
	'PLURAL':'Personas',
	'MODEL':'Person',
	'NEW':'NUEVA',
	'NEW_GENDER': 'una nueva',
	'THIS': 'esta',
	'APP':APP,
}
class Person(Model_base):
	organization = models.ForeignKey('mirari.Organization', blank=True, null=True, on_delete=models.CASCADE, related_name='+',)
	first_name = models.CharField('Nombres', max_length=255)
	last_name = models.CharField('Apellidos', max_length=255)
	#rfc = models.CharField('Nombre', max_length=255)
	#.....
	VARS = VARS
	class Meta(Model_base.Meta):
		verbose_name = VARS['NAME']
		verbose_name_plural = VARS['PLURAL']
		permissions = permissions(VARS)
	def __str__(self):
		return '{0} {1}'.format(self.first_name, self.last_name)

VARS = {
	'NAME':'Credito',
	'PLURAL':'Creditos',
	'MODEL':'SIEBELCredit',
	'NEW':'NUEVO',
	'NEW_GENDER': 'un nuevo',
	'THIS': 'este',
	'APP':APP,
}
class SIEBELCredit(Model_base):
	organization = models.ForeignKey('mirari.Organization', blank=True, null=True, on_delete=models.CASCADE, related_name='+',)
	creditType = models.ForeignKey('CreditType', on_delete=models.PROTECT, related_name='+', verbose_name="Tipo de crédito")
	stage = models.CharField('Etapa del crédito', max_length=255, editable=False)
	#....
	VARS = VARS
	class Meta(Model_base.Meta):
		verbose_name = VARS['NAME']
		verbose_name_plural = VARS['PLURAL']
		permissions = permissions(VARS)
	def __str__(self):
		return '{0}'.format(self.id)

VARS = {
	'NAME':'CreditActor',
	'PLURAL':'CreditActor',
	'MODEL':'CreditActor',
	'NEW':'NUEVO',
	'NEW_GENDER': 'un nuevo',
	'THIS': 'este',
	'APP':APP,
}
class CreditActor(Model_base):
	actor = models.ForeignKey(Actor, on_delete=models.PROTECT, related_name='+')
	person = models.ForeignKey(Person, on_delete=models.PROTECT, related_name='+')
	credit = models.ForeignKey(SIEBELCredit, on_delete=models.PROTECT, related_name='+')
	#....
	VARS = VARS
	class Meta(Model_base.Meta):
		verbose_name = VARS['NAME']
		verbose_name_plural = VARS['PLURAL']
		permissions = permissions(VARS)
	def __str__(self):
		return '[{0}] {1} en {2}'.format(self.actor)