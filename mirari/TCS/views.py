# -*- coding: utf-8 -*-
from mirari.mirari.views import *
from .models import *
from .vars import *	



class calendar__OrderService__TemplateView(Generic__TemplateView):
	template_name = "calendar__OrderService__TemplateView.html"
	model = apps.get_model('TCS', 'OrderService')
	def dispatch(self, request, *args, **kwargs):
		if self.request.GET.get('get_calendar'):
			extra = self.model.EXTRA_RESPONSE(self, request)
			if extra:
				return extra
		return super().dispatch(request, *args, **kwargs)



class manuales_usuario__OrderService__TemplateView(Generic__TemplateView):
	template_name = "manuales_usuario__OrderService__TemplateView.html"
	model = apps.get_model('TCS', 'OrderService')
	


class manuales_iconfield__OrderService__TemplateView(Generic__TemplateView):
	template_name = "manuales_iconfield__OrderService__TemplateView.html"
	model = apps.get_model('TCS', 'OrderService')
	