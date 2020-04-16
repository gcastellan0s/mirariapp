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

class Inventory__ApiView(Generic__ApiView):
	permissions = False
	@method_decorator(csrf_exempt)
	def get_serializers(self, request):
		if request.POST.get('sendData'):
			data = json.loads(request.POST.get('sendData'))
			inventoryOrder = InventoryOrder()
			inventoryOrder.provider = Provider.objects.get(pk=data.provider)
			inventoryOrder.document = data.document
			inventoryOrder.priority = data.priority
			inventoryOrder.responsible = User.objects.get(pk=data.responsible)
			inventoryOrder.notes = data.notes
			inventoryOrder.save()
			#for product in data['productList']:
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