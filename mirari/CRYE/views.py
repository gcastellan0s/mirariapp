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
		walletcredit = WalletCredit.objects.get(id=kwargs['pk'])

		import cx_Oracle
		db = DBConnection.objects.filter(name='siebel', organization__pk=self.request.session.get('organization')).first()
		con = cx_Oracle.connect(db.db_name+'/'+db.db_password+'@'+db.db_host+'/'+db.db_user, encoding = "UTF-8", nencoding = "UTF-8")
		con.autocommit = True
		cursor = con.cursor()
		query = "SELECT ref_number_3,owner_accnt_id,PR_CON_ID, ROW_ID FROM siebline.S_ASSET WHERE asset_num='{0}'".format(walletcredit.obligacion)
		cursor.execute(query)
		self.response1 = cursor.fetchone()
		cursor.close()
		if response1[0] == 'Moral':
			query = "select DISTINCT SIEBLINE.S_PARTY.ROW_ID AS CLAVE_CTE, 'Persona Moral' as REGIMEN, SIEBLINE.S_ORG_EXT.OU_NUM as RFC,  SIEBLINE.S_ORG_EXT.NAME as NOMBRE, 'PATERNO' as APATERNO, 'MATERNO' as AMATERNO, 'CURP' as CURP, 'MATERNO' as AMATERNO, 'FECHA NACIMIENTP' as FNACIMIENTO, 'MEXICANA' as NACIONALIDAD, SIEBLINE.S_ORG_EXT.PAY_TYPE_CD as GIRO, SIEBLINE.S_ADDR_PER.ADDR as CALLE, SIEBLINE.S_ZIPCODE.STREET_ABBREV as COLONIA, SIEBLINE.S_ADDR_PER.ADDR_NUM as NUMERO_INTERIOR, SIEBLINE.S_ADDR_PER.ZIPCODE as CP, SIEBLINE.S_ZIPCODE.COUNTY as DEL_MUNI, SIEBLINE.S_ZIPCODE.CITY as CIUDAD, SIEBLINE.S_ZIPCODE.STATE_PROV as ESTADO, SIEBLINE.S_CONTACT.FST_NAME as NOMBRECONTACTO, SIEBLINE.S_CONTACT.LAST_NAME as APCONTACTO, SIEBLINE.S_CONTACT.MOTHER_MAIDEN_NAME as AMCONTACTO, SIEBLINE.S_CONTACT.HOME_PH_NUM as TELCONTACTO from SIEBLINE.S_ASSET, SIEBLINE.S_ORG_EXT,SIEBLINE.S_ADDR_PER,SIEBLINE.S_PARTY,SIEBLINE.S_ZIPCODE,SIEBLINE.S_CONTACT where SIEBLINE.S_ASSET.OWNER_ACCNT_ID=SIEBLINE.S_ORG_EXT.PAR_ROW_ID and SIEBLINE.S_ASSET.OWNER_ACCNT_ID=SIEBLINE.S_ORG_EXT.PAR_ROW_ID and SIEBLINE.S_ASSET.OWNER_ACCNT_ID=SIEBLINE.S_PARTY.ROW_ID and SIEBLINE.S_ORG_EXT.PR_ADDR_ID=SIEBLINE.S_ADDR_PER.ROW_ID and SIEBLINE.S_ADDR_PER.ADDR_LINE_5=SIEBLINE.S_ZIPCODE.ROW_ID and SIEBLINE.S_CONTACT.ROW_ID=SIEBLINE.S_ASSET.PR_CON_ID and  SIEBLINE.S_ASSET.OWNER_ACCNT_ID='{0}'".format(response1[1])
		else:
			query = "select SIEBLINE.S_CONTACT.ROW_ID AS CLAVE_CTE, 'Persona Fisica' as REGIMEN, SIEBLINE.S_CONTACT.SOC_SECURITY_NUM AS  RFC,  'Razon Social' as RAZON, SIEBLINE.S_CONTACT.LAST_NAME as APATERNO, SIEBLINE.S_CONTACT.MOTHER_MAIDEN_NAME as AMATERNO, SIEBLINE.S_CONTACT.FST_NAME as NOMBRE, SIEBLINE.S_CONTACT_FNX.IDEN2_NUM as CURP, to_char(SIEBLINE.S_CONTACT.BIRTH_DT,'yyyy-mm-dd') as BIRTH, SIEBLINE.S_CONTACT_FNX.INVST_KNWLDG_CD as NACIONALIDAD,   SIEBLINE.S_CONTACT_X.X_ATTRIB_67 as GIRO2, SIEBLINE.S_ADDR_PER.ADDR as CALLE, SIEBLINE.S_ZIPCODE.STREET_ABbREV AS COLONIA, SIEBLINE.S_ADDR_PER.ADDR_NUM as NUMERO_INTERIOR, SIEBLINE.S_ADDR_PER.ZIPCODE as CP,  SIEBLINE.S_ZIPCODE.COUNTY as DEL_MUNI, SIEBLINE.S_ZIPCODE.CITY as CIUDAD, SIEBLINE.S_ZIPCODE.STATE_PROV as ESTADO, SIEBLINE.S_CONTACT_X.GENERO as GENERO, SIEBLINE.S_CONTACT.HOME_PH_NUM as TELEFONO from SIEBLINE.S_CONTACT, SIEBLINE.S_CONTACT_FNX, SIEBLINE.S_CONTACT_X, SIEBLINE.S_ADDR_PER, SIEBLINE.S_CON_ADDR, SIEBLINE.S_ZIPCODE where  SIEBLINE.S_CONTACT.ROW_ID=SIEBLINE.S_CONTACT_FNX.ROW_ID and SIEBLINE.S_CONTACT.ROW_ID=SIEBLINE.S_CONTACT_X.ROW_ID and SIEBLINE.S_CONTACT.ROW_ID=SIEBLINE.S_CON_ADDR.CONTACT_ID and SIEBLINE.S_CON_ADDR.ADDR_PER_ID=SIEBLINE.S_ADDR_PER.ROW_ID AND SIEBLINE.S_ADDR_PER.ADDR_LINE_5=SIEBLINE.S_ZIPCODE.ROW_ID and SIEBLINE.S_CONTACT.ROW_ID ='{0}'".format(response1[2])
		cursor = con.cursor()
		cursor.execute(query)
		self.response2 = cursor.fetchone()
		cursor.close()
		query = "select ACC.X_ORIGINAL_IMPORTE_SIN_IVA MONTO_ORIGINAL, ACC.X_ORIGINAL_NUMERO_AMORTIZACION as NUMERO_AMORTIZACIONES, AX.X_ATTRIB_95 as FECHA_LIBERACION, AX.ATTRIB_07 as ROWAM from S_FN_ACCNT1_FNX ACC, S_ASSET_X AX where ACC.par_row_id='{0}' and ACC.PAR_ROW_ID=AX.PAR_ROW_ID".format(response1[3])
		cursor = con.cursor()
		cursor.execute(query)
		self.response3 = cursor.fetchone()
		cursor.close()
		query = "select ACCUM_VAL NUM_PAGO,to_char(END_DT,'DD/MM/YYYY') FECHA,X_ESTATUS_FACTURA STATUS,END_BALANCE INSOLUTO,CASH_SURRENDER_VAL CAPITAL,INTEREST_PAID INTERESES,FEE_PAID RENTA, HIGH_BALANCE PAGADO from S_FN_ACCNT_BAL where X_CLAVE_PH like '{0}%' order by ACCUM_VAL".format(response1[3])
		cursor = con.cursor()
		cursor.execute(query)
		self.response4 = cursor.fetchall()
		cursor.close()
		
		for field in response4:
			tablaamortizacion = TablaAmortizacion.objects.filter(walletcredit=walletcredit, numeroPago=field[0]).first()
			if not tablaamortizacion:
				tablaamortizacion = TablaAmortizacion()
				tablaamortizacion.walletcredit = walletcredit
				tablaamortizacion.numeroPago = field[0]
				tablaamortizacion.date = datetime.datetime.strptime(field[1], '%d/%m/%Y')
				tablaamortizacion.estatus = field[2]
				tablaamortizacion.balanceInsoluto = field[3]
				tablaamortizacion.capital = field[4]
				tablaamortizacion.intereses = field[5]
				tablaamortizacion.renta = field[6]
				tablaamortizacion.pagado = field[7]
				tablaamortizacion.save()
		#if request.method == 'POST':
			#if request.GET.get('api') == 'getTablaAmortizacion':
				#try:
					######
					#walletCredit = WalletCredit.objects.filter(obligacion = request.POST.get('number'), organization = self.request.session.get('organization')).first()
					#if not walletCredit:
						#walletCredit = WalletCredit()
					#walletCredit.organization = Organization.objects.get(id=self.request.session.get('organization'))
					#walletCredit.obligacion = request.POST.get('number')
					#walletCredit.clasificacion = None
					#walletCredit.clasificacion_contable = None
					#walletCredit.tipo = response2[1]
					#walletCredit.nombre = response2[3]
					#walletCredit.rfc = response2[2]
					#walletCredit.producto = None
					#walletCredit.forma_pago = None
					#walletCredit.tipo_tasa = None
					#walletCredit.tasa = None
					#walletCredit.fecha_otorgado = None
					#walletCredit.fecha_vencimiento = None
					#walletCredit.plazo = int(response3[1])
					#walletCredit.monto = float(response3[0])
					#walletCredit.fondeador = None
					#walletCredit.save()
					#return JsonResponse({'query':query, 'response1':response1, 'response2':response2, 'response3':response3, 'response4':response4})
				#except Exception as e:
					#return JsonResponse({'message':str(e)})
				
		return super().dispatch(request, *args, **kwargs)
	###############################################################################################
	def proccess_context(self, context):
		context['object'] = self.model
		context['response1'] = self.response1
		context['response2'] = self.response2
		context['response3'] = self.response3
		context['response4'] = self.response4
		return context