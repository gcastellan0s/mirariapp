from mirari.mirari.admin import *
from .models import *
from .vars import *

@admin.register(Photo)
class PhotoAdmin(PassAdmin):
	pass