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
        #p = Profile.objects.all()
        #for a in p:
            #a.visible_name = a.name.split('__')[1]
            ##a.name = a.organization.code +'__'+ a.name.upper()
            #a.save()
        #import csv
        #from mirari.INT.models import Team
        #with open('temp/mxf/users_user.csv', newline='', encoding='utf-8') as f:
            #reader = csv.reader(f)
            #p_local = Profile.objects.get(name=u.organization.code + '__LOCAL')
            #p_foraneo = Profile.objects.get(name=u.organization.code + '__FORANEO')
            #p_operador = Profile.objects.get(name=u.organization.code + '__OPERADOR')
            #p_administrador = Profile.objects.get(name=u.organization.code + '__ADMINISTRADOR')
            #for row in reader:
                #if not User.objects.filter(username = u.organization.code + '__' + row[4]):
                    #user = User()
                    #user.username = u.organization.code + '__' + row[4]
                    #user.visible_username = row[4]
                    #user.organization = u.organization
                    #user.email = row[7]
                    #user.id_bckp = row[0]
                    #user.set_password(row[4])
                    #user.save()
                    #if row[11] == 'Operador':
                        #user.groups.add(p_operador)
                    #elif row[11] == 'Tecnico foraneo':
                        #user.groups.add(p_foraneo)
                    #elif row[11] == 'Tecnico local':
                        #user.groups.add(p_local)
                    #elif row[11] == 'Administrador':
                        #user.groups.add(p_administrador)
        #with open('temp/users_empresa.csv', newline='', encoding='utf-8') as f:
            #reader = csv.reader(f)
            #for row in reader:
                #if not Company.objects.filter(name = row[1].capitalize()):
                    #company = Company()
                    #company.name = row[1].capitalize()
                    #company.organization = request.user.organization
                    #company.id_bckp = row[0]
                    #company.save()
        #with open('temp/ordenes_tienda.csv', newline='', encoding='utf-8') as f:
            #reader = csv.reader(f)
            #for row in reader:
                #if not Store.objects.filter(name = row[1]):
                    #store = Store()
                    #store.name = row[1]
                    #store.state = row[2]
                    #store.adress = row[3]
                    #store.phone = row[4]
                    #store.organization = request.user.organization
                    #store.company = Company.objects.get(id_bckp=row[5])
                    #store.id_bckp = row[0]
                    #store.save()
        #with open('temp/ordenes_marca.csv', newline='', encoding='utf-8') as f:
            #reader = csv.reader(f)
            #for row in reader:
                #if not Brand.objects.filter(name = row[1]):
                    #brand = Brand()
                    #brand.name = row[1]
                    #brand.id_bckp = row[0]
                    #brand.save()
        #with open('temp/ordenes_marca_tienda.csv', newline='', encoding='utf-8') as f:
            #reader = csv.reader(f)
            #for row in reader:
                #store = Store.objects.get(id_bckp = row[2])
                #brand = Brand.objects.get(id_bckp = row[1])
                #brand.company.add(store.company)
        #with open('temp/ordenes_modelo.csv', newline='', encoding='utf-8') as f:
            #reader = csv.reader(f)
            #for row in reader:
                #if not Modelo.objects.filter(name = row[1]):
                    #modelo = Modelo()
                    #modelo.brand = Brand.objects.get(id_bckp = row[3])
                    #modelo.name = row[1]
                    #modelo.description = row[2]
                    #modelo.id_bckp = row[0]
                    #modelo.save()
        #with open('temp/mxf/ordenes_orden.csv', newline='', encoding='utf-8') as f:
            #reader = csv.reader(f)
            #for row in reader:
                #try:
                    #service_date = None
                    #buy_date = None
                    #delivery_date = None
                    #if row[7]:
                        #service_date = datetime.datetime.strptime(row[7], '%d/%m/%Y')
                    #if row[8]:
                        #buy_date = datetime.datetime.strptime(row[8], '%d/%m/%Y')
                    #if row[9]:
                        #delivery_date = datetime.datetime.strptime(row[9], '%d/%m/%Y')
                    #orderService = OrderService()
                    #orderService.serial = row[1]
                    #orderService.organization = u.organization
                    #orderService.creation_date = datetime.datetime.strptime(row[2], '%d/%m/%Y %H:%M:%S.%f+00')
                    #orderService.user = User.objects.get(id_bckp=row[34], organization=u.organization)
                    #orderService.technical = User.objects.get(id_bckp=row[35], organization=u.organization)
                    #orderService.status = row[3]
                    #orderService.service = row[4]
                    #orderService.zone = row[5]
                    #orderService.concept = row[6]
                    #orderService.service_date = service_date
                    #orderService.buy_date = buy_date
                    #orderService.delivery_date = delivery_date
                    #orderService.client_name = row[10]
                    #orderService.email = row[11]
                    #orderService.contact_phone1 = row[12]
                    #orderService.contact_phone2 = row[13]
                    #orderService.contact_phone3 = row[14]
                    #orderService.address = row[15]
                    #orderService.colony = row[16]
                    #orderService.city = row[17]
                    #orderService.cp = row[18]
                    #orderService.address_reference = row[19] + ', ' +  row[20]
                    #orderService.company = Company.objects.filter(id_bckp=row[31], organization=u.organization).first()
                    #orderService.store = Store.objects.filter(id_bckp=row[36], company__organization=u.organization).first()
                    #orderService.brand = Brand.objects.filter(id_bckp=row[32], organization=u.organization).first()
                    #orderService.report_name = row[21]
                    #orderService.modelo = Modelo.objects.filter(id_bckp=row[33], brand__organization=u.organization).first()
                    #orderService.serial_number = row[22]
                    #orderService.hidden_notes = row[23]
                    #orderService.order_notes = row[24]
                    #orderService.icon_os = row[25]
                    #orderService.icon_ics = row[26]
                    #orderService.icon_ics_2 = row[27]
                    #orderService.icon_ics_3 = row[28]
                    #orderService.icon_on = row[29]
                    #orderService.icon_cn = row[30]
                    #orderService.id_bckp = row[0]
                    #orderService.save()
                #except:
                    #pass
        return super().dispatch(request, *args, **kwargs)
    