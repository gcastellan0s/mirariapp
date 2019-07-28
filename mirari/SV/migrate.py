import csv
from mirari.mirari.models import *
from mirari.SV.models import *
import datetime
import dateutil.parser

marelisama = 6
estrella = Organization.objects.get(id=11)
nMPanaderia = Sellpoint.objects.get(id=9)
nMCafeteria = Sellpoint.objects.get(id=10)
nMPollos = Sellpoint.objects.get(id=11)
nMTortas = Sellpoint.objects.get(id=12)
Panaderia = 1
Cafeteria = 2
Pollos = 4
Tortas = 3

with open('temp/estrella/sellpoint_menu.csv') as csv_file: 
    csv_reader = csv.reader(csv_file, delimiter=',') 
    for row in csv_reader: 
        menu = Menu.objects.filter(id_bckp=row[0], organization=estrella).first()
        if not menu and row[5] == 't' and row[10] == '6':
            menu = Menu()
            menu.organization = estrella
            menu.name = row[1]
            menu.color = row[2]
            menu.is_active = row[4]
            menu.id_bckp = row[0]
            menu.save()

with open('temp/estrella/sellpoint_product.csv') as csv_file: 
    csv_reader = csv.reader(csv_file, delimiter=',') 
    for row in csv_reader: 
        product = Product.objects.filter(id_bckp=row[0], organization=estrella).first()
        menu = Menu.objects.filter(id_bckp=row[6], organization=estrella)
        if not product and row[5] == 't' and menu:
            product = Product()
        product.organization = estrella
        product.name = row[2]
        product.is_active = row[3]
        product.id_bckp = row[0]
        product.save(commit=False)
        product.menu.add(menu)
        product.save()