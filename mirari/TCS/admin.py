from mirari.mirari.admin import *
from .models import *
from .vars import *

@admin.register(Company)
class CompanyAdmin(PassAdmin):
	pass

@admin.register(Store)
class StoreAdmin(PassAdmin):
	pass

@admin.register(Brand)
class BrandAdmin(PassAdmin):
	pass

@admin.register(Modelo)
class ModeloAdmin(PassAdmin):
	pass

@admin.register(OrderService)
class OrderServiceAdmin(PassAdmin):
	pass