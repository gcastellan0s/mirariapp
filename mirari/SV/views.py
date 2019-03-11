# -*- coding: utf-8 -*-
from mirari.mirari.views import *
from .models import *
from .vars import *

########################################################
########################################################
class SellpointSerializer(Base_Serializer):
	class Meta(Basic_Serializer.Meta):
		model = Sellpoint
########################################################	
class MenuSerializer(Base_Serializer):
	class Meta(Basic_Serializer.Meta):
		model = Menu
########################################################
class ProductSerializer(Base_Serializer):
	class Meta(Basic_Serializer.Meta):
		model = Product
########################################################
class ProductAttributesSerializer(Base_Serializer):
	product = serializers.SerializerMethodField()
	class Meta(Basic_Serializer.Meta):
		model = ProductAttributes
	def get_product(self, obj):
		return ProductSerializer(obj.product, read_only=True).data
########################################################
class TicketSerializer(Base_Serializer):
	class Meta(Basic_Serializer.Meta):
		model = Ticket


########################################################
########################################################
class sv__Sellpoint__TemplateView(Generic__TemplateView):
	template_name = "sv__Sellpoint__TemplateView.html"


########################################################
########################################################
class Sellpoint__ApiView(Generic__ApiView):
	permissions = False
	def get_serializers(self, request):
		if request.GET.get('api') == 'getStates':
			sellpoints = Sellpoint.objects.filter(organization=request.user.organization, active=True, is_active=True)
			productattributes = ProductAttributes.objects.filter( sellpoint__in=sellpoints.all() )
			menu = []
			for productattribute in productattributes:
				for pmenu in productattribute.product.menu.all():
					if not pmenu.pk in menu:
						menu.append(pmenu.pk)
			return JsonResponse({
				'sellpoints': SellpointSerializer( sellpoints , many=True ).data,
				'productAttributes': ProductAttributesSerializer( productattributes, many=True ).data,
				'menus': MenuSerializer( Menu.objects.filter(pk__in = menu), many=True ).data 
			}, safe=False)
		if request.GET.get('api') == 'printTicket':
			return JsonResponse({
				'ticket': TicketSerializer(Ticket().new( activeSellpoint = json.loads(request.POST.get('activeSellpoint')), ticket = json.loads(request.POST.get('ticket')) )).data
			}, safe=False)