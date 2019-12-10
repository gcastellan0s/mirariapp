from mirari.mirari.admin import *
from .models import *
from .vars import *

@admin.register(Provider)
class ProviderAdmin(PassAdmin):
	list_display = ('id', 'name', 'id_bckp',)

@admin.register(CategoryProduct)
class CategoryProductAdmin(PassAdmin):
	list_display = ('id', 'name', 'id_bckp',)

@admin.register(Store)
class Product(PassAdmin):
	list_display = ('id', 'name', 'id_bckp',)