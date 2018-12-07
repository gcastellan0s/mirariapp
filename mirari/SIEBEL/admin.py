from mirari.mirari.admin import *
from .models import *
from .vars import *


@admin.register(CreditType)
class CreditAdmin(PassAdmin):
	pass


@admin.register(Actor)
class ActorAdmin(PassAdmin):
	pass


@admin.register(Person)
class PersonAdmin(PassAdmin):
	pass