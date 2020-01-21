# -*- coding: utf-8 -*-
from mirari.mirari.views import *
from .models import *
from .vars import *	


###############################################################################################
# InventoryOrder ##############################################################################
###############################################################################################
class InventoryOrder__ListView(Generic__ListView):
    template_name = 'InventoryOrder__ListView.html'
    model = InventoryOrder

class InventoryOrder__CreateView(Generic__CreateView):
    template_name = 'InventoryOrder__CreateView.html'
    model = InventoryOrder