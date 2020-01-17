# -*- coding: utf-8 -*-
from mirari.mirari.views import *
from .models import *
from .vars import *	


###############################################################################################
# OrderPicking ################################################################################
###############################################################################################
class InventoryOrderReception__TemplateView(Generic__TemplateView):
    ###########################################################################################
    def dispatch(self, request, *args, **kwargs):
        return HttpResponseRedirect(reverse('STR:dashboard__Organization__TemplateView', args=[])+'?type=RECEPCIONES')

class InventoryOrderPicking__TemplateView(Generic__TemplateView):
    ###########################################################################################
    def dispatch(self, request, *args, **kwargs):
        return HttpResponseRedirect(reverse('STR:dashboard__Organization__TemplateView', args=[])+'?type=ENTREGA')