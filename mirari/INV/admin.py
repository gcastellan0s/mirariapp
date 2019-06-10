from mirari.mirari.admin import *
from .models import *
from .vars import *

@admin.register(Invoice)
class InvoiceAdmin(PassAdmin):
	pass