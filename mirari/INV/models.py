# -*- coding: utf-8 -*-
from mirari.mirari.models import *
from .vars import *

import zeep
import boto3
import os

########################################################################################
def path_FiscalMX(self, filename):
	upload_to = "O/%s%s/INV/FiscalMX/%s" % (self.organization.id, self.organization.code, filename)
	return upload_to
VARS = {
    'NAME':'Dato Fiscal',
    'PLURAL':'Datos Fiscales',
    'MODEL':'FiscalMX',
    'NEW':'NUEVO',
    'NEW_GENDER': 'un nuevo',
    'THIS': 'este',
    'APP':APP,
    'LIST': [
        {
            'field': 'rfc',
            'title': 'RFC',
            'url': 'url_update',
        },
        {
            'field': 'razon_social',
            'title': 'Razón Social',
            'url': 'url_update',
        },
        {
            'field': 'persona',
            'title': 'Tipo',
            'url': 'url_update',
        },
        {
            'field': 'getStatus',
            'title': 'STATUS',
            'url': 'url_update',
        },
    ],
    'FORM': [
        Div(
            Div(
                HTML('<h5 class="kt-section__title ml-2 mb-4">DATOS FISCALES</h5>'),
                Div('rfc'),
                Div('razon_social'),
                Div('persona'),
                Div('curp'),
                HTML('<h5 class="kt-section__title ml-2 mb-4">DATOS DE CONTACTO</h5>'),
                Div('phone'),
                Div('contactName'),
                Div('contactEmail'),
                css_class="col-md-7"
            ),
            Div(
                HTML('<h5 class="kt-section__title ml-2 mb-4">CERTIFICADOS</h5>'),
                Div('cer'),
                Div('key'),
                Div('password'),
                HTML('<h5 class="kt-section__title ml-2 mb-4">DIRECCIÓN</h5>'),
                Div('street'),
                Div('extNumber'),
                Div('intNumber'),
                Div('region'),
                Div('province'),
                Div('state'),
                Div('zipcode'),
                css_class="col-md-5"
            ),
            css_class="form-group m-form__group row"
        ),
    ],
    'FORM_SIZE': 'col-md-12',
}
class FiscalMX(Model_base):
    PERSONA = (
        ('FISICA','FISICA'),
        ('MORAL','MORAL'),
    )
    STATES = (
        ('Aguascalientes', ('Aguascalientes')),
        ('Baja California', ('Baja California')),
        ('Baja California Sur', ('Baja California Sur')),
        ('Campeche', ('Campeche')),
        ('Chihuahua', ('Chihuahua')),
        ('Chiapas', ('Chiapas')),
        ('Coahuila', ('Coahuila')),
        ('Colima', ('Colima')),
        ('CDMX', ('CDMX')),
        ('Durango', ('Durango')),
        ('Guerrero', ('Guerrero')),
        ('Guanajuato', ('Guanajuato')),
        ('Hidalgo', ('Hidalgo')),
        ('Jalisco', ('Jalisco')),
        ('Estado de México', ('Estado de México')),
        ('Michoacán', ('Michoacán')),
        ('Morelos', ('Morelos')),
        ('Nayarit', ('Nayarit')),
        ('Nuevo León', ('Nuevo León')),
        ('Oaxaca', ('Oaxaca')),
        ('Puebla', ('Puebla')),
        ('Querétaro', ('Querétaro')),
        ('Quintana Roo', ('Quintana Roo')),
        ('Sinaloa', ('Sinaloa')),
        ('San Luis Potosí', ('San Luis Potosí')),
        ('Sonora', ('Sonora')),
        ('Tabasco', ('Tabasco')),
        ('Tamaulipas', ('Tamaulipas')),
        ('Tlaxcala', ('Tlaxcala')),
        ('Veracruz', ('Veracruz')),
        ('Yucatán', ('Yucatán')),
        ('Zacatecas', ('Zacatecas')),
    )
    organization = models.ForeignKey('mirari.Organization', related_name='+', on_delete=models.CASCADE)
    rfc = MXRFCField(verbose_name="RFC")
    razon_social = models.CharField('Razón social', max_length=255, help_text="Razón social de persona Física o Moral")
    persona = models.CharField('Tipo de persona', choices=PERSONA, max_length=100, default='Física')
    curp = MXCURPField('C.U.R.P.', blank=True, null=True)
    contactEmail = models.EmailField('Email contacto', max_length=100, help_text="Correo donde llegarán las notificaciones sobre facturación")
    phone = models.CharField('Teléfono contacto', max_length=100, blank=True, null=True)
    contactName = models.CharField('Nombre contacto', max_length=255, blank=True, null=True)
    street = models.CharField('Calle', max_length=255, blank=True, null=True)
    extNumber = models.CharField('No. EXT', max_length=150, blank=True, null=True)
    intNumber = models.CharField('No. INT', max_length=150, blank=True, null=True)
    region = models.CharField('Colonia', max_length=255, blank=True, null=True)
    province = models.CharField('Municipio o Delegación', max_length=150, blank=True, null=True)
    state = models.CharField('Estado', choices=STATES, max_length=100, blank=True, null=True)
    zipcode = MXZipCodeField('CP.', blank=True, null=True)
    country = models.CharField('País', max_length=100, default='México')
    cer = models.FileField('CERTIFICADO', blank=True, null=True, upload_to=path_FiscalMX)
    key = models.FileField('LLAVE', blank=True, null=True, upload_to=path_FiscalMX)
    password = models.CharField('PASSWORD', blank=True, null=True, max_length=50, help_text="Contraseña de la llave privada")
    noCer= models.CharField('', blank=True, null=True, max_length=50, help_text="Numero de certificado")
    VARS = VARS
    class Meta(Model_base.Meta):
        verbose_name = VARS['NAME']
        verbose_name_plural = VARS['PLURAL']
        permissions = permissions(VARS)

    def __str__(self):
        return '{0}'.format(self.id)
    
    def getStatus(self):
        if self.noCer:
            return mark_safe('<i class="flaticon2-hexagonal text-success"></i>')
        else:
            return mark_safe('<i class="flaticon2-hexagonal text-danger"></i>')
@receiver(post_save, sender=FiscalMX)
def post_saveFiscalMX(sender, **kwargs):
    instance = kwargs.pop('instance', None)
    directory = "O/%s%s/INV/FiscalMX/" % (instance.organization.id, instance.organization.name)
    if settings.DJANGO_SETTINGS_MODULE == 'config.settings.production':
        pass
        s3 = boto3.resource('s3', aws_access_key_id=settings.AWS_ACCESS_KEY_ID, aws_secret_access_key=settings.AWS_SECRET_ACCESS_KEY)
        bucket = s3.Bucket(settings.AWS_STORAGE_BUCKET_NAME)
        bucket.download_file('media/'+instance.cer.name, str(settings.APPS_DIR.path('media'))+'/'+directory+instance.rfc+'.cer')
        bucket.download_file('media/'+instance.key.name, str(settings.APPS_DIR.path('media'))+'/'+directory+instance.rfc+'.key')
        cer = str(settings.APPS_DIR.path('media'))+'/'+directory+instance.rfc+'.cer'
        key = str(settings.APPS_DIR.path('media'))+'/'+directory+instance.rfc+'.key'
    else:
        cer = str(settings.APPS_DIR.path('media'))+'/'+instance.cer.name
        key = str(settings.APPS_DIR.path('media'))+'/'+instance.key.name
    noCer = os.popen('openssl x509 -inform DER -in '+cer.replace(" ","\ ")+' -noout -serial').readlines()[0].replace("serial=","").replace("\n","")
    certificado = ""
    for i in range(len(noCer)):
        if i % 2 != 0:
            certificado = certificado + noCer[i]
    if not certificado == instance.noCer:
        FiscalMX.objects.filter(pk=instance.pk).update(noCer = '')
        client = zeep.Client(wsdl=settings.FINKOK['URL']+'registration.wsdl')
        response = client.service.get( 
            reseller_username = settings.FINKOK['USER'],
            reseller_password = settings.FINKOK['PASSWORD'],
            taxpayer_id = instance.rfc, 
        )
        if not response['users']:
            response = client.service.add( 
                reseller_username = settings.FINKOK['USER'],
                reseller_password = settings.FINKOK['PASSWORD'],
                taxpayer_id = instance.rfc, 
                type_user = 'O',
                cer = open(cer, "rb").read(),
                key = open(key, "rb").read(),
                passphrase = instance.password,
            )
        else:
            response = client.service.edit( 
                reseller_username = settings.FINKOK['USER'],
                reseller_password = settings.FINKOK['PASSWORD'],
                taxpayer_id = instance.rfc, 
                status = 'A',
                cer = open(cer, "rb").read(),
                key = open(key, "rb").read(),
                passphrase = instance.password,
            )
        if response['success'] == True:
            FiscalMX.objects.filter(pk=instance.pk).update(noCer = certificado)

########################################################################################
VARS = {
    'NAME':'Factura',
    'PLURAL':'Facturas',
    'MODEL':'Invoice',
    'NEW':'NUEVO',
    'NEW_GENDER': 'un nuevo',
    'THIS': 'este',
    'APP':APP,
    'LIST': [
        {
            'field': 'id',
            'title': 'ID',
            'url': 'url_update',
            'sorteable': True,
            'serchable': True,
        },
    ],
}
class Invoice(Model_base):
    organization = models.ForeignKey('mirari.Organization', related_name='+', on_delete=models.CASCADE)
    VARS = VARS
    class Meta(Model_base.Meta):
        verbose_name = VARS['NAME']
        verbose_name_plural = VARS['PLURAL']
        permissions = permissions(VARS)
    def __str__(self):
        return '{0}'.format(self.id)