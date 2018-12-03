from mirari.mirari.admin import *
from .models import *
from .vars import *


@admin.register(Credit)
class CreditAdmin(PassAdmin):
	pass


@admin.register(Actor)
class ActorAdmin(PassAdmin):
	pass