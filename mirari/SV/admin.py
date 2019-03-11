from mirari.mirari.admin import *
from .models import *
from .vars import *

@admin.register(Sellpoint)
class SellpointAdmin(PassAdmin):
	pass

@admin.register(Menu)
class MenuAdmin(PassAdmin):
	pass

@admin.register(Product)
class ProductAdmin(PassAdmin):
	pass

@admin.register(ProductAttributes)
class ProductAttributesAdmin(PassAdmin):
	pass

@admin.register(Ticket)
class TicketAdmin(PassAdmin):
	pass

@admin.register(TicketProducts)
class TicketProductsAdmin(PassAdmin):
	pass

@admin.register(Cut)
class CutAdmin(PassAdmin):
	pass