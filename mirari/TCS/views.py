# -*- coding: utf-8 -*-
from mirari.mirari.views import *
from .models import *
from .vars import *	
import csv
from django.http import HttpResponse

from lxml.etree import Element, SubElement, tostring, XML, XMLParser, fromstring
from lxml import etree
from requests import Session
from requests.auth import HTTPBasicAuth
from zeep import Client, Plugin
from zeep.transports import Transport
import requests
import xmltodict


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
            orderServices = OrderService.objects.filter(creation_date__gt=start, creation_date__lt=end, active=True, organization=request.user.organization)
            if technical:
                orderServices = orderServices.filter(technical__id=technical)
            if company:
                orderServices = orderServices.filter(company__id=company)
            if store:
                orderServices = orderServices.filter(store__id=store)
            if modelo:
                orderServices = orderServices.filter(modelo__id=modelo)
            with open('OrderServiceReport.csv', 'w', newline='', encoding='latin1') as csvfile:
                filewriter = csv.writer(csvfile, delimiter=',', quoting=csv.QUOTE_ALL)
                filewriter.writerow([
                    'FOLIO', 
                    'TIPO SERVICIO',
                    'ESTATUS',
                    'ZONA',
                    'FECHA SERVICIO', 
                    'OPERADOR',
                    'TECNICO',
                    'COMPAÑIA',
                    'TIENDA',
                    'MARCA',
                    'MODELO',
                    'NUMERO DE SERIE',
                    'COMENTARIOS',
                    'COMENTARIOS',
                    'COMENTARIOS',
                    ])
                for orderService in orderServices:
                    filewriter.writerow([
                        orderService.serial, 
                        orderService.service,
                        orderService.status,
                        orderService.zone,
                        orderService.service_date, 
                        orderService.user.visible_username,
                        orderService.technical.visible_username,
                        orderService.company,
                        orderService.store,
                        orderService.brand,
                        orderService.modelo,
                        orderService.serial_number,
                        orderService.hidden_notes.replace(',',''),
                        orderService.order_notes.replace(',',''),
                        orderService.comments.replace(',',''),
                        ])
            return JsonResponse({'range':range_,'technical':technical,'company':company,'store':store,'modelo':modelo,'start':start,'end':end,'len':len(orderServices)})
        return super().dispatch(request, *args, **kwargs)


class OrderServiceReport__TemplateView(Generic__TemplateView):
    model = apps.get_model(APP, 'OrderServiceReport')
    template_name = "OrderServiceReport__CreateView.pug"
    ###########################################################################################
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        with open('OrderServiceReport.csv', 'r', newline='', encoding='latin1') as csvfile:
            response = HttpResponse(csvfile, content_type='text/csv')
            response['Content-Disposition'] = 'attachment; filename="OrderServiceReport.csv"'
            return response


class liverpoolTools__TemplateView(Generic__TemplateView):
    template_name = "liverpoolTools__TemplateView.html"
    model = apps.get_model('TCS', 'LiverpoolTools')
    #def dispatch(self, request, *args, **kwargs):
        #if self.request.GET.get('api'):
            #return self.model.APIRESPONSE(self.model, self)
        #return super().dispatch(request, *args, **kwargs)


class TCSapi__ApiView(Generic__ApiView):
    permissions = False
    @method_decorator(csrf_exempt)
    def get_serializers(self, request):
        if request.POST.get('getOrders'):
        return JsonResponse({'ok':'ok'}, safe=False)