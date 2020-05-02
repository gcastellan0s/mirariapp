import requests
headers = {
    'Content-Type': 'text/xml',
    'SOAPAction': '"http://www.example.org/wbi/AltaOperation"',
}
data = open('request.xml', 'rb').read()
response = requests.post('https://srproveedoresqa.liverpool.com.mx/wbi/AltaTicket', headers=headers, data=data)




curl -X POST -H "Content-Type: text/xml" \
    -H 'SOAPAction: "http://www.example.org/wbi/AltaOperation"' \
    --data-binary @request.xml \
    https://srproveedoresqa.liverpool.com.mx/wbi/AltaTicket







        

from mirari.mirari.models import *
from mirari.TCS.models import *

from lxml.etree import Element, SubElement, tostring, XML, XMLParser, fromstring
from lxml import etree
from requests import Session
from requests.auth import HTTPBasicAuth
from zeep import Client, Plugin
from zeep.transports import Transport
import requests
import xmltodict

class my_plugin(Plugin):
    def egress(self, envelope, http_headers, operation, binding_options):
        xmlString = tostring(envelope, encoding='unicode')
        xmlString = xmlString.replace("&lt;", "<")
        xmlString = xmlString.replace("&gt;", ">")
        xmlString = xmlString.replace("&amp;", "&")
        parser = XMLParser(strip_cdata=False)
        newenvelope = XML(xmlString, parser=parser)
        return newenvelope, http_headers

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
if (str(response) == '<Response [200]>'):
    xml = xmltodict.parse(xmltodict.parse(response.text.encode())['soapenv:Envelope']['soapenv:Body']['NS1:TransferenciaResponse']['NS1:archivo'])
    xml = xml['ns:LVP_spcConsulta_spcSR_Output']['ListOfLvpServiceRequestIo']['LvpServiceRequestCustom']
    for order in xml:    
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
        orderService.client_notes = order['Abstract'] + ' Area:' + order['INSArea'] + ' SubArea:' + order['INSSub-Area'] + ' Tipo:' + order['LVPType4thLevel']
        orderService.company = Company.objects.filter(pk=37).first()
        orderService.companyName = 'liverpool'
        orderService.report_name = order['LVPCreatedBy']
        orderService.serial_number = order['SerialNumber']
        orderService.order_notes = 'Modelo: ' + order['LVPAssetModel']
        orderService.save(commit=False)
        print(orderService)




node = client.create_message(client.service, 'AltaOperation', **request_data)
tostring(node)


