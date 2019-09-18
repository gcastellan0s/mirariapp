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
    list_display = ('sellpoint','barcode', 'key','rasurado','total',)
    search_fields = ('key', 'barcode')

@admin.register(TicketProducts)
class TicketProductsAdmin(PassAdmin):
    pass

@admin.register(Cut)
class CutAdmin(PassAdmin):
    list_display = ('sellpoint',)

@admin.register(Offer)
class OfferAdmin(PassAdmin):
    pass

@admin.register(ClientProfile)
class ClientProfileAdmin(PassAdmin):
    pass

@admin.register(Client)
class ClientAdmin(PassAdmin):
    pass


@admin.register(SellpointGroups)
class SellpointGroupsAdmin(PassAdmin):
    pass