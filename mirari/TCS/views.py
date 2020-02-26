# -*- coding: utf-8 -*-
from mirari.mirari.views import *
from .models import *
from .vars import *	

class calendar__OrderService__TemplateView(Generic__TemplateView):
    template_name = "calendarOrderService__TemplateView.pug"
    model = apps.get_model('TCS', 'OrderService')
    def dispatch(self, request, *args, **kwargs):
        if self.request.GET.get('api'):
            return self.model.APIRESPONSE(self.model, self)
        return super().dispatch(request, *args, **kwargs)

class manuales_usuario__OrderService__TemplateView(Generic__TemplateView):
    template_name = "manuales_usuario__OrderService__TemplateView.pug"
    model = apps.get_model('TCS', 'OrderService')

class manuales_iconfield__OrderService__TemplateView(Generic__TemplateView):
    template_name = "manuales_iconfield__OrderService__TemplateView.pug"
    model = apps.get_model('TCS', 'OrderService')
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

###############################################################################################
# OrderServiceReport ##########################################################################
###############################################################################################
class OrderServiceReport__TemplateView(Generic__TemplateView):
    model = apps.get_model(APP, 'OrderServiceReport')
    template_name = "OrderServiceReport__TemplateView.pug"
    ###########################################################################################
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)
    ###########################################################################################
    def proccess_context(self, context):
        #context['object'] = self.object
        return context