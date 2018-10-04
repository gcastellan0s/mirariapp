# -*- coding: utf-8 -*-
from mirari.mirari.models import *
from .vars import *

VARS = {
	'NAME':'Desbloqueo Siebel',
	'PLURAL':'Desbloqueo Siebel',
	'MODEL':'SiebelUnblock',
	'NEW':'NUEVO',
	'NEW_GENDER': 'un nuevo',
	'THIS': 'este',
	'APP':APP,
	'EXCLUDE_PERMISSIONS':['create','update','delete',],
}
class SiebelUnblock(Model_base):
    VARS = VARS
    class Meta(Model_base.Meta):
        verbose_name = VARS['NAME']
        verbose_name_plural = VARS['PLURAL']
        permissions = permissions(VARS)
    def __str__(self):
        return '{0}'.format(self.VARS['NAME'])