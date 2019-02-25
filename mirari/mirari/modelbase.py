# -*- encoding: utf-8 -*-
from django.contrib.auth.models import AbstractUser, Permission, Group
from django.contrib.sites.models import Site
from django.contrib.sites.managers import CurrentSiteManager
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey
from django.core.exceptions import PermissionDenied
from django.db import models, transaction
from django.db.models import Q
from django.db.models.signals import m2m_changed, post_save
from django.http import JsonResponse
from django_countries.fields import CountryField
from django.template.loader import get_template, render_to_string
from django.core.mail import EmailMultiAlternatives, get_connection
from django.dispatch import receiver
from django.utils.safestring import mark_safe
from django.utils.text import slugify
from django.conf import settings
from django.urls import reverse
from django.apps import apps

from crispy_forms.layout import *
from crispy_forms.bootstrap import *

from localflavor.mx.models import MXRFCField, MXZipCodeField, MXCURPField

from mptt.models import MPTTModel, TreeForeignKey

from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFill

from itertools import chain

from taggit.managers import TaggableManager

import datetime
import uuid
from itertools import chain

from .vars import *
from .taskapp import *

########################################################################################
## FUNCTIONS ###########################################################################
########################################################################################
def permissions(VARS):
	permissions = []
	if not 'EXCLUDE_PERMISSIONS' in VARS:
		exclude_permissions = []
	else:
		exclude_permissions = VARS['EXCLUDE_PERMISSIONS']
	if not 'all' in exclude_permissions:
		if not 'view' in exclude_permissions:
			permissions.append(('Can_View__'+VARS['MODEL'], 'Ve '+VARS['PLURAL'].lower()))
		if not 'create' in exclude_permissions:
			permissions.append(('Can_Create__'+VARS['MODEL'], 'Crea '+VARS['PLURAL'].lower()))
		if not 'update' in exclude_permissions:
			permissions.append(('Can_Update__'+VARS['MODEL'], 'Modifica '+VARS['PLURAL'].lower()))
		if not 'delete' in exclude_permissions:
			permissions.append(('Can_Delete__'+VARS['MODEL'], 'Elimina '+VARS['PLURAL'].lower()))
	if 'EXTEND_PERMISSIONS' in VARS:
		for permission in VARS['EXTEND_PERMISSIONS']:
			permissions.append(permission)
	return permissions



########################################################################################
########################################################################################
VARS = {
		'NAME': 'Model base',
		'PLURAL': 'Model base',
		'MODEL': 'Model_base',
		'NEW': '',
		'NEW_GENDER': '',
		'THIS': '',
		'APP': APP,
		'EXCLUDE_PERMISSIONS': ['all'],
	}
class Model_base(models.Model):
	active = models.BooleanField(default=True)
	VARS = VARS
	class Meta():
		default_permissions = []
		verbose_name = VARS['NAME']
		verbose_name_plural = VARS['PLURAL']
		permissions = permissions(VARS)
		abstract = True
		ordering = ['-id']
	def my_organization(self):
		try:
			return self.organization
		except:
			return None
	def natural_key(self):
		return self.str_obj()
	def exclude_permissions(self):
		if 'EXCLUDE_PERMISSIONS' in self.VARS:
			return self.VARS['EXCLUDE_PERMISSIONS']
		else:
			return []
	def add_text(self):
		return self.VARS['NEW']+" "+self.VARS['NAME'].upper(), "Agregar "+self.VARS['NAME'].lower(), "Agrega "+self.VARS['NEW_GENDER']+" "+self.VARS['NAME'].lower()+" al sistema"
	def edit_text(self):
		return "EDITAR "+self.VARS['NAME'].upper(), "Editar "+self.VARS['NAME'].lower(), "Edita los datos de "+self.VARS['THIS']+" "+self.VARS['NAME'].lower()+" al sistema"
	def delete_text(self):
		return "ELIMINAR " + self.VARS['NAME'].upper(), "Eliminar "+self.VARS['NAME'].lower(), "Elimina los datos de "+self.VARS['THIS']+" "+self.VARS['NAME'].lower(), "Se eliminará "+self.VARS['THIS']+" "+self.VARS['NAME'].lower()+" y todos sus datos asociados!"
	def url_list(self):
		return reverse('mirari:Generic__ListView', kwargs={'app': self.VARS['APP'], 'model': self.VARS['MODEL']})
	def url_add(self):
		if not 'create' in self.exclude_permissions():
			return reverse('mirari:Generic__CreateView', kwargs={'app': self.VARS['APP'], 'model': self.VARS['MODEL']})
		else:
			return None
	def url_update(self):
		if not 'update' in self.exclude_permissions():
			return reverse('mirari:Generic__UpdateView', kwargs={'app': self.VARS['APP'], 'model': self.VARS['MODEL'], 'pk': self.pk})
		else:
			return None
	def url_delete(self):
		if not 'delete' in self.exclude_permissions():
			return reverse('mirari:Generic__DeleteView', kwargs={'app': self.VARS['APP'], 'model': self.VARS['MODEL'], 'pk': self.pk})
		else:
			return None
	def url_detail(self):
		try:
			return reverse('mirari:Generic__DetailView', kwargs={'app': self.VARS['APP'], 'model': self.VARS['MODEL'], 'pk': self.pk})
		except:
			return None
	def str_obj(self):
		return str(self)
	def str_select2(self):
		return self.str_obj()
	def select2filter(self, query):
		return query
	###########
	def FORM_VALID(self, view, form):
		return form
	def EXTRA_RESPONSE(self, request):
		return False
	###########
	def render_boolean(self, field):
		if field:
			return '<i class="la la-check m--font-success"></i>'
		else:
			return '<i class="la la-times m--font-danger"></i>'
	def render_color(self, field):
		return '<i class="fa fa-circle" style="color:'+field+'"></i>'
	def render_list(self, list, attr):
		string = ''
		if not list.all():
			return '-'
		for l in list.all():
			string += getattr(l, attr) + ', '
		return string[0:len(string)-2]
	def render_if(self, attr):
		if not attr:
			return '-'
		return attr
	def render_string_color(self, field):
		if field:
			return 'success'
		else:
			return 'danger'
	def render_boolean_del(self, text, attr):
		if not attr:
			return '<s>{0}</s>'.format(text)
		return text
	#def render_ifnot_link(self, attr):
		#if not attr:
			#return '-'
		#return str(self.attr)
	def render_date(self, attr):
		return attr.strftime('%d/%m/%Y')
	def render_datetime(self, attr):
		return attr.strftime('%d/%m/%Y %I:%M %p')
	#def get_select2(self):
		#return self.name
	#def max_string(self, field, value):
		#string = getattr(self, field)[0:value]
		#if len(getattr(self, field)) > value:
			#string += '...'
		#return string
