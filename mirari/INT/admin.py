from mirari.mirari.admin import *
from .models import *
from .vars import *

@admin.register(Catalogue)
class CatalogueAdmin(PassAdmin):
	pass

@admin.register(Team)
class TeamAdmin(PassAdmin):
	pass

@admin.register(Notification)
class NotificationAdmin(PassAdmin):
	pass

@admin.register(Handbook)
class HandbookAdmin(PassAdmin):
	pass

