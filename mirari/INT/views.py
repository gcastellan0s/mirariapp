# -*- coding: utf-8 -*-
from mirari.mirari.views import *
from .models import *
from .vars import *


###############################################################################################
######### Notification ########################################################################
class Notification__DetailView(Generic__DetailView):
	template_name = 'Notification__DetailView.html'
	def get_object(self, *args, **kwargs):
		if self.uuid  == '404':
			raise Http404
		notification = self.model.objects.filter(uuid=self.uuid).first()
		if not notification.active:
			raise Http404
		if not self.request.user in notification.sended_to.all():
			raise Http404
		if notification.datetime_expire:
			if timezone.now() > notification.datetime_expire:
				raise Http404
		notification.readed_by.add(self.request.user)
		return notification
	def initialize(self, request, *args, **kwargs):
		self.model = apps.get_model(APP, 'Notification')
		self.uuid = kwargs['uuid']
		return True
	

###############################################################################################
###############################################################################################
######### Employee ############################################################################
class EmployeDirectory__ListView(Generic__ListView):
	model = apps.get_model('mirari', 'User')
	permissions = ['INT.Can_View__Team']
	verbose_name = 'EMPLEADO'
	verbose_name_plural = 'EMPLEADOS'
	LIST = [
			{
				'field': 'visible_username',
				'title': 'Usuario',
			},
			{
				'field': 'property_get_email',
				'title': 'Email',
			},
			{
				'field': 'property_get_phone',
				'title': 'EXT',
			},
			{
				'field': 'property_get_my_teams',
				'title': 'Equipo',
			},
			{
				'field': 'property_get_last_login',
				'title': 'Último Acceso',
			},
		]



###############################################################################################
###############################################################################################
######### DASHBOARD ###########################################################################
class InternalMailBox_Mail__CreateView(Generic__CreateView):
	def initialize(self, request, *args, **kwargs):
		self.model = apps.get_model(kwargs['app'], kwargs['model'])
		self.internalmailbox = apps.get_model(kwargs['app'], 'InternalMailBox').objects.get(pk=kwargs['pk'])
		return True
	def form_valid(self, form, *args, **kwargs):
		form.instance.internalmailbox = self.internalmailbox
		return super().form_valid(form)
	def get_success_url(self):	
		self.object.send_mail()
		return reverse('mirari:dashboard__Organization__TemplateView',)
	