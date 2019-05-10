# -*- coding: utf-8 -*-
from django import template
from mirari.mirari.vars import *
from mirari.mirari.models import *
from django.conf import settings
import re

register = template.Library()

@register.filter
def verbose_name_singular(obj):
	return obj._meta.verbose_name

@register.filter
def verbose_name_plural(obj):
	return obj._meta.verbose_name_plural

@register.filter
def get_menu(obj):
	return sorted(MMENU.items(), reverse=True)

@register.filter
def has_app(request, apps):
	organization = Organization.objects.get(pk=request.session.get('organization'))
	for app in apps:
		if Module.objects.get(code=app) in organization.modules.all():
			return True
	return False

@register.filter
def has_app_code(request, code_app):
	organization = Organization.objects.get(pk=request.session.get('organization'))
	if Module.objects.get(code=code_app) in organization.modules.all():
		return True
	return False

@register.filter
def has_permission(request, module):
	model = module['model'].split('.')
	if 'permission_' in module:
		return request.user.has_perm(model[0]+'.'+module['permission_'])
	if not module['permission']:
		return True
	return request.user.has_perm(model[0]+'.'+module['permission']+'__'+model[1])

@register.filter
def get_url(module):
	if 'url' in module:
		app, model = module['model'].split('.')
		if 'Generic__' in module['url']:
			return reverse('mirari:'+module['url'], kwargs={'app':app,'model':model})
		else:
			return reverse(app+':'+module['url'], kwargs={'app':app,'model':model})
	elif 'href' in module:
		return reverse(module['href'])
	elif 'link' in module:
		return module['link']
	else:
		return '#@'

@register.filter
def prepend_perm(perm, model):
	return model['APP']+'.'+perm+model['MODEL']

@register.filter
def if_has_perm(perm, request):
	if request.user.has_perm(perm):
		return True
	return False

@register.filter
def renderDataTable(obj):
	return mark_safe(obj.replace('{{','${row.').replace('}}','}'))

@register.filter
def get_session_organization(request):
	return Organization.objects.filter(pk=request.session['organization']).first()
