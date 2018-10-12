# -*- coding: utf-8 -*-
from mirari.mirari.views import *
from .models import *
from .vars import *



###############################################################################################
###############################################################################################
######### Notification ########################################################################
class Notification__DetailView(Generic__DetailView):
	def get_object(self, *args, **kwargs):
		if kwargs['uuid'] == '404':
			raise Http404
		notification = self.model.objects.filter(uuid=kwargs['uuid']).first()
		if not self.request.user in notification.get_targets().all():
			raise Http404
		return notification
#######
	def initialize(self, request, *args, **kwargs):
		self.model = apps.get_model(APP, 'Notification')
		return True