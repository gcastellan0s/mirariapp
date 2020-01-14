# -*- coding: utf-8 -*-
from mirari.mirari.views import *
from .models import *
from .vars import *	


###############################################################################################
# SiebelUnblock ###############################################################################
###############################################################################################
class InventoryOrder__TemplateView(Generic__TemplateView):
    model = apps.get_model(APP, 'InventoryOrder')
    template_name = "InventoryOrder__TemplateView.html"
    ###########################################################################################
    #@method_decorator(csrf_exempt)
    #def dispatch(self, request, *args, **kwargs):
        #message, api = 'Hay un error en tu consulta', 'error' 
        #if request.method == 'POST':
            #if request.GET.get('api') == 'unblock_siebel':
                #try:
                    #import cx_Oracle
                    #db = DBConnection.objects.filter(name='siebel', organization__pk=self.request.session.get('organization')).first()
                    #con = cx_Oracle.connect(db.db_name+'/'+db.db_password+'@'+db.db_host+'/'+db.db_user, encoding = "UTF-8", nencoding = "UTF-8")
                    #con.autocommit = True
                    #cursor = con.cursor()
                    #query = "update siebline.S_ASSET set status_cd='Análisis' where asset_num='{0}'".format(request.POST.get('unblock_number'))
                    #cursor.execute(query)
                    #cursor.close()
                    #message, api = 'Solicitud atendida', 'success' 
                #except Exception as e:
                    #message, api = str(e), 'error' 
            #return JsonResponse({'message':message,'api':api})
        #return super().dispatch(request, *args, **kwargs)
    ############################################################################################
    #def proccess_context(self, context):
        #context['object'] = self.model
        #return context
