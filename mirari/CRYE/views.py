# -*- coding: utf-8 -*-
from mirari.mirari.views import *
from .models import *
from .vars import *	

###############################################################################################
# SiebelUnblock ###############################################################################
###############################################################################################
class SiebelUnblock__SiebelUnblock__TemplateView(Generic__TemplateView):
    model = apps.get_model(APP, 'SiebelUnblock')
    template_name = "SiebelUnblock__TemplateView.html"
    ###########################################################################################
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
    ###########################################################################################
    def proccess_context(self, context):
        context['object'] = self.model
        return context


###############################################################################################
# WalletCredit ################################################################################
###############################################################################################
class WalletCredit__TemplateView(Generic__TemplateView):
    model = apps.get_model(APP, 'WalletCredit')
    template_name = "WalletCredit__TemplateView.html"
    ###########################################################################################
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        try:
            if request.method == 'POST':
                import cx_Oracle
                if request.POST.get('type') == 'CREDITO':
                    db = DBConnection.objects.filter(name='siebel', organization__pk=self.request.session.get('organization')).first()
                    con = cx_Oracle.connect(db.db_name+'/'+db.db_password+'@'+db.db_host+'/'+db.db_user, encoding = "UTF-8", nencoding = "UTF-8")
                    con.autocommit = True
                    cursor = con.cursor()
                    query = "SELECT ref_number_3,owner_accnt_id,PR_CON_ID, ROW_ID FROM siebline.S_ASSET WHERE asset_num='{0}'".format(request.POST.get('id'))
                    cursor.execute(query)
                    response1 = cursor.fetchone()
                    cursor.close()
                    if response1[0] == 'Moral':
                        query = "select DISTINCT SIEBLINE.S_PARTY.ROW_ID AS CLAVE_CTE, 'Persona Moral' as REGIMEN, SIEBLINE.S_ORG_EXT.OU_NUM as RFC,  SIEBLINE.S_ORG_EXT.NAME as NOMBRE, 'PATERNO' as APATERNO, 'MATERNO' as AMATERNO, 'CURP' as CURP, 'MATERNO' as AMATERNO, 'FECHA NACIMIENTP' as FNACIMIENTO, 'MEXICANA' as NACIONALIDAD, SIEBLINE.S_ORG_EXT.PAY_TYPE_CD as GIRO, SIEBLINE.S_ADDR_PER.ADDR as CALLE, SIEBLINE.S_ZIPCODE.STREET_ABBREV as COLONIA, SIEBLINE.S_ADDR_PER.ADDR_NUM as NUMERO_INTERIOR, SIEBLINE.S_ADDR_PER.ZIPCODE as CP, SIEBLINE.S_ZIPCODE.COUNTY as DEL_MUNI, SIEBLINE.S_ZIPCODE.CITY as CIUDAD, SIEBLINE.S_ZIPCODE.STATE_PROV as ESTADO, SIEBLINE.S_CONTACT.FST_NAME as NOMBRECONTACTO, SIEBLINE.S_CONTACT.LAST_NAME as APCONTACTO, SIEBLINE.S_CONTACT.MOTHER_MAIDEN_NAME as AMCONTACTO, SIEBLINE.S_CONTACT.HOME_PH_NUM as TELCONTACTO from SIEBLINE.S_ASSET, SIEBLINE.S_ORG_EXT,SIEBLINE.S_ADDR_PER,SIEBLINE.S_PARTY,SIEBLINE.S_ZIPCODE,SIEBLINE.S_CONTACT where SIEBLINE.S_ASSET.OWNER_ACCNT_ID=SIEBLINE.S_ORG_EXT.PAR_ROW_ID and SIEBLINE.S_ASSET.OWNER_ACCNT_ID=SIEBLINE.S_ORG_EXT.PAR_ROW_ID and SIEBLINE.S_ASSET.OWNER_ACCNT_ID=SIEBLINE.S_PARTY.ROW_ID and SIEBLINE.S_ORG_EXT.PR_ADDR_ID=SIEBLINE.S_ADDR_PER.ROW_ID and SIEBLINE.S_ADDR_PER.ADDR_LINE_5=SIEBLINE.S_ZIPCODE.ROW_ID and SIEBLINE.S_CONTACT.ROW_ID=SIEBLINE.S_ASSET.PR_CON_ID and  SIEBLINE.S_ASSET.OWNER_ACCNT_ID='{0}'".format(response1[1])
                    else:
                        query = "select SIEBLINE.S_CONTACT.ROW_ID AS CLAVE_CTE, 'Persona Fisica' as REGIMEN, SIEBLINE.S_CONTACT.SOC_SECURITY_NUM AS  RFC,  'Razon Social' as RAZON, SIEBLINE.S_CONTACT.LAST_NAME as APATERNO, SIEBLINE.S_CONTACT.MOTHER_MAIDEN_NAME as AMATERNO, SIEBLINE.S_CONTACT.FST_NAME as NOMBRE, SIEBLINE.S_CONTACT_FNX.IDEN2_NUM as CURP, to_char(SIEBLINE.S_CONTACT.BIRTH_DT,'yyyy-mm-dd') as BIRTH, SIEBLINE.S_CONTACT_FNX.INVST_KNWLDG_CD as NACIONALIDAD,   SIEBLINE.S_CONTACT_X.X_ATTRIB_67 as GIRO2, SIEBLINE.S_ADDR_PER.ADDR as CALLE, SIEBLINE.S_ZIPCODE.STREET_ABbREV AS COLONIA, SIEBLINE.S_ADDR_PER.ADDR_NUM as NUMERO_INTERIOR, SIEBLINE.S_ADDR_PER.ZIPCODE as CP,  SIEBLINE.S_ZIPCODE.COUNTY as DEL_MUNI, SIEBLINE.S_ZIPCODE.CITY as CIUDAD, SIEBLINE.S_ZIPCODE.STATE_PROV as ESTADO, SIEBLINE.S_CONTACT_X.GENERO as GENERO, SIEBLINE.S_CONTACT.HOME_PH_NUM as TELEFONO from SIEBLINE.S_CONTACT, SIEBLINE.S_CONTACT_FNX, SIEBLINE.S_CONTACT_X, SIEBLINE.S_ADDR_PER, SIEBLINE.S_CON_ADDR, SIEBLINE.S_ZIPCODE where  SIEBLINE.S_CONTACT.ROW_ID=SIEBLINE.S_CONTACT_FNX.ROW_ID and SIEBLINE.S_CONTACT.ROW_ID=SIEBLINE.S_CONTACT_X.ROW_ID and SIEBLINE.S_CONTACT.ROW_ID=SIEBLINE.S_CON_ADDR.CONTACT_ID and SIEBLINE.S_CON_ADDR.ADDR_PER_ID=SIEBLINE.S_ADDR_PER.ROW_ID AND SIEBLINE.S_ADDR_PER.ADDR_LINE_5=SIEBLINE.S_ZIPCODE.ROW_ID and SIEBLINE.S_CONTACT.ROW_ID ='{0}'".format(response1[2])
                    cursor = con.cursor()
                    cursor.execute(query)
                    response2 = cursor.fetchone()
                    cursor.close()
                    query = "select ACC.X_ORIGINAL_IMPORTE_SIN_IVA MONTO_ORIGINAL, ACC.X_ORIGINAL_NUMERO_AMORTIZACION as NUMERO_AMORTIZACIONES, AX.X_ATTRIB_95 as FECHA_LIBERACION, AX.ATTRIB_07 as ROWAM from S_FN_ACCNT1_FNX ACC, S_ASSET_X AX where ACC.par_row_id='{0}' and ACC.PAR_ROW_ID=AX.PAR_ROW_ID".format(response1[3])
                    cursor = con.cursor()
                    cursor.execute(query)
                    response3 = cursor.fetchone()
                    cursor.close()
                    query = "select ACCUM_VAL NUM_PAGO,to_char(END_DT,'DD/MM/YYYY') FECHA,X_ESTATUS_FACTURA STATUS,END_BALANCE INSOLUTO,CASH_SURRENDER_VAL CAPITAL,INTEREST_PAID INTERESES,FEE_PAID RENTA, HIGH_BALANCE PAGADO from S_FN_ACCNT_BAL where X_CLAVE_PH like '{0}%' order by ACCUM_VAL".format(response1[3])
                    cursor = con.cursor()
                    cursor.execute(query)
                    response4 = cursor.fetchall()
                    cursor.close()
                    walletCredit = WalletCredit.objects.filter(obligacion = request.POST.get('id'), organization = self.request.session.get('organization')).first()
                    if not walletCredit:
                        walletCredit = WalletCredit()
                    walletCredit.organization = Organization.objects.get(id=self.request.session.get('organization'))
                    walletCredit.obligacion = request.POST.get('id')
                    walletCredit.clasificacion = None
                    walletCredit.clasificacion_contable = None
                    walletCredit.tipo = response2[1]
                    walletCredit.nombre = response2[3]
                    walletCredit.rfc = response2[2]
                    walletCredit.producto = None
                    walletCredit.forma_pago = None
                    walletCredit.tipo_tasa = None
                    walletCredit.tasa = None
                    walletCredit.fecha_otorgado = None
                    walletCredit.fecha_vencimiento = None
                    walletCredit.plazo = int(response3[1])
                    walletCredit.monto = float(response3[0])
                    walletCredit.fondeador = None
                    walletCredit.save()
                    for field in response4:
                        tablaamortizacion = TablaAmortizacion.objects.filter(walletcredit=walletCredit, numeroPago=field[0]).first()
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
                elif request.POST.get('type') == 'ARRENDAMIENTO':
                    dsnStr = cx_Oracle.makedsn("187.217.173.14", "1521", "CREDIPRO")
                    con = cx_Oracle.connect(user="java_core", password="JAVA_CORE", dsn=dsnStr, encoding = "UTF-8", nencoding = "UTF-8")
                    message = con.version
                    con.autocommit = True
                    query = "select SIEBPLINE.S_OPTY.ROW_ID as SOL_ID, SIEBPLINE.S_OPTY.NAME as SOLICITUD, decode(SIEBPLINE.S_OPTY.PR_DEPT_OU_ID,'No Match Row Id',SIEBPLINE.S_OPTY.PR_CON_ID,SIEBPLINE.S_OPTY.PR_DEPT_OU_ID) as IDCLIENTE, decode(SIEBPLINE.S_OPTY.PR_DEPT_OU_ID,'No Match Row Id','Persona Fisica','Persona Moral') as TIPO_PERSONA, decode(SIEBPLINE.S_OPTY.PR_DEPT_OU_ID,'No Match Row Id',SIEBPLINE.S_CONTACT.FST_NAME || ' ' || SIEBPLINE.S_CONTACT.LAST_NAME,SIEBPLINE.S_ORG_EXT.NAME) as TIPO_PERSONA1, SIEBPLINE.S_REVN.PROD_ID, SIEBPLINE.S_PROD_INT.PART_NUM as PRODUCTO,  SIEBPLINE.S_PROD_INT.DESC_TEXT as DATOS_EXTRA, SIEBPLINE.S_FN_OFFR_FEE.BASIS_PERCENT TASA_COMISIONES, SIEBPLINE.S_REVN.REVN_AMT as LIMITE_CREDITO, DECODE(SIEBPLINE.S_OPTY_PROD_FNX.FIXED_RATE_FLG,'Y',SIEBPLINE.S_OPTY_PROD_FNX.LN_APPR_INT_RATE,SIEBPLINE.S_FN_INDEX_RATE.INDEX_VAL + SIEBPLINE.S_OPTY_PROD_FNX.RATE_SPREAD) as INTERES_ORDINARIO, DECODE(SIEBPLINE.S_OPTY_PROD_FNX.FIXED_RATE_FLG,'Y',0, SIEBPLINE.S_OPTY_PROD_FNX.RATE_SPREAD) as PUNTOS_EXTRA, SIEBPLINE.S_PROD_INT_TNTX.CONSUMP_UOM_PP_NUM FACTOR_MORATORIOS, nvl(SIEBPLINE.S_OPTY_PROD1_FNX.AS_PAYFREQ_CD,'Días') as TIPO_PLAZO, decode(SIEBPLINE.S_REVN.PROD_ID,'1-2XFB',SIEBPLINE.S_OPTY_PROD_FNX.FST_PAYMNT_DT-SIEBPLINE.S_OPTY_PROD_FNX.INTRST_START_DT, '1-4YRV',SIEBPLINE.S_OPTY_PROD_FNX.FST_PAYMNT_DT-SIEBPLINE.S_OPTY_PROD_FNX.INTRST_START_DT, SIEBPLINE.S_OPTY_PROD_FNX.LN_AMORT_NUM_MTH) as PLAZO from SIEBPLINE.S_OPTY, SIEBPLINE.S_REVN, SIEBPLINE.S_PROD_INT, SIEBPLINE.S_PROD_INT_TNTX, SIEBPLINE.S_FN_OFFR_FEE,  SIEBPLINE.S_OPTY_PROD_FNX, SIEBPLINE.S_FN_INDEX_RATE, SIEBPLINE.S_OPTY_PROD1_FNX, SIEBPLINE.S_CONTACT, SIEBPLINE.S_ORG_EXT where SIEBPLINE.S_OPTY.ROW_ID = SIEBPLINE.S_REVN.OPTY_ID and SIEBPLINE.S_OPTY.PR_OPTYPRD_ID = SIEBPLINE.S_REVN.ROW_ID and SIEBPLINE.S_REVN.PROD_ID = SIEBPLINE.S_PROD_INT.ROW_ID and SIEBPLINE.S_PROD_INT.ROW_ID = SIEBPLINE.S_PROD_INT_TNTX.PAR_ROW_ID and SIEBPLINE.S_REVN.INDEX_RATE_ID=SIEBPLINE.S_FN_INDEX_RATE.ROW_ID(+) and SIEBPLINE.S_REVN.PR_LOAN_FEE_ID = SIEBPLINE.S_FN_OFFR_FEE.ROW_ID(+) and SIEBPLINE.S_OPTY.PR_OPTYPRD_ID = SIEBPLINE.S_OPTY_PROD_FNX.ROW_ID and SIEBPLINE.S_OPTY.PR_OPTYPRD_ID = SIEBPLINE.S_OPTY_PROD1_FNX.ROW_ID(+) and SIEBPLINE.S_OPTY.PR_CON_ID = SIEBPLINE.S_CONTACT.ROW_ID(+) and SIEBPLINE.S_OPTY.PR_DEPT_OU_ID = SIEBPLINE.S_ORG_EXT.ROW_ID(+)"
                    cursor = con.cursor()
                    cursor.execute(query)
                    response1 = cursor.fetchall()
                    cursor.close()
                    for client in response1:
                        query = "select * from java_core.creditos where creditos.id_solicitud='{0}'".format(request.POST.get('unblock_number'))

                    #query = "select SIEBPLINE.S_ORG_EXT.ROW_ID as CLIENTE, 'Persona Moral' as REGIMEN, REPLACE(REPLACE(SIEBPLINE.S_ORG_EXT.ALIAS_NAME,'-',''),' ','') as RFC, SIEBPLINE.S_ORG_EXT.NAME as RAZON_SOCIAL, SIEBPLINE.S_ORG_EXT.URL as GIRO, SIEBPLINE.S_ADDR_PER.ADDR as CALLE, SIEBPLINE.S_ADDR_PER.PROVINCE as COLONIA, '' as NUM_INT, '' as NUM_EXT, 'Persona Moral' as REGIMEN, 'Mexicana' as NACIONALIDAD, 'Mexicana' as TELCONTACTO, 'N/A' as NUMERO_INTERIOR, SIEBPLINE.S_ADDR_PER.ZIPCODE as CP, SIEBPLINE.S_ADDR_PER.COUNTY as MUNICIPIO, SIEBPLINE.S_ADDR_PER.CITY as CIUDAD, SIEBPLINE.S_ADDR_PER.STATE as ESTADO, SUBSTR(SIEBPLINE.S_ORG_EXT.MAIN_PH_NUM,4) as TELEFONO, SIEBPLINE.S_CONTACT.FST_NAME || ' ' || SIEBPLINE.S_CONTACT.LAST_NAME as NOMBRE_CONTACTO, SIEBPLINE.S_ADDR_PER.COUNTRY as PAIS from SIEBPLINE.S_ORG_EXT, SIEBPLINE.S_ADDR_PER, SIEBPLINE.S_ORG_EXT_FNX, SIEBPLINE.S_CONTACT where  SIEBPLINE.S_ORG_EXT.PR_ADDR_ID=SIEBPLINE.S_ADDR_PER.ROW_ID(+) and SIEBPLINE.S_ORG_EXT.ROW_ID = SIEBPLINE.S_ORG_EXT_FNX.PAR_ROW_ID and SIEBPLINE.S_ORG_EXT.PR_CON_ID = SIEBPLINE.S_CONTACT.PAR_ROW_ID(+) and  SIEBPLINE.S_ORG_EXT.ROW_ID='{0}'".format(request.POST.get('unblock_number'))
                    #query = "select SIEBPLINE.S_CONTACT.ROW_ID as IDCLIENTE, 'Persona Fisica' as REGIMEN, REPLACE(REPLACE(SIEBPLINE.S_CONTACT.ALIAS_NAME,'-',''),' ','') as RFC, SIEBPLINE.S_CONTACT.LAST_NAME as APELLIDOS, SIEBPLINE.S_CONTACT.FST_NAME as NOMBRE, SIEBPLINE.S_CONTACT_FNX.IDEN2_NUM as CURP, TO_CHAR(SIEBPLINE.S_CONTACT.BIRTH_DT,'YYYY-MM-DD') as FECHA_NACIMIENTO, SIEBPLINE.S_CONTACT.NATIONALITY as NACIONALIDAD, SIEBPLINE.S_CONTACT_X.ATTRIB_34 as GIRO, SIEBPLINE.S_CONTACT.PR_PER_ADDR_ID, SIEBPLINE.S_ADDR_PER.ADDR as CALLE, SIEBPLINE.S_ADDR_PER.PROVINCE as COLONIA, '' as NUM_INT, '' as NUM_EXT, SIEBPLINE.S_ADDR_PER.ZIPCODE as CP, SIEBPLINE.S_ADDR_PER.COUNTY as MUNICIPIO, SIEBPLINE.S_ADDR_PER.CITY as CIUDAD, SIEBPLINE.S_ADDR_PER.STATE as ESTADO, SUBSTR(SIEBPLINE.S_CONTACT.WORK_PH_NUM,4) as TELEFONO, SIEBPLINE.S_CONTACT.FST_NAME || ' ' || SIEBPLINE.S_CONTACT.LAST_NAME as NOMBRE_CONTACTO, SIEBPLINE.S_CONTACT.SEX_MF as SEXO, SIEBPLINE.S_CONTACT.MARITAL_STAT_CD as EDO_CIVIL, SIEBPLINE.S_CONTACT_FNX.BIRTH_PLACE as LUGAR_NACIMIENTO, SIEBPLINE.S_ADDR_PER.COUNTRY as PAIS, '' as FIEL, '' as NIE, SIEBPLINE.S_CONTACT.EMAIL_ADDR as CORREO from SIEBPLINE.S_CONTACT,  SIEBPLINE.S_CONTACT_X,  SIEBPLINE.S_ADDR_PER,  SIEBPLINE.S_CONTACT_FNX where SIEBPLINE.S_CONTACT.ROW_ID = SIEBPLINE.S_CONTACT_X.PAR_ROW_ID and SIEBPLINE.S_CONTACT.ROW_ID = SIEBPLINE.S_CONTACT_FNX.PAR_ROW_ID and SIEBPLINE.S_CONTACT.PR_PER_ADDR_ID = SIEBPLINE.S_ADDR_PER.ROW_ID(+) and SIEBPLINE.S_CONTACT.ROW_ID='{0}'".format(request.POST.get('unblock_number'))
                    #query = "select * from java_core.creditos where creditos.id_solicitud='{0}'".format(request.POST.get('unblock_number'))
                return JsonResponse({'redirect':walletCredit.url_update()})
        except Exception as e:
            return JsonResponse({'message':str(e)})
        return super().dispatch(request, *args, **kwargs)


class WalletCreditSerializer(Base_Serializer):
    class Meta(Basic_Serializer.Meta):
        model = WalletCredit

class TablaAmortizacionSerializer(Base_Serializer):
    #product = serializers.SerializerMethodField()
    class Meta(Basic_Serializer.Meta):
        model = TablaAmortizacion
    #def get_product(self, obj):
        #return ProductSerializer(obj.product, read_only=True).data

class PagoAmortizacionSerializer(Base_Serializer):
    class Meta(Basic_Serializer.Meta):
        model = PagoAmortizacion

###############################################################################################
# TablaAmortizacion ###########################################################################
###############################################################################################
class TablaAmortizacion__TemplateView(Generic__TemplateView):
    model = apps.get_model(APP, 'TablaAmortizacion')
    template_name = "TablaAmortizacion__TemplateView.html"
    ###########################################################################################
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        self.object = WalletCredit.objects.get(id=kwargs['pk'])
        if request.method == 'POST':
            if request.GET.get('api') == 'addPayment':
                tablaAmortizacion = TablaAmortizacion.objects.get(id=request.POST.get('tablaAmortizacion'))
                pagoAmortizacion = PagoAmortizacion()
                pagoAmortizacion.user = request.user
                pagoAmortizacion.tablaaAmortizacion = tablaAmortizacion
                pagoAmortizacion.capital = request.POST.get('capital', 0)
                pagoAmortizacion.interesVigente = request.POST.get('interesVigente', 0)
                pagoAmortizacion.intereVigenteNoPagado = request.POST.get('intereVigenteNoPagado', 0)
                pagoAmortizacion.interesMoratorio = request.POST.get('interesMoratorio', 0)
                pagoAmortizacion.gastosCobranza = request.POST.get('gastosCobranza', 0)
                pagoAmortizacion.iva = request.POST.get('iva', 0)
                pagoAmortizacion.save()
                return JsonResponse({
                    'walletcredit': WalletCreditSerializer(self.object).data,
                    'tablasamortizaciones': TablaAmortizacionSerializer(TablaAmortizacion.objects.filter(walletcredit=self.object), many=True).data,
                    'pagosamortizacion': PagoAmortizacionSerializer(PagoAmortizacion.objects.filter(tablaaAmortizacion=tablaAmortizacion), many=True).data,
                })
            if request.GET.get('api') == 'getPagosAmortizacion':
                tablaAmortizacion = TablaAmortizacion.objects.get(id=request.POST.get('tablaAmortizacion'))
                return JsonResponse({
                    'pagosamortizacion': PagoAmortizacionSerializer(PagoAmortizacion.objects.filter(tablaaAmortizacion=tablaAmortizacion), many=True).data,
                })
            if request.GET.get('api') == 'getTable':
                return JsonResponse({
                    'walletcredit': WalletCreditSerializer(self.object).data,
                    'tablasamortizaciones': TablaAmortizacionSerializer(TablaAmortizacion.objects.filter(walletcredit=self.object), many=True).data,
                })
        return super().dispatch(request, *args, **kwargs)
    ###########################################################################################
    def proccess_context(self, context):
        context['object'] = self.object
        return context



###############################################################################################
# SiebelUnblock ###############################################################################
###############################################################################################
class TablaAmortizacion2__TemplateView(Generic__TemplateView):
    model = apps.get_model(APP, 'SiebelUnblock')
    template_name = "TablaAmortizacion2__TemplateView.html"
    ###########################################################################################
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        if request.method == 'POST':
            if request.GET.get('api') == 'unblock_siebel':
                try:
                    import cx_Oracle
                    dsnStr = cx_Oracle.makedsn("187.217.173.14", "1521", "CREDIPRO")
                    con = cx_Oracle.connect(user="java_core", password="JAVA_CORE", dsn=dsnStr, encoding = "UTF-8", nencoding = "UTF-8")
                    message = con.version
                    con.autocommit = True
                    query = "select SIEBPLINE.S_OPTY.ROW_ID as SOL_ID, SIEBPLINE.S_OPTY.NAME as SOLICITUD, decode(SIEBPLINE.S_OPTY.PR_DEPT_OU_ID,'No Match Row Id',SIEBPLINE.S_OPTY.PR_CON_ID,SIEBPLINE.S_OPTY.PR_DEPT_OU_ID) as IDCLIENTE, decode(SIEBPLINE.S_OPTY.PR_DEPT_OU_ID,'No Match Row Id','Persona Fisica','Persona Moral') as TIPO_PERSONA, decode(SIEBPLINE.S_OPTY.PR_DEPT_OU_ID,'No Match Row Id',SIEBPLINE.S_CONTACT.FST_NAME || ' ' || SIEBPLINE.S_CONTACT.LAST_NAME,SIEBPLINE.S_ORG_EXT.NAME) as TIPO_PERSONA1, SIEBPLINE.S_REVN.PROD_ID, SIEBPLINE.S_PROD_INT.PART_NUM as PRODUCTO,  SIEBPLINE.S_PROD_INT.DESC_TEXT as DATOS_EXTRA, SIEBPLINE.S_FN_OFFR_FEE.BASIS_PERCENT TASA_COMISIONES, SIEBPLINE.S_REVN.REVN_AMT as LIMITE_CREDITO, DECODE(SIEBPLINE.S_OPTY_PROD_FNX.FIXED_RATE_FLG,'Y',SIEBPLINE.S_OPTY_PROD_FNX.LN_APPR_INT_RATE,SIEBPLINE.S_FN_INDEX_RATE.INDEX_VAL + SIEBPLINE.S_OPTY_PROD_FNX.RATE_SPREAD) as INTERES_ORDINARIO, DECODE(SIEBPLINE.S_OPTY_PROD_FNX.FIXED_RATE_FLG,'Y',0, SIEBPLINE.S_OPTY_PROD_FNX.RATE_SPREAD) as PUNTOS_EXTRA, SIEBPLINE.S_PROD_INT_TNTX.CONSUMP_UOM_PP_NUM FACTOR_MORATORIOS, nvl(SIEBPLINE.S_OPTY_PROD1_FNX.AS_PAYFREQ_CD,'Días') as TIPO_PLAZO, decode(SIEBPLINE.S_REVN.PROD_ID,'1-2XFB',SIEBPLINE.S_OPTY_PROD_FNX.FST_PAYMNT_DT-SIEBPLINE.S_OPTY_PROD_FNX.INTRST_START_DT, '1-4YRV',SIEBPLINE.S_OPTY_PROD_FNX.FST_PAYMNT_DT-SIEBPLINE.S_OPTY_PROD_FNX.INTRST_START_DT, SIEBPLINE.S_OPTY_PROD_FNX.LN_AMORT_NUM_MTH) as PLAZO from SIEBPLINE.S_OPTY, SIEBPLINE.S_REVN, SIEBPLINE.S_PROD_INT, SIEBPLINE.S_PROD_INT_TNTX, SIEBPLINE.S_FN_OFFR_FEE,  SIEBPLINE.S_OPTY_PROD_FNX, SIEBPLINE.S_FN_INDEX_RATE, SIEBPLINE.S_OPTY_PROD1_FNX, SIEBPLINE.S_CONTACT, SIEBPLINE.S_ORG_EXT where SIEBPLINE.S_OPTY.ROW_ID = SIEBPLINE.S_REVN.OPTY_ID and SIEBPLINE.S_OPTY.PR_OPTYPRD_ID = SIEBPLINE.S_REVN.ROW_ID and SIEBPLINE.S_REVN.PROD_ID = SIEBPLINE.S_PROD_INT.ROW_ID and SIEBPLINE.S_PROD_INT.ROW_ID = SIEBPLINE.S_PROD_INT_TNTX.PAR_ROW_ID and SIEBPLINE.S_REVN.INDEX_RATE_ID=SIEBPLINE.S_FN_INDEX_RATE.ROW_ID(+) and SIEBPLINE.S_REVN.PR_LOAN_FEE_ID = SIEBPLINE.S_FN_OFFR_FEE.ROW_ID(+) and SIEBPLINE.S_OPTY.PR_OPTYPRD_ID = SIEBPLINE.S_OPTY_PROD_FNX.ROW_ID and SIEBPLINE.S_OPTY.PR_OPTYPRD_ID = SIEBPLINE.S_OPTY_PROD1_FNX.ROW_ID(+) and SIEBPLINE.S_OPTY.PR_CON_ID = SIEBPLINE.S_CONTACT.ROW_ID(+) and SIEBPLINE.S_OPTY.PR_DEPT_OU_ID = SIEBPLINE.S_ORG_EXT.ROW_ID(+)"
                    #query = "select SIEBPLINE.S_ORG_EXT.ROW_ID as CLIENTE, 'Persona Moral' as REGIMEN, REPLACE(REPLACE(SIEBPLINE.S_ORG_EXT.ALIAS_NAME,'-',''),' ','') as RFC, SIEBPLINE.S_ORG_EXT.NAME as RAZON_SOCIAL, SIEBPLINE.S_ORG_EXT.URL as GIRO, SIEBPLINE.S_ADDR_PER.ADDR as CALLE, SIEBPLINE.S_ADDR_PER.PROVINCE as COLONIA, '' as NUM_INT, '' as NUM_EXT, 'Persona Moral' as REGIMEN, 'Mexicana' as NACIONALIDAD, 'Mexicana' as TELCONTACTO, 'N/A' as NUMERO_INTERIOR, SIEBPLINE.S_ADDR_PER.ZIPCODE as CP, SIEBPLINE.S_ADDR_PER.COUNTY as MUNICIPIO, SIEBPLINE.S_ADDR_PER.CITY as CIUDAD, SIEBPLINE.S_ADDR_PER.STATE as ESTADO, SUBSTR(SIEBPLINE.S_ORG_EXT.MAIN_PH_NUM,4) as TELEFONO, SIEBPLINE.S_CONTACT.FST_NAME || ' ' || SIEBPLINE.S_CONTACT.LAST_NAME as NOMBRE_CONTACTO, SIEBPLINE.S_ADDR_PER.COUNTRY as PAIS from SIEBPLINE.S_ORG_EXT, SIEBPLINE.S_ADDR_PER, SIEBPLINE.S_ORG_EXT_FNX, SIEBPLINE.S_CONTACT where  SIEBPLINE.S_ORG_EXT.PR_ADDR_ID=SIEBPLINE.S_ADDR_PER.ROW_ID(+) and SIEBPLINE.S_ORG_EXT.ROW_ID = SIEBPLINE.S_ORG_EXT_FNX.PAR_ROW_ID and SIEBPLINE.S_ORG_EXT.PR_CON_ID = SIEBPLINE.S_CONTACT.PAR_ROW_ID(+) and  SIEBPLINE.S_ORG_EXT.ROW_ID='{0}'".format(request.POST.get('unblock_number'))
                    #query = "select SIEBPLINE.S_CONTACT.ROW_ID as IDCLIENTE, 'Persona Fisica' as REGIMEN, REPLACE(REPLACE(SIEBPLINE.S_CONTACT.ALIAS_NAME,'-',''),' ','') as RFC, SIEBPLINE.S_CONTACT.LAST_NAME as APELLIDOS, SIEBPLINE.S_CONTACT.FST_NAME as NOMBRE, SIEBPLINE.S_CONTACT_FNX.IDEN2_NUM as CURP, TO_CHAR(SIEBPLINE.S_CONTACT.BIRTH_DT,'YYYY-MM-DD') as FECHA_NACIMIENTO, SIEBPLINE.S_CONTACT.NATIONALITY as NACIONALIDAD, SIEBPLINE.S_CONTACT_X.ATTRIB_34 as GIRO, SIEBPLINE.S_CONTACT.PR_PER_ADDR_ID, SIEBPLINE.S_ADDR_PER.ADDR as CALLE, SIEBPLINE.S_ADDR_PER.PROVINCE as COLONIA, '' as NUM_INT, '' as NUM_EXT, SIEBPLINE.S_ADDR_PER.ZIPCODE as CP, SIEBPLINE.S_ADDR_PER.COUNTY as MUNICIPIO, SIEBPLINE.S_ADDR_PER.CITY as CIUDAD, SIEBPLINE.S_ADDR_PER.STATE as ESTADO, SUBSTR(SIEBPLINE.S_CONTACT.WORK_PH_NUM,4) as TELEFONO, SIEBPLINE.S_CONTACT.FST_NAME || ' ' || SIEBPLINE.S_CONTACT.LAST_NAME as NOMBRE_CONTACTO, SIEBPLINE.S_CONTACT.SEX_MF as SEXO, SIEBPLINE.S_CONTACT.MARITAL_STAT_CD as EDO_CIVIL, SIEBPLINE.S_CONTACT_FNX.BIRTH_PLACE as LUGAR_NACIMIENTO, SIEBPLINE.S_ADDR_PER.COUNTRY as PAIS, '' as FIEL, '' as NIE, SIEBPLINE.S_CONTACT.EMAIL_ADDR as CORREO from SIEBPLINE.S_CONTACT,  SIEBPLINE.S_CONTACT_X,  SIEBPLINE.S_ADDR_PER,  SIEBPLINE.S_CONTACT_FNX where SIEBPLINE.S_CONTACT.ROW_ID = SIEBPLINE.S_CONTACT_X.PAR_ROW_ID and SIEBPLINE.S_CONTACT.ROW_ID = SIEBPLINE.S_CONTACT_FNX.PAR_ROW_ID and SIEBPLINE.S_CONTACT.PR_PER_ADDR_ID = SIEBPLINE.S_ADDR_PER.ROW_ID(+) and SIEBPLINE.S_CONTACT.ROW_ID='{0}'".format(request.POST.get('unblock_number'))
                    #query = "select ID_CREDITO from java_core.creditos where creditos.id_solicitud='{0}'".format(request.POST.get('unblock_number'))
                    query = "select * from amortizacion where ID_CREDITO='{0}'".format(request.POST.get('unblock_number'))
                    cursor = con.cursor()
                    cursor.execute(query)
                    response = cursor.fetchall()
                    cursor.close()
                    return JsonResponse({'message':message,'api':'Success','response':response})
                except Exception as e:
                    message, api = str(e), 'error' 
            return JsonResponse({'message':message,'api':api})
        return super().dispatch(request, *args, **kwargs)
    ###########################################################################################
    def proccess_context(self, context):
        context['object'] = self.model
        return context