import csv
from mirari.mirari.models import *
from mirari.TCS.models import *
import datetime
import dateutil.parser

o = Organization.objects.get(id=6)

with open('temp/mexicof/users_user.csv') as csv_file: 
    csv_reader = csv.reader(csv_file, delimiter=',') 
    for row in csv_reader: 
        user = User.objects.filter(id_bckp=row[0]).first()
        if not user:
            user = User()
            user.username = o.code + '__' + row[4]
            user.visible_username = row[4]
            user.email = row[7]
            user.id_bckp = row[0]
        user.can_change_password = True
        user.needChangePassword = True
        user.save()
        user.set_password(user.visible_username)
        profileName = row[11]
        if profileName == 'Tecnico foraneo':
            profileName = 'FORANEO'
        elif profileName == 'Tecnico local':
            profileName = 'LOCAL'
        elif profileName == 'Operador':
            profileName = 'OPERADOR'
        elif profileName == 'Administrador':
            profileName = 'ADMINISTRADOR'
        profile = Profile.objects.get(name= o.code + '__' + profileName)
        user.groups.clear()
        user.groups.add(profile)

with open('temp/mexicof/users_empresa.csv') as csv_file: 
    csv_reader = csv.reader(csv_file, delimiter=',') 
    for row in csv_reader: 
        company = Company.objects.filter(id_bckp=row[0]).first()
        if not company:
            company = Company()
            company.organization = o
            company.name = row[1]
            company.id_bckp = row[0]
            company.save()

with open('temp/mexicof/ordenes_tienda.csv') as csv_file: 
    csv_reader = csv.reader(csv_file, delimiter=',') 
    for row in csv_reader: 
        store = Store.objects.filter(id_bckp=row[0]).first()
        if not store:
            store = Store()
            store.company = Company.objects.filter(id_bckp=row[5]).first()
            store.state = row[2]
            store.adress = row[3]
            store.phone = row[4]
            store.name = row[1]
            store.id_bckp = row[0]
            store.save()

with open('temp/mexicof/ordenes_orden.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',') 
    for row in csv_reader: 
        orderService = OrderService.objects.filter(id_bckp=row[0]).first()
        if not orderService:
            try:
                orderService = OrderService()
                orderService.serial = row[1]
                orderService.organization = o
                orderService.creation_date = dateutil.parser.parse(row[2])# datetime.datetime.strptime(row[2].replace('/','-').split('+')[0], '%Y-%m-%d %H:%M:%S.%f')
                orderService.user = User.objects.get(id_bckp=row[21])
                orderService.technical = User.objects.get(id_bckp=row[35])
                orderService.status = row[3]
                orderService.service = row[4]
                orderService.zone = row[5]
                orderService.concept = row[6]
                orderService.service_date = dateutil.parser.parse(row[7]) #datetime.datetime.strptime(row[7], '%Y-%m-%d')
                orderService.buy_date = dateutil.parser.parse(row[8]) #datetime.datetime.strptime(row[8], '%Y-%m-%d')
                orderService.delivery_date = dateutil.parser.parse(row[9]) #datetime.datetime.strptime(row[9], '%Y-%m-%d')
                orderService.client_name = row[10]
                orderService.email = row[11]
                orderService.contact_phone1 = row[12]
                orderService.contact_phone2 = row[13]
                orderService.contact_phone3 = row[14]
                orderService.address = row[15]
                orderService.colony = row[16]
                orderService.city = row[17]
                orderService.cp = row[18]
                orderService.address_reference = row[19] + ' ' + row[20]
                orderService.client_notes = row[23]
                orderService.company = Company.objects.get(id_bckp=row[31])
                orderService.companyName = Company.objects.get(id_bckp=row[31]).name
                orderService.store = Store.objects.get(id_bckp=row[36])
                orderService.storeName = Store.objects.get(id_bckp=row[36]).name
                orderService.brand = Brand.objects.get(id_bckp=row[32])
                orderService.brandName = Brand.objects.get(id_bckp=row[32]).name
                orderService.report_name = row[21]
                orderService.modelo = Modelo.objects.get(id_bckp=row[33])
                orderService.modeloName = Modelo.objects.get(id_bckp=row[33]).name
                orderService.serial_number = row[22]
                orderService.hidden_notes = row[23]
                orderService.order_notes = row[24]
                orderService.icon_os = row[25]
                orderService.icon_ics = row[26]
                orderService.icon_ics_2 = row[27]
                orderService.icon_ics_3 = row[28]
                orderService.icon_on = row[29]
                orderService.icon_cn = row[30]
                orderService.id_bckp = row[0]
                orderService.comments = row[24]
                orderService.save()
                print(orderService.serial)
            except Exception as e:
                print (row[1], str(e))