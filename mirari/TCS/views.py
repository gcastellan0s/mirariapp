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
class OrderServiceReport__CreateView(Generic__CreateView):
    model = apps.get_model(APP, 'OrderServiceReport')
    template_name = "OrderServiceReport__CreateView.pug"
    ###########################################################################################
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        message, api = 'Hay un error en tu consulta', 'error' 
        if request.method == 'POST':
            range_ = request.POST.get('range').split(" / ", 1)
            start = datetime.datetime.strptime(range_[0], '%d/%m/%Y')
            end = datetime.datetime.strptime(range_[1], '%d/%m/%Y')
            technical = request.POST.get('technical')
            company = request.POST.get('company')
            store = request.POST.get('store')
            modelo = request.POST.get('modelo')
            orderService = OrderService.objects.filter(creation_date__gt=start, creation_date__lt=end, active=True)
            return JsonResponse({'range':range_,'technical':technical,'company':company,'store':store,'modelo':modelo,'start':start,'end':end,'len':len(orderService)})
        return super().dispatch(request, *args, **kwargs)