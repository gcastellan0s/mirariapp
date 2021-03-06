import csv
from mirari.mirari.models import *
from mirari.SV.models import *
import datetime
import dateutil.parser

o = Organization.objects.get(id=11)

with open('temp/estrella/sellpoint_menu.csv') as csv_file: 
    csv_reader = csv.reader(csv_file, delimiter=',') 
    for row in csv_reader: 
        try:
            menu = Menu.objects.filter(id_bckp=row[0], organization=o).first()
            if not menu:
                if row[10] == 7:
                    menu = Menu()
                    menu.organization = o
                    menu.name = row[1]
                    menu.color = row[2]
                    menu.id_bckp = row[0]
                    menu.save()
        except Exception as e:
            print(str(e))

with open('temp/estrella/sellpoint_product.csv') as csv_file: 
    csv_reader = csv.reader(csv_file, delimiter=',') 
    for row in csv_reader: 
        try:
            product = Product.objects.filter(id_bckp=row[0], organization=o).first()
            if not product:
                menu = Menu.objects.filter(id_bckp=row[6], organizatin=o).first()
                if row[4] == True:
                    product = Product()
                    product.organization = o
                    product.name = row[2]
                    product.menu = menu
                    product.id_bckp = row[0]
                    product.save()
        except Exception as e:
            print(str(e))