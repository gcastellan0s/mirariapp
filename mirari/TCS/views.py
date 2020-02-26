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
        pass
        #self.object = WalletCredit.objects.get(id=kwargs['pk'])
        #if request.method == 'POST':
            #if request.GET.get('api') == 'addPayment':
                #tablaAmortizacion = TablaAmortizacion.objects.get(id=request.POST.get('tablaAmortizacion'))
                #pagoAmortizacion = PagoAmortizacion()
                #pagoAmortizacion.user = request.user
                #pagoAmortizacion.tablaaAmortizacion = tablaAmortizacion
                #pagoAmortizacion.capital = request.POST.get('capital', 0)
                #pagoAmortizacion.interesVigente = request.POST.get('interesVigente', 0)
                #pagoAmortizacion.intereVigenteNoPagado = request.POST.get('intereVigenteNoPagado', 0)
                #pagoAmortizacion.interesMoratorio = request.POST.get('interesMoratorio', 0)
                #pagoAmortizacion.gastosCobranza = request.POST.get('gastosCobranza', 0)
                #pagoAmortizacion.iva = request.POST.get('iva', 0)
                #pagoAmortizacion.save()
                #return JsonResponse({
                    #'walletcredit': WalletCreditSerializer(self.object).data,
                    #'tablasamortizaciones': TablaAmortizacionSerializer(TablaAmortizacion.objects.filter(walletcredit=self.object), many=True).data,
                    #'pagosamortizacion': PagoAmortizacionSerializer(PagoAmortizacion.objects.filter(tablaaAmortizacion=tablaAmortizacion), many=True).data,
                #})
            #if request.GET.get('api') == 'getPagosAmortizacion':
                #tablaAmortizacion = TablaAmortizacion.objects.get(id=request.POST.get('tablaAmortizacion'))
                #return JsonResponse({
                    #'pagosamortizacion': PagoAmortizacionSerializer(PagoAmortizacion.objects.filter(tablaaAmortizacion=tablaAmortizacion), many=True).data,
                #})
            #if request.GET.get('api') == 'getTable':
                #return JsonResponse({
                    #'walletcredit': WalletCreditSerializer(self.object).data,
                    #'tablasamortizaciones': TablaAmortizacionSerializer(TablaAmortizacion.objects.filter(walletcredit=self.object), many=True).data,
                #})
        #return super().dispatch(request, *args, **kwargs)
    ###########################################################################################
    def proccess_context(self, context):
        context['object'] = self.object
        return context