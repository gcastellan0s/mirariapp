# -*- coding: utf-8 -*-
from mirari.mirari.views import *
from .models import *
from .vars import *	

class OrderService__ApiView(Generic__ApiView):
	def get_objects(self):
		if request.GET.get('api'):
			if action == 'get_Technical':
				pass
		class ApiSerializer(Base_Serializer):
			pass
		ApiSerializer.Meta.model = self.model
		return ApiSerializer(self.request.user)