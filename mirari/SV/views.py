# -*- coding: utf-8 -*-
from mirari.mirari.views import *
from .models import *
from .vars import *

class SellpointSerializer(Base_Serializer):
	class Meta(Basic_Serializer.Meta):
		model = Sellpoint
class MenuSerializer(Base_Serializer):
	class Meta(Basic_Serializer.Meta):
		model = Menu
class ProductSerializer(Base_Serializer):
	class Meta(Basic_Serializer.Meta):
		model = Product
class ProductAttributesSerializer(Base_Serializer):
	class Meta(Basic_Serializer.Meta):
		model = ProductAttributes

class SetSellpoint__ApiView(Generic__ApiView):
	def dispatch(self, request, *args, **kwargs):
		self.initialize(request, *args, **kwargs)
		if request.method == "POST" or request.method == "GET":
			employeeaccess = EmployeeAccess.objects.filter(user = self.request.user, active=True)[0]
			sellpoints = employeeaccess.sellpoints.all().filter(is_active=True, active=True)
			menus = Menu.objects.filter(organization = self.request.user.organization, is_active=True, active=True)
			products = ProductAttributes.objects.filter(product__sellpoints__in = sellpoints, is_active=True, active=True)
			return JsonResponse({
				'Sellpoints': SellpointSerializer(employeeaccess.sellpoints.all(), many=True).data,
				'Menus': MenuSerializer(menus, many=True).data,
				'Products': ProductAttributesSerializer(products, many=True).data,
			})
		return super().dispatch(request, *args, **kwargs)