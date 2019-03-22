# -*- coding: utf-8 -*-
from mirari.mirari.models import *
from .vars import *



VARS = {
    'NAME':'Desbloqueo Siebel',
    'PLURAL':'Desbloqueo Siebel',
    'MODEL':'SiebelUnblock',
    'NEW':'NUEVO',
    'NEW_GENDER': 'un nuevo',
    'THIS': 'este',
    'APP':APP,
    'EXCLUDE_PERMISSIONS':['create','update','delete',],
}
class SiebelUnblock(Model_base):
    VARS = VARS
    class Meta(Model_base.Meta):
        verbose_name = VARS['NAME']
        verbose_name_plural = VARS['PLURAL']
        permissions = permissions(VARS)
    def __str__(self):
        return '{0}'.format(self.VARS['NAME'])



VARS = {
    'NAME':'Cartera',
    'PLURAL':'Carteras',
    'MODEL':'WalletCredit',
    'NEW':'NUEVA',
    'NEW_GENDER': 'una nueva',
    'THIS': 'esta',
    'APP':APP,
    'LIST': [
            {
                'field': 'obligacion',
                'title': 'Obligación',
                'width': 100,
                'url': 'property_url_update',
            },
            {
                'field': 'nombre',
                'title': 'Nombre',
                'width': 300,
                'url': 'property_url_update',
            },
            {
                'field': 'walletcredit_tipo',
                'title': 'TIPO',
                'url': 'property_url_update',
            },
            {
                'field': 'rfc',
                'title': 'RFC',
            },
            {
                'field': 'property_get_plazo',
                'title': 'Plazo',
            },
            {
                'field': 'property_get_monto',
                'title': 'Monto',
            },
        ],
    'SERIALIZER': ('get_monto','get_plazo'),
    'SEARCH': ['nombre','rfc','obligacion'],
    'SORTEABLE': ['nombre','obligacion','fecha_vencimiento','fecha_otorgado'],
    'HIDE_CHECKBOX_LIST': True,
    'HIDE_BUTTONS_LIST': True,
    'FORM': [
        Div(
            Div('numero', css_class="col-md-3"),
            Div('nombre', css_class="col-md-9"),
            
            css_class="form-group m-form__group row"
        ),
        Div(
            Div('obligacion', css_class="col-md-4"),
            Div('clasificacion', css_class="col-md-4"),
            Div('clasificacion_contable', css_class="col-md-4"),
            css_class="form-group m-form__group row"
        ),
        Div(
            Div('rfc', css_class="col-md-4"),
            Div('producto', css_class="col-md-4"),
            Div('forma_pago', css_class="col-md-4"),
            css_class="form-group m-form__group row"
        ),
        Div(
            Div('fecha_otorgado', css_class="col-md-6"),
            Div('fecha_vencimiento', css_class="col-md-6"),
            css_class="form-group m-form__group row"
        ),
        
        Div(
            Div('tipo_tasa', css_class="col-md-4"),
            Div('tasa', css_class="col-md-4"),
            css_class="form-group m-form__group row"
        ),
        Div(
            Div('plazo', css_class="col-md-4"),
            Div('monto', css_class="col-md-4"),
            Div('fondeador', css_class="col-md-4"),
            css_class="form-group m-form__group row"
        ),
    ],
}
class WalletCredit(Model_base):
    organization = models.ForeignKey('mirari.Organization', blank=True, null=True, on_delete=models.CASCADE, related_name='+',)
    walletcredit_tipo = models.CharField('Obligación', max_length=250, choices=WALLETCREDIT_TIPO, default="CREDITO")
    numero = models.IntegerField('ID CLiente', blank=True, null=True)
    obligacion = models.CharField('Obligación', max_length=250, blank=True, null=True)
    clasificacion = models.CharField('Clasificación', max_length=250, blank=True, null=True)
    clasificacion_contable = models.CharField('Clasificación contable', max_length=250, choices=CLASIFICACION_CONTABLE, blank=True, null=True)
    nombre = models.CharField('Nombre', max_length=250, blank=True, null=True)
    tipo = models.CharField('Tipo de persona', max_length=250, blank=True, null=True)
    rfc = models.CharField('RFC', max_length=250, blank=True, null=True)
    producto = models.CharField('Producto', max_length=250, blank=True, null=True)
    forma_pago = models.CharField('Forma de pago', max_length=250, choices=FORMA_PAGO, blank=True, null=True)
    tipo_tasa = models.CharField('Tipo de tasa', max_length=250, choices=TIPO_TASA, blank=True, null=True)
    tasa = models.FloatField('Tasa', blank=True, null=True)
    fecha_otorgado = models.DateField('Fecha otorgado', blank=True, null=True)
    fecha_vencimiento = models.DateField('Fecha vencimiento', blank=True, null=True)
    plazo = models.IntegerField('Plazo', blank=True, null=True)
    monto = models.FloatField('Monto', blank=True, null=True)
    fondeador = models.CharField('Fondeador', max_length=250, blank=True, null=True)
    VARS = VARS
    class Meta(Model_base.Meta):
        verbose_name = VARS['NAME']
        verbose_name_plural = VARS['PLURAL']
        permissions = permissions(VARS)
    def __str__(self):
        return '{0}'.format(self.VARS['NAME'])
    def url_add(self):
        return reverse('CRYE:WalletCredit__TemplateView', kwargs={'app': self.VARS['APP'], 'model': self.VARS['MODEL']})
    def url_update(self):
        return reverse('CRYE:TablaAmortizacion__TemplateView', kwargs={'app': self.VARS['APP'], 'model': self.VARS['MODEL'], 'pk': self.pk})
    def get_plazo(self):
        if self.plazo:
            return '{0} meses'.format(self.plazo)
        return '-'
    def get_monto(self):
        if self.monto:
            return '$ {0}'.format(self.monto)
        return '-'
    def payments(self):
        return len(PagoAmortizacion.objects.filter(tablaaAmortizacion__in = TablaAmortizacion.objects.filter(walletcredit = self)))
    def totalPayment(self):
        total = 0
        for pagoamortizacion in PagoAmortizacion.objects.filter(tablaaAmortizacion__in = TablaAmortizacion.objects.filter(walletcredit = self)):
            total += pagoamortizacion.total()
        return total
    def lastPayment(self):
        try:
            return PagoAmortizacion.objects.filter(tablaaAmortizacion__in = TablaAmortizacion.objects.filter(walletcredit = self)).first().fecha
        except:
            pass
    def lastUser(self):
        try:
            return PagoAmortizacion.objects.filter(tablaaAmortizacion__in = TablaAmortizacion.objects.filter(walletcredit = self)).first().user
        except:
            pass
    
    
    

VARS = {
    'NAME':'Tabla de amortización',
    'PLURAL':'Tablas de amortización',
    'MODEL':'TablaAmortizacion',
    'NEW':'NUEVO',
    'NEW_GENDER': 'un nuevo',
    'THIS': 'este',
    'APP':APP,
    'EXCLUDE_PERMISSIONS':['all'],
}
class TablaAmortizacion(Model_base):
    Estatus = (
        ('Facturado','Facturado'),
        ('Pendiente','Pendiente'),
    )
    walletcredit = models.ForeignKey('WalletCredit', on_delete=models.CASCADE, related_name='+',)
    numeroPago = models.IntegerField('ID CLiente', blank=True, null=True)
    date = models.DateField('Fecha otorgado', blank=True, null=True)
    estatus = models.CharField('Fondeador', max_length=250, choices=Estatus)
    balanceInsoluto = models.FloatField('Balance Insoluto')
    capital = models.FloatField('Capital')
    intereses = models.FloatField('Intereses')
    renta = models.FloatField('Renta')
    pagado  = models.FloatField('Pagado')
    VARS = VARS
    class Meta(Model_base.Meta):
        verbose_name = VARS['NAME']
        verbose_name_plural = VARS['PLURAL']
        permissions = permissions(VARS)
    def __str__(self):
        return '{0}'.format(self.VARS['NAME'])



VARS = {
    'NAME':'Pago de amortizacion',
    'PLURAL':'Pago de amortizacion',
    'MODEL':'PagoAmortizacion',
    'NEW':'NUEVO',
    'NEW_GENDER': 'un nuevo',
    'THIS': 'este',
    'APP':APP,
    'EXCLUDE_PERMISSIONS':['all'],
}
class PagoAmortizacion(Model_base):
    fecha = models.DateField(auto_now_add=True)
    user = models.ForeignKey('mirari.User', on_delete=models.CASCADE, related_name='+',)
    tablaaAmortizacion = models.ForeignKey('TablaAmortizacion', on_delete=models.CASCADE, related_name='+',)
    capital = models.FloatField('Intereses')
    interesVigente = models.FloatField('Intereses')
    intereVigenteNoPagado = models.FloatField('Intereses')
    interesMoratorio = models.FloatField('Intereses')
    gastosCobranza = models.FloatField('Intereses')
    iva = models.FloatField('Intereses')
    VARS = VARS
    class Meta(Model_base.Meta):
        verbose_name = VARS['NAME']
        verbose_name_plural = VARS['PLURAL']
        permissions = permissions(VARS)
    def __str__(self):
        return '{0}'.format(self.pk)
    def total(self):
        total = 0
        total += self.capital
        total += self.interesVigente
        total += self.intereVigenteNoPagado
        total += self.interesMoratorio
        total += self.gastosCobranza
        total += self.iva
        return total



VARS = {
    'NAME':'Tasa de interés',
    'PLURAL':'Tasas de interés',
    'MODEL':'TasasInteres',
    'NEW':'NUEVO',
    'NEW_GENDER': 'una nueva',
    'THIS': 'esta',
    'APP':APP,
}
class TasasInteres(Model_base):
    VARS = VARS
    class Meta(Model_base.Meta):
        verbose_name = VARS['NAME']
        verbose_name_plural = VARS['PLURAL']
        permissions = permissions(VARS)
    def __str__(self):
        return '{0}'.format(self.VARS['NAME'])




        