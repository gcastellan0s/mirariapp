# -*- coding: utf-8 -*-
from mirari.mirari.views import *
from .models import *
from .vars import *	

class SiebelUnblock__SiebelUnblock__TemplateView(Generic__TemplateView):
	model = apps.get_model(APP, 'SiebelUnblock')
	template_name = "SiebelUnblock__TemplateView.html"
	@method_decorator(csrf_exempt)
	def dispatch(self, request, *args, **kwargs):
		message, api = 'Hay un error en tu consulta', 'error' 
		if request.method == 'POST':
			if request.GET.get('api') == 'unblock_siebel':
				try:
					import cx_Oracle
					db = DBConnection.objects.filter(name='siebel', organization__pk=self.request.session.get('organization')).first()
					con = cx_Oracle.connect(db.db_name+'/'+db.db_password+'@'+db.db_host+'/'+db.db_user, encoding = "UTF-8", nencoding = "UTF-8")
					con.autocommit = True
					cursor = con.cursor()
					query = "update siebline.S_ASSET set status_cd='Análisis' where asset_num='{0}'".format(request.POST.get('unblock_number'))
					cursor.execute(query)
					cursor.close()
					message, api = 'Solicitud atendida', 'success' 
				except Exception as e:
					message, api = str(e), 'error' 
			return JsonResponse({'message':message,'api':api})
		return super().dispatch(request, *args, **kwargs)
	###############################################################################################
	def proccess_context(self, context):
		context['object'] = self.model
		return context
	
class TablaAmortizacion__TemplateView(Generic__TemplateView):
	model = apps.get_model(APP, 'TablaAmortizacion')
	template_name = "TablaAmortizacion__TemplateView.html"
	@method_decorator(csrf_exempt)
	def dispatch(self, request, *args, **kwargs):
		message, api = 'Hay un error en tu consulta', 'error' 
		if request.method == 'POST':
			if request.GET.get('api') == 'getTablaAmortizacion':
				#try:
				import cx_Oracle
				db = DBConnection.objects.filter(name='siebel', organization__pk=self.request.session.get('organization')).first()
				con = cx_Oracle.connect(db.db_name+'/'+db.db_password+'@'+db.db_host+'/'+db.db_user, encoding = "UTF-8", nencoding = "UTF-8")
				con.autocommit = True

				cursor = con.cursor()
				query = "SELECT ref_number_3,owner_accnt_id,PR_CON_ID FROM siebline.S_ASSET WHERE asset_num='{0}'".format(request.POST.get('number'))
				cursor.execute(query)
				response1 = cursor.fetchone()
				cursor.close()

				if response1[0] == 'Moral':
					query = "select DISTINCT SIEBLINE.S_PARTY.ROW_ID AS CLAVE_CTE, 'Persona Moral' as REGIMEN, SIEBLINE.S_ORG_EXT.OU_NUM as RFC,  SIEBLINE.S_ORG_EXT.NAME as NOMBRE, 'PATERNO' as APATERNO, 'MATERNO' as AMATERNO, 'CURP' as CURP, 'MATERNO' as AMATERNO, 'FECHA NACIMIENTP' as FNACIMIENTO, 'MEXICANA' as NACIONALIDAD, SIEBLINE.S_ORG_EXT.PAY_TYPE_CD as GIRO, SIEBLINE.S_ADDR_PER.ADDR as CALLE, SIEBLINE.S_ZIPCODE.STREET_ABBREV as COLONIA, SIEBLINE.S_ADDR_PER.ADDR_NUM as NUMERO_INTERIOR, SIEBLINE.S_ADDR_PER.ZIPCODE as CP, SIEBLINE.S_ZIPCODE.COUNTY as DEL_MUNI, SIEBLINE.S_ZIPCODE.CITY as CIUDAD, SIEBLINE.S_ZIPCODE.STATE_PROV as ESTADO, SIEBLINE.S_CONTACT.FST_NAME as NOMBRECONTACTO, SIEBLINE.S_CONTACT.LAST_NAME as APCONTACTO, SIEBLINE.S_CONTACT.MOTHER_MAIDEN_NAME as AMCONTACTO, SIEBLINE.S_CONTACT.HOME_PH_NUM as TELCONTACTO from SIEBLINE.S_ASSET, SIEBLINE.S_ORG_EXT,SIEBLINE.S_ADDR_PER,SIEBLINE.S_PARTY,SIEBLINE.S_ZIPCODE,SIEBLINE.S_CONTACT where SIEBLINE.S_ASSET.OWNER_ACCNT_ID=SIEBLINE.S_ORG_EXT.PAR_ROW_ID and SIEBLINE.S_ASSET.OWNER_ACCNT_ID=SIEBLINE.S_ORG_EXT.PAR_ROW_ID and SIEBLINE.S_ASSET.OWNER_ACCNT_ID=SIEBLINE.S_PARTY.ROW_ID and SIEBLINE.S_ORG_EXT.PR_ADDR_ID=SIEBLINE.S_ADDR_PER.ROW_ID and SIEBLINE.S_ADDR_PER.ADDR_LINE_5=SIEBLINE.S_ZIPCODE.ROW_ID and SIEBLINE.S_CONTACT.ROW_ID=SIEBLINE.S_ASSET.PR_CON_ID and  SIEBLINE.S_ASSET.OWNER_ACCNT_ID='{0}'".format(response1[1])
				else:
					query = "select SIEBLINE.S_CONTACT.ROW_ID AS CLAVE_CTE, 'Persona Fisica' as REGIMEN, SIEBLINE.S_CONTACT.SOC_SECURITY_NUM AS  RFC,  'Razon Social' as RAZON, SIEBLINE.S_CONTACT.LAST_NAME as APATERNO, SIEBLINE.S_CONTACT.MOTHER_MAIDEN_NAME as AMATERNO, SIEBLINE.S_CONTACT.FST_NAME as NOMBRE, SIEBLINE.S_CONTACT_FNX.IDEN2_NUM as CURP, to_char(SIEBLINE.S_CONTACT.BIRTH_DT,'yyyy-mm-dd') as BIRTH, SIEBLINE.S_CONTACT_FNX.INVST_KNWLDG_CD as NACIONALIDAD,   SIEBLINE.S_CONTACT_X.X_ATTRIB_67 as GIRO2, SIEBLINE.S_ADDR_PER.ADDR as CALLE, SIEBLINE.S_ZIPCODE.STREET_ABbREV AS COLONIA, SIEBLINE.S_ADDR_PER.ADDR_NUM as NUMERO_INTERIOR, SIEBLINE.S_ADDR_PER.ZIPCODE as CP,  SIEBLINE.S_ZIPCODE.COUNTY as DEL_MUNI, SIEBLINE.S_ZIPCODE.CITY as CIUDAD, SIEBLINE.S_ZIPCODE.STATE_PROV as ESTADO, SIEBLINE.S_CONTACT_X.GENERO as GENERO, SIEBLINE.S_CONTACT.HOME_PH_NUM as TELEFONO from SIEBLINE.S_CONTACT, SIEBLINE.S_CONTACT_FNX, SIEBLINE.S_CONTACT_X, SIEBLINE.S_ADDR_PER, SIEBLINE.S_CON_ADDR, SIEBLINE.S_ZIPCODE where  SIEBLINE.S_CONTACT.ROW_ID=SIEBLINE.S_CONTACT_FNX.ROW_ID and SIEBLINE.S_CONTACT.ROW_ID=SIEBLINE.S_CONTACT_X.ROW_ID and SIEBLINE.S_CONTACT.ROW_ID=SIEBLINE.S_CON_ADDR.CONTACT_ID and SIEBLINE.S_CON_ADDR.ADDR_PER_ID=SIEBLINE.S_ADDR_PER.ROW_ID AND SIEBLINE.S_ADDR_PER.ADDR_LINE_5=SIEBLINE.S_ZIPCODE.ROW_ID and SIEBLINE.S_CONTACT.ROW_ID ='{0}'".format(response1[1])
				cursor = con.cursor()
				cursor.execute(query)
				response2 = cursor.fetchone()
				cursor.close()

				message, api = 'Solicitud atendida', 'success' 
				#except Exception as e:
					#message, api = str(e), 'error' 
			return JsonResponse({'message':message,'api':api, 'query':query, 'response1':response1, 'response2':response2})
		return super().dispatch(request, *args, **kwargs)
	###############################################################################################
	def proccess_context(self, context):
		context['object'] = self.model
		return context