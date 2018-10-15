# -*- coding: utf-8 -*-
from mirari.mirari.views import *
from .models import *
from .vars import *


###############################################################################################
###############################################################################################
######### Notification ########################################################################
class Notification__DetailView(Generic__DetailView):
	template_name = 'Notification__DetailView.html'
	def get_object(self, *args, **kwargs):
		if self.uuid  == '404':
			raise Http404
		notification = self.model.objects.filter(uuid=self.uuid).first()
		if not self.request.user in notification.get_targets().all():
			raise Http404
		if notification.datetime_expire:
			if timezone.now() > notification.datetime_expire:
				raise Http404
		return notification
#######
	def initialize(self, request, *args, **kwargs):
		self.model = apps.get_model(APP, 'Notification')
		self.uuid = kwargs['uuid']
		return True