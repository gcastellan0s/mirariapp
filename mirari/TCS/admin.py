from mirari.mirari.admin import *
from .models import *
from .vars import *

@admin.register(Company)
class CompanyAdmin(PassAdmin):
	list_display = ('id', 'name', 'id_bckp',)

@admin.register(Store)
class StoreAdmin(PassAdmin):
	pass

@admin.register(Brand)
class BrandAdmin(PassAdmin):
	pass

@admin.register(Modelo)
class ModeloAdmin(PassAdmin):
	list_display = ('name', 'id_bckp',)
	search_fields = ('name', 'id_bckp')

@admin.register(OrderService)
class OrderServiceAdmin(PassAdmin):
	pass