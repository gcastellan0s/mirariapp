# -*- coding: utf-8 -*-
from mirari.mirari.views import *
from .models import *
from .vars import *	


###############################################################################################
# InventoryOrder ##############################################################################
###############################################################################################
class InventoryOrder__ListView(Generic__ListView):
    def list(self):
        extrabuttons = ''
        if self.request.user.has_perm('mirari.Can_Change__Password'):
            extrabuttons = '<a href="{{url_password}}" class="btn btn-outline-primary btn-elevate btn-circle btn-icon btn-sm mr-3" title="Cambiar contraseña"><i class="la la-key"></i></a>'
        return self.render_list(extrabuttons = extrabuttons)