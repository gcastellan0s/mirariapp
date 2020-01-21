# -*- coding: utf-8 -*-
from mirari.mirari.views import *
from .models import *
from .vars import *	


###############################################################################################
# InventoryOrder ##############################################################################
###############################################################################################
class InventoryOrder__ListView(Generic__ListView):
    template_name = 'generic/ListViewx.html'
    model = InventoryOrder