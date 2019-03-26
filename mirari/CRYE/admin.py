from mirari.mirari.admin import *
from .models import *
from .vars import *


@admin.register(WalletCredit)
class WalletCreditAdmin(admin.ModelAdmin):
	actions_on_top = True
	actions_on_bottom = False

    
@admin.register(TablaAmortizacion)
class TablaAmortizacionAdmin(admin.ModelAdmin):
	actions_on_top = True
	actions_on_bottom = False
	list_display = ('walletcredit', 'numeroPago',)