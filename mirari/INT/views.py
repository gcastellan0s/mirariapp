# -*- coding: utf-8 -*-
from mirari.mirari.views import *
from .models import *
from .vars import *

###############################################################################################
###############################################################################################
######### Notification ########################################################################
class Notification__DetailView(Generic__DetailView):
	def get_object(self):
		return self.model.objects.filter(uuid=kwargs['uuid']).first()
#######
	def initialize(self, request, *args, **kwargs):
		self.model = apps.get_model(kwargs['app'], 'Notification')
		return True
		