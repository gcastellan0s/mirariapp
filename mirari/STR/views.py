# -*- coding: utf-8 -*-
from mirari.mirari.views import *
from .models import *
from .vars import *	

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
			inventoryOrder.save()
			InventoryOrderProoduct.objects.filter(inventoryorder = inventoryOrder).delete()
			for product in data['productList']:
				inventoryOrderProoduct = InventoryOrderProoduct()
				p = Product.objects.get(pk=product[0]['id'])
				if data['status'] == 'TERMINADA':
					if data['type'] == 'in':
						p.quantity += product[1]
					if data['type'] == 'out':
						p.quantity -= product[1]
					p.save()
				inventoryOrderProoduct.product = p
				inventoryOrderProoduct.quantity = product[1]
				inventoryOrderProoduct.inventoryorder = inventoryOrder
				inventoryOrderProoduct.save()
			return JsonResponse({'sendData':inventoryOrder.pk}, safe=False)
		if request.POST.get('codebar'):
			return JsonResponse({'product':ProductSerializer(Product.objects.filter(codebar=request.POST.get('codebar')).first()).data}, safe=False)
		if request.POST.get('productID'):
			return JsonResponse({'product':ProductSerializer(Product.objects.filter(pk=request.POST.get('productID')).first()).data}, safe=False)
		if request.POST.get('PlusCodebar'):
			product = Product.objects.filter(codebar=request.POST.get('PlusCodebar')).first()
			product.quantity += 1
			product.save()
			return JsonResponse({'ok':'ok'}, safe=False)
		if request.POST.get('getProducts'):	
			inventoryOrder = InventoryOrder.objects.get(pk=request.POST.get('getProducts'))
			products = InventoryOrderProoduct.objects.filter(inventoryorder = inventoryOrder)
			return JsonResponse({'products':InventoryOrderProoductSerializer(products, many=True).data}, safe=False)
			