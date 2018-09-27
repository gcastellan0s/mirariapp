from mirari.mirari.admin import *
from .models import *
from .vars import *

@admin.register(Catalogue)
class CatalogueAdmin(PassAdmin):
	pass