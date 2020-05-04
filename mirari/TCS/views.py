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

        class my_plugin(Plugin):
            def egress(self, envelope, http_headers, operation, binding_options):	
                xmlString = tostring(envelope, encoding='unicode')	
                xmlString = xmlString.replace("&lt;", "<")	
                xmlString = xmlString.replace("&gt;", ">")	
                xmlString = xmlString.replace("&amp;", "&")	
                parser = XMLParser(strip_cdata=False)	
                newenvelope = XML(xmlString, parser=parser)	
                return newenvelope, http_headers

        if request.POST.get('getOrders'):
            nscus = 'http://siebel.com/CustomUI'	
            archive = Element('{%s}LVP_spcConsulta_spcSR_Input' % nscus, nsmap={'cus': nscus})	
            subelement = SubElement(archive, '{%s}strUsuario' % nscus)	
            subelement.text = 'PROVEEDOR24'	
            subelement = SubElement(archive, '{%s}strFechaInicio' % nscus)	
            subelement.text = ''	
            request_data = {	
                'operacion': 'CSR',	
                'archivo': '<![CDATA['+tostring(archive).decode("utf-8")+']]>',	
            }	
            client = Client('http://srproveedores.liverpool.com.mx/wbi/AltaTicket?wsdl', plugins=[my_plugin()])	
            node = client.create_message(client.service, 'AltaOperation', **request_data)	
            with open('./xml/TCS/CSR.xml', 'wb') as f:	
                f.write(tostring(node, pretty_print=True))	
            headers = {	
                'Content-Type': 'text/xml',	
                'SOAPAction': '"http://www.example.org/wbi/AltaOperation"',	
            }	
            data = open('./xml/TCS/CSR.xml', 'rb').read()	
            response = requests.post('https://srproveedoresqa.liverpool.com.mx/wbi/AltaTicket', headers=headers, data=data)	
            orders = [] 	
            if (str(response) == '<Response [200]>'):	
                xml = xmltodict.parse(xmltodict.parse(response.text.encode())['soapenv:Envelope']['soapenv:Body']['NS1:TransferenciaResponse']['NS1:archivo'])	
                xml = xml['ns:LVP_spcConsulta_spcSR_Output']['ListOfLvpServiceRequestIo']['LvpServiceRequestCustom']	
                for order in xml:	
                    if not OrderService.objects.filter(serialLiverpool = order['SRId']):	
                        orderService = OrderService()	
                        orderService.serialLiverpool = order['SRId']	
                        orderService.organization = Organization.objects.filter(pk=3).first()	
                        orderService.user = User.objects.filter(pk=656).first()	
                        orderService.delivery_date = datetime.datetime.strptime(order['ShipDate'], "%d/%m/%Y").date()	
                        orderService.client_name = order['ContactFirstName'] + ' ' + order['ContactLastName']	
                        orderService.email = order['LVPContacteMail']	
                        orderService.contact_phone1 = order['LVPContactPhone']	
                        orderService.address = order['LVPStreetAddress']	
                        orderService.colony = order['LVPProvince']	
                        orderService.city = order['LVPCity'] + ' ' + order['LVPState']	
                        orderService.cp = order['LVPPostalCode']	
                        orderService.client_notes = order['Abstract'] + ' || Area: ' + order['INSArea'] + ' || SubArea: ' + order['INSSub-Area'] + ' || Tipo: ' + order['LVPType4thLevel']	
                        orderService.company = Company.objects.filter(pk=37).first()	
                        orderService.companyName = 'liverpool'	
                        orderService.report_name = order['LVPCreatedBy']	
                        orderService.serial_number = order['SerialNumber']	
                        orderService.order_notes = 'Modelo: ' + order['LVPAssetModel']	
                        orderService.save()	
                    orders.append(order['SRId'])	
            return JsonResponse({'OrderServices':OrderServiceSerializer(OrderService.objects.filter(serialLiverpool__in=orders), many=True).data}, safe=False)
            
        if request.POST.get('activitiesNotesLiverpool'):
            nscus = 'http://siebel.com/CustomUI'	
            archive = Element('{%s}LVP_spcConsulta_spcActividades_Input' % nscus, nsmap={'cus': nscus})	
            subelement = SubElement(archive, '{%s}Object_spcId' % nscus)	
            subelement.text = request.POST.get('activitiesNotesLiverpool')
            request_data = {	
                'operacion': 'CASP',	
                'archivo': '<![CDATA['+tostring(archive).decode("utf-8")+']]>',	
            }	
            client = Client('http://srproveedores.liverpool.com.mx/wbi/AltaTicket?wsdl', plugins=[my_plugin()])	
            node = client.create_message(client.service, 'AltaOperation', **request_data)	
            with open('./xml/TCS/CASP.xml', 'wb') as f:	
                f.write(tostring(node, pretty_print=True))	
            headers = {	
                'Content-Type': 'text/xml',	
                'SOAPAction': '"http://www.example.org/wbi/AltaOperation"',	
            }	
            data = open('./xml/TCS/CASP.xml', 'rb').read()	
            response = requests.post('https://srproveedoresqa.liverpool.com.mx/wbi/AltaTicket', headers=headers, data=data)
            xml = xmltodict.parse(xmltodict.parse(response.text.encode())['soapenv:Envelope']['soapenv:Body']['NS1:TransferenciaResponse']['NS1:archivo'])
            activitiesxml = xml['ns:LVP_spcConsulta_spcActividades_Output']['ListOfLvpSrActionIo']['LvpServiceRequestCustom']['ListOfLvpServiceRequestAction']['LvpServiceRequestAction']
            ########################
            nscus = 'http://siebel.com/CustomUI'	
            archive = Element('{%s}LVP_spcConsulta_spcNotas_Input' % nscus, nsmap={'cus': nscus})	
            subelement = SubElement(archive, '{%s}Object_spcId' % nscus)	
            subelement.text = request.POST.get('activitiesNotesLiverpool')
            request_data = {	
                'operacion': 'CN',	
                'archivo': '<![CDATA['+tostring(archive).decode("utf-8")+']]>',	
            }	
            client = Client('http://srproveedores.liverpool.com.mx/wbi/AltaTicket?wsdl', plugins=[my_plugin()])	
            node = client.create_message(client.service, 'AltaOperation', **request_data)	
            with open('./xml/TCS/CN.xml', 'wb') as f:	
                f.write(tostring(node, pretty_print=True))	
            headers = {	
                'Content-Type': 'text/xml',	
                'SOAPAction': '"http://www.example.org/wbi/AltaOperation"',	
            }	
            data = open('./xml/TCS/CN.xml', 'rb').read()	
            response = requests.post('https://srproveedoresqa.liverpool.com.mx/wbi/AltaTicket', headers=headers, data=data)
            xml = xmltodict.parse(xmltodict.parse(response.text.encode())['soapenv:Envelope']['soapenv:Body']['NS1:TransferenciaResponse']['NS1:archivo'])
            notesxml = xml['ns:LVP_spcConsulta_spcNotas_Output']['ListOfLvpSrNotesIo']['LvpServiceRequestCustom']['ListOfLvpServiceRequestNotes']['LvpServiceRequestNotes']

            return JsonResponse({'activitiesLiverpool':json.dumps(activitiesxml), 'notesLiverpool':json.dumps(notesxml)}, safe=False)
            