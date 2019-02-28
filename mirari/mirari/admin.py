from .models import *
from .adminbase import *

@admin.register(Module)
class ModuleAdmin(PassAdmin):
	pass

@admin.register(Organization)
class OrganizationAdmin(PassAdmin):
	pass

@admin.register(User)
class UserAdmin(PassAdmin):
	actions_on_top = True
	actions_on_bottom = False
	search_fields = ('pk', 'username', 'visible_username', 'email',)
	list_display = ('pk', 'username', 'visible_username', 'email')

@admin.register(Profile)
class ProfileAdmin(PassAdmin):
	actions_on_top = True
	actions_on_bottom = False
	#list_display = ('visible_name', 'name', 'organization',)

@admin.register(Permission)
class PermissionAdmin(admin.ModelAdmin):
	actions_on_top = True
	actions_on_bottom = False
	search_fields = ('codename', 'name')
	list_display = ('codename', 'name', 'content_type',)

@admin.register(ProductsServicesSAT)
class ProductsServicesSATAdmin(PassAdmin):
	pass

@admin.register(UnitsCodesSat)
class UnitsCodesSatAdmin(PassAdmin):
	pass

@admin.register(DBConnection)
class DBConnectionAdmin(PassAdmin):
	pass

@admin.register(HostEmail)
class HostEmailAdmin(PassAdmin):
	pass

@admin.register(HTMLPage)
class HTMLPageAdmin(PassAdmin):
	pass