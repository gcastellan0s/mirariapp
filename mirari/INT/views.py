# -*- coding: utf-8 -*-
from mirari.mirari.views import *
from .models import *
from .vars import *

###############################################################################################
###############################################################################################
######### Notification ########################################################################
class Notification__TemplateView(Generic__TemplateView):
	template_name = "Notification__TemplateView.html"
	def initialize(self, request, *args, **kwargs):
		self.model = apps.get_model(kwargs['app'], 'Notification')
		self.object = Notification.objects.get(uuid=kwargs['uuid'])
		return True
	def proccess_context(self, context, *args, **kwargs):
		context['object'] = Notification.objects.all()[0]
		return context