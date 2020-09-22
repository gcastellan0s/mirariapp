from mirari.mirari.admin import *
from .models import *
from .vars import *

@admin.register(Storehouse)
class StorehouseAdmin(PassAdmin):
	list_display = ('id', 'name',)

@admin.register(Provider)
class ProviderAdmin(PassAdmin):
	list_display = ('id', 'name','uid','codebar')
	search_fields = ['name','uid','codebar']

@admin.register(CategoryProduct)
class CategoryProductAdmin(PassAdmin):
	list_display = ('id', 'name',)

@admin.register(InventoryOrder)
class InventoryOrderAdmin(PassAdmin):
	list_display = ('id',)
	
@admin.register(Product)
class ProductAdmin(PassAdmin):
	list_display = ('id',)

@admin.register(InventoryOrderProoduct)
class InventoryOrderProoduct(PassAdmin):
	list_display = ('id',)