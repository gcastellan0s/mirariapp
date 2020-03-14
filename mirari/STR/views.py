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
	#def get_serializers(self, request):
		#Action = request.GET.get('api')
		#if Action == 'getOnlineStatus':
			#return JsonResponse({'api':'ok'}, safe=False)
		#elif Action == 'getReport':
			#sellpointgroup = SellpointGroups.objects.get(pk=request.POST.get('sellpointgroup'))
			#cut = Cut.objects.filter(sellpoint__in=sellpointgroup.sellpoints.all(), final_time__year=2019, final_time__month=request.POST.get('month'), final_time__day=request.POST.get('day'))
			#return JsonResponse({'day':request.POST.get('day'), 'cuts':CutReportSerializer(cut, many=True).data}, safe=False)
		#return JsonResponse({'message':'Ocurrió un error en el servidor'}, status=500)