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
	first_name = models.CharField('Nombre(s)', max_length=255, blank=True, null=True,)
	last_name = models.CharField('Apellido Paterno', max_length=255, blank=True, null=True,)
	mothers_last_name = models.CharField('Apellido Materno', max_length=255, blank=True, null=True,)
	birthday = models.DateField('Fecha nacimiento', blank=True, null=True)
	civil_status = models.CharField('Estado civil', max_length=255, blank=True, null=True,)
	gender = models.CharField('Género', choices=GENDER, max_length=255, blank=True, null=True,)
	occupation = models.CharField('Ocupación', max_length=255, blank=True, null=True,)
	rfc = MXRFCField('RFC', blank=True, null=True,)
	curp = MXCURPField('CURP', blank=True, null=True,)
	business_activity = models.CharField('Actividad empresarial', choices=PERSON_TYPE, max_length=255, blank=True, null=True,)
	contact1 = models.CharField('Contacto', max_length=255, blank=True, null=True,)
	contact2 = models.CharField('Contacto', max_length=255, blank=True, null=True,)
	contact3 = models.CharField('Contacto', max_length=255, blank=True, null=True,)
	email =  models.CharField('Contacto', max_length=255, blank=True, null=True,)
	VARS = VARS
	class Meta(Model_base.Meta):
		verbose_name = VARS['NAME']
		verbose_name_plural = VARS['PLURAL']
		permissions = permissions(VARS)
	def __str__(self):
		return '{0} {1}'.format(self.first_name, self.last_name)


VARS = {
	'NAME':'Empresa',
	'PLURAL':'Empresas',
	'MODEL':'Company',
	'NEW':'NUEVA',
	'NEW_GENDER': 'una nueva',
	'THIS': 'esta',
	'APP':APP,
}
class Company(Model_base):
	organization = models.ForeignKey('mirari.Organization', blank=True, null=True, on_delete=models.CASCADE, related_name='+',)
	name = models.CharField('Nombre', max_length=255, blank=True, null=True,)
	legal_representative = models.CharField('Nombre del representante legal de la empresa', max_length=255, blank=True, null=True,)
	contact_representative = models.CharField('Nombre del contacto en la empresa', max_length=255, blank=True, null=True,)
	rfc = MXRFCField('RFC', blank=True, null=True,)
	type_company = models.CharField('Tipo de empresa', choices=COMPANY_TYPE, max_length=255, blank=True, null=True,)
	business_activity = models.CharField('Actividad empresarial', choices=COMPANY_ACTIVITY, max_length=255, blank=True, null=True,)
	parent = models.ForeignKey('Company', verbose_name="Depende de:", blank=True, null=True, on_delete=models.CASCADE, related_name='+',)
	contact1 = models.CharField('Contacto', max_length=255, blank=True, null=True,)
	contact2 = models.CharField('Contacto', max_length=255, blank=True, null=True,)
	contact3 = models.CharField('Contacto', max_length=255, blank=True, null=True,)
	email =  models.CharField('Email', max_length=255, blank=True, null=True,)
	address = models.CharField('Dirección', max_length=255, blank=True, null=True,)
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
	'MODEL':'SBCredit',
	'NEW':'NUEVO',
	'NEW_GENDER': 'un nuevo',
	'THIS': 'este',
	'APP':APP,
}
class SBCredit(Model_base):
	organization = models.ForeignKey('mirari.Organization', blank=True, null=True, on_delete=models.CASCADE, related_name='+',)
	creditType = models.ForeignKey('CreditType', on_delete=models.PROTECT, related_name='+', verbose_name="Tipo de crédito")
	stage = models.CharField('Etapa del crédito', max_length=255)
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
	person = models.ForeignKey(Person, on_delete=models.PROTECT, related_name='+', blank=True, null=True)
	company = models.ForeignKey(Company, on_delete=models.PROTECT, related_name='+', blank=True, null=True)
	credit = models.ForeignKey(SBCredit, on_delete=models.PROTECT, related_name='+')
	VARS = VARS
	class Meta(Model_base.Meta):
		verbose_name = VARS['NAME']
		verbose_name_plural = VARS['PLURAL']
		permissions = permissions(VARS)
	def __str__(self):
		return '[{0}] {1} en {2}'.format(self.actor)