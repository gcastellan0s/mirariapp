# -*- coding: utf-8 -*-
from mirari.mirari.views import *
from .models import *
from .vars import *	

import csv
from django.http import HttpResponse

###############################################################################################
# Product ##############################################################################
###############################################################################################
class Product__ListView(Generic__ListView):
	template_name = 'Product__ListView.html'
	model = Product

###############################################################################################
# InventoryOrder ##############################################################################
###############################################################################################
class InventoryOrder__ListView(Generic__ListView):
	template_name = 'InventoryOrder__ListView.html'
	model = InventoryOrder

class InventoryOrder__CreateView(Generic__CreateView):
	template_name = 'InventoryOrder__CreateView.html'
	model = InventoryOrder

class InventoryOrder__UpdateView(Generic__UpdateView):
	template_name = 'InventoryOrder__UpdateView.html'
	model = InventoryOrder

class printInventoryOrder__UpdateView(Generic__UpdateView):
	template_name = 'printInventoryOrder__UpdateView.html'
	model = InventoryOrder

class Inventory__ApiView(Generic__ApiView):
	permissions = False
	@method_decorator(csrf_exempt)
	def get_serializers(self, request):
		if request.POST.get('sendData'):
			data = json.loads(request.POST.get('sendData'))
			if 'idObject' in data:
				inventoryOrder = InventoryOrder.objects.get(pk=data['idObject'])
			else:
				inventoryOrder = InventoryOrder()
				inventoryOrder.organization = Organization.objects.get(id=self.request.session.get('organization'))
			if data['provider']:
				inventoryOrder.provider = Provider.objects.get(pk=data['provider'])
			if data['responsible']:
				inventoryOrder.responsible = User.objects.get(pk=data['responsible'])
			inventoryOrder.status = data['status']
			inventoryOrder.notes = data['notes']
			inventoryOrder.operationType = data['type']
			inventoryOrder.producttype = data['producttype']
			inventoryOrder.fordwarder = data['fordwarder']
			inventoryOrder.paymentCondition = data['paymentCondition']
			inventoryOrder.responsibleName = data['responsibleName']
			inventoryOrder.serial = data['serial']
			if data['client']:
				inventoryOrder.client = Client.objects.get(pk=data['client'])
			inventoryOrder.outType = data['outType']
			inventoryOrder.package = data['package']
			inventoryOrder.orderNumber = data['orderNumber']
			inventoryOrder.guideNumber = data['guideNumber']
			inventoryOrder.save()
			InventoryOrderProoduct.objects.filter(inventoryorder = inventoryOrder).delete()
			for product in data['productList']:
				inventoryOrderProoduct = InventoryOrderProoduct()
				p = Product.objects.get(pk=product[0]['id'])
				if data['status'] == 'TERMINADA' :
					if data['type'] == 'in':
						p.quantity += product[1]
					p.save()
				if data['status'] == 'EN TRANSITO' :
					if data['type'] == 'out':
						p.quantity -= product[1]
					p.save()
				inventoryOrderProoduct.product = p
				inventoryOrderProoduct.quantity = product[1]
				inventoryOrderProoduct.cost = product[2]
				inventoryOrderProoduct.specialCost = product[3]
				inventoryOrderProoduct.inventoryorder = inventoryOrder
				inventoryOrderProoduct.save()
			return JsonResponse({'sendData':inventoryOrder.pk}, safe=False)
		if request.POST.get('codebar'):
			return JsonResponse({'product':ProductSerializer(Product.objects.filter(codebar=request.POST.get('codebar'), active=True, organization__id=request.session.get('organization')).first()).data}, safe=False)
		if request.POST.get('productID'):
			return JsonResponse({'product':ProductSerializer(Product.objects.filter(pk=request.POST.get('productID')).first()).data}, safe=False)
		if request.POST.get('PlusCodebar'):
			product = Product.objects.get(codebar=request.POST.get('PlusCodebar'), active=True, organization__id=request.session.get('organization'))
			product.quantity += 1
			product.save()
			return JsonResponse({'ok':'ok'}, safe=False)
		if request.POST.get('getProducts'):	
			inventoryOrder = InventoryOrder.objects.get(pk=request.POST.get('getProducts'))
			products = InventoryOrderProoduct.objects.filter(inventoryorder = inventoryOrder)
			return JsonResponse({'products':InventoryOrderProoductSerializer(products, many=True).data}, safe=False)
		if request.POST.get('getProductsReport'):
			dates = request.POST.get('getProductsReport').split(" / ", 1)
			start = datetime.datetime.strptime(dates[0], '%d-%m-%Y')
			end = datetime.datetime.strptime(dates[1], '%d-%m-%Y')	
			inventoryOrderProoducts = InventoryOrderProoduct.objects.filter(inventoryorder__initialDateTime__range=(start, end))
			with open('ProductReport.csv', 'w', newline='', encoding='latin1') as csvfile:
				filewriter = csv.writer(csvfile, delimiter=',', quoting=csv.QUOTE_ALL)
				filewriter.writerow([
					'PRODUCTO',
					'UID',
					'SERIAL',
					'MODEL',
					'CANTIDAD',
					'PRECIO',
					'PRECIO ESPECIAL',
					'ID DE ORDEN',
					'No DE ORDEN',
					'No DE GUIA',
					'FECHA',
					'TIPO',
					'ESTATUS'
				])
				for inventoryOrderProoduct in inventoryOrderProoducts:
					
					if inventoryOrderProoduct.inventoryorder.operationType == 'in':
						tipoSalida = 'ENTRADA'
					else:
						tipoSalida = 'SALIDA'

					filewriter.writerow([
						inventoryOrderProoduct.product.name,
						inventoryOrderProoduct.product.model,
						inventoryOrderProoduct.product.uid,
						inventoryOrderProoduct.product.codebar,
						inventoryOrderProoduct.quantity,
						inventoryOrderProoduct.cost, 
						inventoryOrderProoduct.specialCost,
						inventoryOrderProoduct.inventoryorder.id,
						inventoryOrderProoduct.inventoryorder.orderNumber,
						inventoryOrderProoduct.inventoryorder.guideNumber,
						inventoryOrderProoduct.inventoryorder.initialDateTime.strftime("%m/%d/%Y %H:%M"),
						tipoSalida,
						inventoryOrderProoduct.inventoryorder.status,
					])
			return JsonResponse({'inventoryOrderProoduct': len(inventoryOrderProoducts)}, safe=False)
		if request.POST.get('getReportInventori'):
			range_ = request.POST.get('range').split(" / ", 1)
			start = datetime.datetime.strptime(range_[0], '%d-%m-%Y')
			end = datetime.datetime.strptime(range_[1], '%d-%m-%Y')
			products = InventoryOrderProoduct.objects.filter(inventoryorder__initialDateTime__range=(start, end))
			return JsonResponse({'products':InventoryOrderProoductSerializer(products, many=True).data}, safe=False)

class ProductReport__TemplateView(Generic__TemplateView):
	model = Product
	template_name = 'Product__ListView.html'
	###########################################################################################
	@method_decorator(csrf_exempt)
	def dispatch(self, request, *args, **kwargs):
		with open('ProductReport.csv', 'r', newline='', encoding='latin1') as csvfile:
			response = HttpResponse(csvfile, content_type='text/csv')
			response['Content-Disposition'] = 'attachment; filename="OrderServiceReport.csv"'
			return response