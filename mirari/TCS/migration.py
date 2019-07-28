import csv
from mirari.mirari.models import *
from mirari.TCS.models import *
import datetime
import dateutil.parser
o = Organization.objects.get(id=3)

with open('temp/tecnoservicio/users_user.csv') as csv_file: 
    csv_reader = csv.reader(csv_file, delimiter=',') 
    for row in csv_reader: 
        try:
            user = User.objects.filter(id_bckp=row[0], organization=o).first()
            if not user:
                user = User()
                user.username = o.code + '__' + row[4]
                user.organization = o
                user.visible_username = row[4]
                user.email = row[7]
                user.id_bckp = row[0]
            user.can_change_password = True
            user.needChangePassword = True
            user.save()
            user.set_password(user.visible_username)
            user.save()
            profileName = row[11]
            if profileName == 'Tecnico foraneo':
                profileName = 'FORANEO'
            elif profileName == 'Tecnico local':
                profileName = 'LOCAL'
            elif profileName == 'Operador':
                profileName = 'OPERADOR'
            elif profileName == 'Administrador':
                profileName = 'ADMINISTRADOR'
            elif profileName == 'Tienda':
                profileName = 'TIENDA'
            profile = Profile.objects.get(name= o.code + '__' + profileName)
            user.groups.clear()
            user.groups.add(profile)
        except Exception as e:
            print(str(e))

with open('temp/tecnoservicio/users_empresa.csv') as csv_file: 
    csv_reader = csv.reader(csv_file, delimiter=',') 
    for row in csv_reader: 
        company = Company.objects.filter(id_bckp=row[0], organization=o).first()
        if not company:
            company = Company()
            company.organization = o
            company.name = row[1]
            company.id_bckp = row[0]
            company.save()

with open('temp/tecnoservicio/ordenes_tienda.csv') as csv_file: 
    csv_reader = csv.reader(csv_file, delimiter=',') 
    for row in csv_reader: 
        store = Store.objects.filter(id_bckp=row[0], company__organization=o).first()
        if not store:
            store = Store()
            store.company = Company.objects.filter(id_bckp=row[5], organization=o).first()
            store.state = row[2]
            store.adress = row[3]
            store.phone = row[4]
            store.name = row[1]
            store.id_bckp = row[0]
            store.save()

with open('temp/tecnoservicio/ordenes_marca.csv') as csv_file: 
    csv_reader = csv.reader(csv_file, delimiter=',') 
    for row in csv_reader: 
        brand = Brand.objects.filter(id_bckp=row[0], organization=o).first()
        if not brand:
            brand = Brand()
            brand.organization = o
            brand.name = row[1]
            brand.id_bckp = row[0]
            brand.save()

with open('temp/tecnoservicio/ordenes_modelo.csv') as csv_file: 
    csv_reader = csv.reader(csv_file, delimiter=',') 
    for row in csv_reader: 
        modelo = Modelo.objects.filter(id_bckp=row[0], brand__organization=o).first()
        if not modelo:
            modelo = Modelo()
            modelo.brand = Brand.objects.filter(id_bckp=row[3], organization=o).first()
            modelo.name = row[1]
            modelo.description = row[2]
            modelo.id_bckp = row[0]
            modelo.save()
            

with open('temp/tecnoservicio/ordenes_orden.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',') 
    for row in csv_reader: 
        orderService = OrderService.objects.filter(id_bckp=row[0], organization=o).first()
        if not orderService:
            #try:
            orderService = OrderService()
            orderService.serial = row[1]
            orderService.organization = o
            orderService.creation_date = dateutil.parser.parse(row[2])# datetime.datetime.strptime(row[2].replace('/','-').split('+')[0], '%Y-%m-%d %H:%M:%S.%f')
            if row[34]:
                orderService.user = User.objects.filter(id_bckp=row[34], organization=o).first()
            else:
                orderService.user = None
            if row[35]:
                orderService.technical = User.objects.filter(id_bckp=row[35], organization=o).first()
            else:
                orderService.technical = None
            orderService.status = row[3]
            orderService.service = row[4]
            orderService.zone = row[5]
            orderService.concept = row[6]
            if row[7]:
                orderService.service_date = dateutil.parser.parse(row[7]) #datetime.datetime.strptime(row[7], '%Y-%m-%d')
            else:
                orderService.service_date = None
            if row[8]:
                orderService.buy_date = dateutil.parser.parse(row[8]) #datetime.datetime.strptime(row[8], '%Y-%m-%d')
            else:
                orderService.buy_date = None
            if row[9]:
                orderService.delivery_date = dateutil.parser.parse(row[9]) #datetime.datetime.strptime(row[9], '%Y-%m-%d')
            else:
                orderService.delivery_date = None
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
            orderService.company = Company.objects.get(id_bckp=row[31], organization=o)
            orderService.companyName = Company.objects.get(id_bckp=row[31], organization=o).name
            orderService.store = Store.objects.get(id_bckp=row[36], company__organization=o)
            orderService.storeName = Store.objects.get(id_bckp=row[36], company__organization=o).name
            orderService.brand = Brand.objects.get(id_bckp=row[32], organization=o)
            orderService.brandName = Brand.objects.get(id_bckp=row[32], organization=o).name
            orderService.report_name = row[21]
            if row[33]:
                orderService.modelo = Modelo.objects.get(id_bckp=row[33], brand__organization=o)
                orderService.modeloName = Modelo.objects.get(id_bckp=row[33], brand__organization=o).name
            else:
                orderService.modelo = None
                orderService.modeloName = None
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
            #except Exception as e:
                #print(row[1], str(e))
            

with open('temp/tecnoservicio/ordenes_concepto.csv') as csv_file: 
    csv_reader = csv.reader(csv_file, delimiter=',') 
    for row in csv_reader: 
        orderServiceConcept = OrderServiceConcept.objects.filter(id_bckp=row[0], orderservice__organization=o).first()
        if not orderServiceConcept:
            orderServiceConcept = OrderServiceConcept()
            orderServiceConcept.orderservice = OrderService.objects.filter(id_bckp=row[5], organization=o).first()
            if row[6]:
                orderServiceConcept.user = User.objects.filter(id_bckp=row[6], organization=o).first()
            else:
                orderServiceConcept.user = None
            orderServiceConcept.concept = row[1]
            orderServiceConcept.quantity = row[2]
            orderServiceConcept.creation_date = dateutil.parser.parse(row[3])
            orderServiceConcept.id_bckp = row[0]
            orderServiceConcept.save()
with open('temp/tecnoservicio/ordenes_mensaje.csv') as csv_file: 
    csv_reader = csv.reader(csv_file, delimiter=',') 
    for row in csv_reader: 
        orderServiceComment = OrderServiceComment.objects.filter(id_bckp=row[0], orderservice__organization=o).first()
        if not orderServiceComment:
            orderServiceComment = OrderServiceComment()
            orderServiceComment.orderservice = OrderService.objects.filter(id_bckp=row[3], organization=o).first()
            if row[4]:
                orderServiceComment.user = User.objects.filter(id_bckp=row[4], organization=o).first()
            else:
                orderServiceComment.user = None
            orderServiceComment.comment = row[2]
            orderServiceComment.creation_date = dateutil.parser.parse(row[1])
            orderServiceComment.id_bckp = row[0]
            orderServiceComment.save()