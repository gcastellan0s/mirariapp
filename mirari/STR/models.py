# -*- coding: utf-8 -*-
from rest_framework import serializers
from mirari.mirari.viewbase import Basic_Serializer
from mirari.mirari.models import *
from .vars import *


########################################################################################
VARS = {
    'NAME':'Almacén',
    'PLURAL':'Almacenes',
    'MODEL':'Storehouse',
    'NEW':'NUEVO',
    'NEW_GENDER': 'un nuevo',
    'THIS': 'este',
    'APP':APP,
    'LIST': [
        {
            'field': 'name',
            'title': 'ALMACÉN',
        },
        {
            'field': 'get_street',
            'title': 'CALLE',
        },
    ],
    'FORM_CLASS': 'kt-form kt-form--fit kt-form--label-right form-horizontal',
}
class Storehouse(Model_base):
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
    name = models.CharField('Alias', max_length=250, help_text="Nombre con el que identificas al almacén")
    street = models.CharField('Calle', max_length=255, blank=True, null=True)
    extNumber = models.CharField('No. EXT', max_length=150, blank=True, null=True)
    intNumber = models.CharField('No. INT', max_length=150, blank=True, null=True)
    region = models.CharField('Colonia', max_length=255, blank=True, null=True)
    province = models.CharField('Municipio o Delegación', max_length=150, blank=True, null=True)
    state = models.CharField('Estado', choices=STATES, max_length=100, blank=True, null=True, default="CDMX")
    zipcode = MXZipCodeField('CP', blank=True, null=True)
    country = models.CharField('País', max_length=100, default='México')
    VARS = VARS
    class Meta(Model_base.Meta):
        verbose_name = VARS['NAME']
        verbose_name_plural = VARS['PLURAL']
        permissions = permissions(VARS)
    def __str__(self):
        return self.name
    def get_street(self):
        return self.render_if(self.street)

        
########################################################################################
VARS = {
    'NAME':'Proveedor',
    'PLURAL':'Proveedores',
    'MODEL':'Provider',
    'NEW':'NUEVO',
    'NEW_GENDER': 'un nuevo',
    'THIS': 'este',
    'APP':APP,
    'LIST': [
        {
            'field': 'name',
            'title': 'PROVEEDOR',
        },
        {
            'field': 'get_rfc',
            'title': 'RFC',
        },
        {
            'field': 'get_razonSocial',
            'title': 'RAZON SOCIAL',
        },
        {
            'field': 'get_contactEmail',
            'title': 'EMAIL DE CONTACTO',
        },
        {
            'field': 'get_contactName',
            'title': 'NOMBRE DEL PROVEEDOR',
        },
    ],
    'FORM_CLASS': 'kt-form kt-form--fit kt-form--label-right form-horizontal',
    'FORM': [
        Div(
            Div('name', css_class="col-md-12"),
            css_class="form-group m-form__group row mt-3"
        ),
        Div('rfc', css_class="col-md-12"),
        Div('razonSocial', css_class="col-md-12"),
        Div(
            HTML('<h4 class="kt-section__title ml-2 mb-4">INFORMACIÓN GENERAL</h5>'),
        ),
        Div(
            Div(
                Div('persona', css_class="col-md-12"),
                Div('curp', css_class="col-md-12"),
                Div('contactEmail', css_class="col-md-12"),
                Div('contactName', css_class="col-md-12"),
                css_class="col-md-7"
            ),
            Div(
                Div('typeProvider', css_class="col-md-12"),
                css_class="col-md-5"
            ),
            css_class="form-group m-form__group row"
        ),
    ],
}
class Provider(Model_base):
    PERSONA = (
        ('FISICA','FISICA'),
        ('MORAL','MORAL'),
    )
    TYPEPROVIDER = (
        ('NACIONAL','NACIONAL'),
        ('EXTRANJERO','EXTRANJERO'),
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
    name = models.CharField('Alias', max_length=250, help_text="Nombre con el que identificas al proveedor")
    rfc = MXRFCField(verbose_name="RFC", blank=True, null=True)
    razonSocial = models.CharField('Razón social', max_length=255, help_text="Razón social de persona Física o Moral", blank=True, null=True)
    persona = models.CharField('Tipo de persona', choices=PERSONA, max_length=100, default='Física', blank=True, null=True)
    curp = MXCURPField('C.U.R.P.', blank=True, null=True)
    contactEmail = models.CharField('Email contacto', blank=True, null=True, max_length=100, help_text="Correo donde llegarán las notificaciones de facturación")
    contactName = models.CharField('Nombre contacto', max_length=255, help_text="Quien responde al contacto del negocio?", blank=True, null=True)
    street = models.CharField('Calle', max_length=255, blank=True, null=True)
    extNumber = models.CharField('No. EXT', max_length=150, blank=True, null=True)
    intNumber = models.CharField('No. INT', max_length=150, blank=True, null=True)
    region = models.CharField('Colonia', max_length=255, blank=True, null=True)
    province = models.CharField('Municipio o Delegación', max_length=150, blank=True, null=True)
    state = models.CharField('Estado', choices=STATES, max_length=100, blank=True, null=True)
    typeProvider = models.CharField('Tipo', choices=TYPEPROVIDER, default="NACIONAL", max_length=100, blank=True, null=True)
    zipcode = MXZipCodeField('CP', blank=True, null=True)
    country = models.CharField('País', max_length=100, default='México')
    VARS = VARS
    class Meta(Model_base.Meta):
        verbose_name = VARS['NAME']
        verbose_name_plural = VARS['PLURAL']
        permissions = permissions(VARS)
    def __str__(self):
        return self.name
    def get_rfc(self):
        return self.render_if(self.rfc)
    def get_razonSocial(self):
        return self.render_if(self.razonSocial)
    def get_contactEmail(self):
        return self.render_if(self.contactEmail)
    def get_contactName(self):
        return self.render_if(self.contactName)

########################################################################################
VARS = {
    'NAME':'Cliente',
    'PLURAL':'Clientes',
    'MODEL':'Client',
    'NEW':'NUEVO',
    'NEW_GENDER': 'un nuevo',
    'THIS': 'este',
    'APP':APP,
    'LIST': [
        {
            'field': 'name',
            'title': 'CLIENTE',
        },
        {
            'field': 'get_rfc',
            'title': 'RFC',
        },
        {
            'field': 'get_razonSocial',
            'title': 'RAZON SOCIAL',
        },
        {
            'field': 'get_contactEmail',
            'title': 'EMAIL DE CONTACTO',
        },
        {
            'field': 'get_contactName',
            'title': 'NOMBRE DEL CLIENTE',
        },
    ],
    'FORM_CLASS': 'kt-form kt-form--fit kt-form--label-right form-horizontal',
    'FORM': [
        Div(
            Div('name', css_class="col-md-12"),
            css_class="form-group m-form__group row mt-3"
        ),
        Div('rfc', css_class="col-md-12"),
        Div('razonSocial', css_class="col-md-12"),
        Div(
            HTML('<h4 class="kt-section__title ml-2 mb-4">INFORMACIÓN GENERAL</h5>'),
        ),
        Div(
            Div(
                Div('persona', css_class="col-md-12"),
                Div('curp', css_class="col-md-12"),
                Div('contactEmail', css_class="col-md-12"),
                Div('contactName', css_class="col-md-12"),
                css_class="col-md-7"
            ),
            Div(
                css_class="col-md-5"
            ),
            css_class="form-group m-form__group row"
        ),
    ],
}
class Client(Model_base):
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
    name = models.CharField('Alias', max_length=250, help_text="Nombre con el que identificas al proveedor")
    rfc = MXRFCField(verbose_name="RFC", blank=True, null=True)
    razonSocial = models.CharField('Razón social', max_length=255, help_text="Razón social de persona Física o Moral", blank=True, null=True)
    persona = models.CharField('Tipo de persona', choices=PERSONA, max_length=100, default='Física', blank=True, null=True)
    curp = MXCURPField('C.U.R.P.', blank=True, null=True)
    contactEmail = models.CharField('Email contacto', blank=True, null=True, max_length=100, help_text="Correo donde llegarán las notificaciones de facturación")
    contactName = models.CharField('Nombre contacto', max_length=255, help_text="Quien responde al contacto del negocio?", blank=True, null=True)
    street = models.CharField('Calle', max_length=255, blank=True, null=True)
    extNumber = models.CharField('No. EXT', max_length=150, blank=True, null=True)
    intNumber = models.CharField('No. INT', max_length=150, blank=True, null=True)
    region = models.CharField('Colonia', max_length=255, blank=True, null=True)
    province = models.CharField('Municipio o Delegación', max_length=150, blank=True, null=True)
    state = models.CharField('Estado', choices=STATES, max_length=100, blank=True, null=True)
    zipcode = MXZipCodeField('CP', blank=True, null=True)
    country = models.CharField('País', max_length=100, default='México')
    VARS = VARS
    class Meta(Model_base.Meta):
        verbose_name = VARS['NAME']
        verbose_name_plural = VARS['PLURAL']
        permissions = permissions(VARS)
    def __str__(self):
        return self.name
    def get_rfc(self):
        return self.render_if(self.rfc)
    def get_razonSocial(self):
        return self.render_if(self.razonSocial)
    def get_contactEmail(self):
        return self.render_if(self.contactEmail)
    def get_contactName(self):
        return self.render_if(self.contactName)


########################################################################################
VARS = {
    'NAME':'Categoria de producto',
    'PLURAL':'Categoria de productos',
    'MODEL':'CategoryProduct',
    'NEW':'NUEVA',
    'NEW_GENDER': 'una nueva',
    'THIS': 'esta',
    'APP':APP,
    'LIST': [
        {
            'field': 'name',
            'title': 'NOMBRE',
        },
    ],
    'FORM': ('name',),
}
class CategoryProduct(Model_base):
    organization = models.ForeignKey('mirari.Organization', blank=True, null=True, on_delete=models.CASCADE, related_name='+',)
    name = models.CharField('Nombre de la categoria', max_length=250)
    VARS = VARS
    class Meta(Model_base.Meta):
        verbose_name = VARS['NAME']
        verbose_name_plural = VARS['PLURAL']
        permissions = permissions(VARS)
    def __str__(self):
        return self.name


########################################################################################
VARS = {
    'NAME':'Producto',
    'PLURAL':'Productos',
    'MODEL':'Product',
    'NEW':'NUEVO',
    'NEW_GENDER': 'un nuevo',
    'THIS': 'este',
    'APP':APP,
    'LIST': [
        {
            'field': 'name',
            'title': 'NOMBRE',
            'serchable': True,
        },
        {
            'field': 'model',
            'title': 'MODELO',
            'serchable': True,
        },
        {
            'field': 'get_codebar',
            'title': 'CODIGO DE BARRAS',
        },
        {
            'field': 'get_uid',
            'title': 'UID',
        },
        {
            'field': 'quantity',
            'title': 'Cantidad',
        },
        {
            'field': 'get_category',
            'title': 'CATEGORIA',
        },
    ],
    'PAGECreate': 'Product__CreateView.html',
    'FORM_CLASS': 'kt-form kt-form--fit kt-form--label-right form-horizontal',
    'FORM': [
        Div(
            Div('name', css_class="col-md-12"),
            Div('codebar', css_class="col-md-10"),
            Div(
                HTML("""<button type="button" onclick="var message={action:'GetQR', target:'codebar'}; webkit.messageHandlers.cordova_iab.postMessage(JSON.stringify(message));" class="btn btn-brand"><i class="fas fa-barcode"></i> CAPTURAR</button>"""),
                css_class="col-md-2"
            ),
            Div('uid', css_class="col-md-10"),
            Div(
                HTML("""<button type="button" onclick="var message={action:'GetQR', target:'uid'}; webkit.messageHandlers.cordova_iab.postMessage(JSON.stringify(message));" class="btn btn-brand"><i class="fas fa-barcode"></i> CAPTURAR</button>"""),
                css_class="col-md-2"
            ),
            css_class="form-group m-form__group row mt-3"
        ),
        Div('canBySell', css_class="col-md-12"),
        Div('canByBuy', css_class="col-md-12"),
        TabHolder(
            Tab('GENERAL',
                HTML('<h4 class="kt-section__title ml-2 mb-4">INFORMACIÓN GENERAL</h4>'),
                Div(
                    Div(
                        Div('typeProduct', css_class="col-md-12"),
                        Div('category', css_class="col-md-12"),
                        Div('model', css_class="col-md-12"),
                        css_class="col-md-7"
                    ),
                    Div(
                        Div('sellPrice', css_class="col-md-12"),
                        Div('costPrice', css_class="col-md-12"),
                        css_class="col-md-5"
                    ),
                    css_class="form-group m-form__group row"
                ),
                
                Div('description', css_class="col-md-12"),
                Div('photo', css_class="col-md-12"),
                Div('notes', css_class="col-md-12"),
            ),
            Tab('INVENTARIO',
                HTML('<h4 class="kt-section__title ml-2 mb-4">INVENTARIO</h5>'),
                Div(
                    Div(
                        Div('location', css_class="col-md-12"),
                        Div('weight', css_class="col-md-12"),
                        Div('volume', css_class="col-md-12"),
                        css_class="col-md-5"
                    ),
                    Div(
                        Div('quantity', css_class="col-md-12"),
                        Div('deliveryTerm', css_class="col-md-12"),
                        Div('minimumQuantity', css_class="col-md-12"),
                        Div('maximumQuantity', css_class="col-md-12"),
                        css_class="col-md-7"
                    ),
                    css_class="form-group m-form__group row"
                ),
            ),
            Tab('EXTRA',
                HTML('<h4 class="kt-section__title ml-2 mb-4">INFORMACIÓN EXTRA</h5>'),
                Div('users', css_class="col-md-12"),
                Div('providers', css_class="col-md-12"),
                Div('deliveryDescription', css_class="col-md-12"),
                Div('receptionsDescription', css_class="col-md-12"),
            ),
        ),
    ],
    'SELECTQ': {
        'category': {
            'model': ['STR', 'CategoryProduct'],
            'plugin': 'select2',
            'query': [
                (
                    ('organization__pk', 'self.request.session.get("organization")'),
                ),
            ],
            'sercheable': ['name__icontains',],
            'limits': 50,
            'placeholder': 'Elige una categoría',
            'minimumInputLength': '0',
        },
        'users': {
            'model': ['mirari', 'User'],
            'plugin': 'selectmultiple',
            'query': [
                (
                    ('groups__in', 'Group.objects.filter(id=33)'),
                ),
            ],
            #'sercheable': ('visible_username__icontains'),
        },
        'providers': {
            'model': ['STR', 'Provider'],
            'plugin': 'selectmultiple',
            #'query': [
                #(
                    #('organization__pk', 'self.request.session.get("organization")'),
                #),
            #],
            #'sercheable': ('name__icontains'),
        },
    },
}
def pathProductImage(self, filename):
    upload_to = "O/%s%s/STR/Prod/%s" % (self.organization.id, self.organization.code, filename)
    return upload_to
class Product(Model_base):
    PRODUCTTYPE = (
        ('Consumible','Consumible'),
        ('Servicio','Servicio'),
        ('Almacenaje','Almacenaje'),
    )
    organization = models.ForeignKey('mirari.Organization', blank=True, null=True, on_delete=models.CASCADE, related_name='+',)
    name = models.CharField('Nombre del producto', max_length=250)
    canBySell = models.BooleanField('Puede ser vendido?', default=True)
    canByBuy = models.BooleanField('Puede ser comprado?', default=True)
    typeProduct = models.CharField('Tipo de producto', choices=PRODUCTTYPE, max_length=250, default="Almacenaje")
    category = models.ForeignKey('STR.CategoryProduct', on_delete=models.SET_NULL, verbose_name="Categoría", related_name  ='+', blank=True, null=True)
    uid = models.CharField('PKU', max_length=30, blank=True, null=True)
    codebar = models.CharField('Código de barras o QR', max_length=30, blank=True, null=True)
    model = models.CharField('Modelo', max_length=50, blank=True, null=True)
    sellPrice = models.FloatField('Venta $', blank=True, null=True)
    costPrice = models.FloatField('Costo $', blank=True, null=True)
    notes = models.TextField(blank=True, verbose_name="NOTAS INTERNAS")
    description = models.TextField(blank=True, verbose_name="DESCRIPCIÓN")
    weight = models.FloatField('Peso (kg)', blank=True, null=True)
    volume = models.FloatField('Volumen (m2)', blank=True, null=True)
    deliveryTerm = models.IntegerField('Plazo entrega (días)', blank=True, null=True)
    users = models.ManyToManyField('mirari.User', verbose_name="Responsables", blank=True)
    providers = models.ManyToManyField('STR.Provider', verbose_name="Proveedores", blank=True)
    deliveryDescription = models.TextField(blank=True, verbose_name="Descripción para entregas")
    receptionsDescription = models.TextField(blank=True, verbose_name="Descripción para recepciones")
    quantity = models.IntegerField('CANTIDAD ACTUAL', default=0)
    minimumQuantity = models.IntegerField('Cantidad mínima', blank=True, null=True)
    maximumQuantity = models.IntegerField('Cantidad máxima', blank=True, null=True)
    location = models.CharField('Ubicación', max_length=250, blank=True, null=True)
    photo = ProcessedImageField(upload_to=pathProductImage, format='JPEG', options={'quality': 60}, blank=True, null=True, verbose_name="Imagen del producto")
    id_bckp = models.IntegerField(blank=True, null=True)
    VARS = VARS
    class Meta(Model_base.Meta):
        verbose_name = VARS['NAME']
        verbose_name_plural = VARS['PLURAL']
        permissions = permissions(VARS)
    def __str__(self):
        if not self.model:
            return 'Modelo no definido'
        return self.model
    def url_list(self):
        return reverse('STR:Product__ListView')
    def get_category(self):
        return self.render_if(self.category.name)
    def get_uid(self):
        return self.render_if(self.uid)
    def get_codebar(self):
        return self.render_if(self.codebar)
    def get_photo(self):
        return self.render_if(self.photo)

class ProductSerializer(Basic_Serializer):
    class Meta(Basic_Serializer.Meta):
        model = Product

########################################################################################
VARS = {
    'NAME':'Orden de Inventario',
    'PLURAL':'Ordenes de Inventario',
    'MODEL':'InventoryOrder',
    'NEW':'NUEVA',
    'NEW_GENDER': 'una nueva',
    'THIS': 'esta',
    'APP':APP,
    'LIST': [
        {
            'field': 'id',
            'title': 'FOLIO',
            'url': 'url_update',
        },
        {
            'field': 'status',
            'title': 'STATUS',
            'url': 'url_update',
        },
        {
            'field': 'get_initialDateTime',
            'title': 'FECHA',
            'url': 'url_update',
        },
        {
            'field': 'get_provider',
            'title': 'PERSONA O EMPRESA',
            'url': 'url_update',
        },
    ],
    'FORM': ('status','serial','provider','client','producttype', 'outType', 'fordwarder', 'package', 'orderNumber', 'guideNumber', 'paymentCondition','responsibleName','responsible','product', 'notes'),
    'SELECTQ': {
        'provider': {
            'model': ['STR', 'Provider'],
            'plugin': 'select2',
            'query': [
                (
                    ('organization__pk', 'self.request.session.get("organization")'),
                ),
            ],
            'sercheable': ['name__icontains'],
            'limits': 50,
            'placeholder': 'Elige un proveedor',
            'minimumInputLength': '0',
        },
        'responsible': {
            'model': ['mirari', 'User'],
            'plugin': 'select2',
            'sercheable': ['visible_username__icontains'],
            'limits': 50,
            'placeholder': 'Elige un responsable',
            'query': [
                (
                    ('organization__pk', 'self.request.session.get("organization")'),
                    ('groups__in', 'Group.objects.filter(id=33)'),
                ),
            ],
            'minimumInputLength': '0',
        },
        'product': {
            'model': ['STR', 'Product'],
            'plugin': 'select2',
            'sercheable': ['codebar__icontains','name__icontains','model__icontains'],
            'limits': 50,
            'placeholder': 'Elige un producto', 
            'query': [
                (
                    ('organization__pk', 'self.request.session.get("organization")'),
                ),
            ],
            'minimumInputLength': '0',
        },
    },
}
class InventoryOrder(Model_base):
    OPERATIONTYPE = (
        ('in','in'),
        ('out','out'),
    )
    STATUS = (
        ('BORRADOR','BORRADOR'),
        ('EN TRANSITO','EN TRANSITO'),
        ('TERMINADA','TERMINADA'),
    )
    PAYMENTCONDITION = (
        ('30 dias','30 dias'),
        ('45 dias','45 dias'),
        ('60 dias','60 dias'),
        ('90 dias','90 dias'),
    )
    PRODUCTTYPE = (
        ('EQUIPOS-ACCESORIOS','EQUIPOS-ACCESORIOS'),
        ('REFACCIONES','REFACCIONES'),
        ('REFACCIONES BICI','REFACCIONES BICI'),
        ('REFACCIONES TRICI','REFACCIONES TRICI'),
    )
    OUTTYPE = (
        ('VENTA','VENTA'),
        ('ARRENDAMIENTO','ARRENDAMIENTO'),
        ('EXHIBICION','EXHIBICION'),
    )
    FORDWARDER = (
        ('BOEKI','BOEKI'),
        ('CENTRAL CARGO','CENTRAL CARGO'),
        ('GLOBEX','GLOBEX'),
        ('TICAMEX','TICAMEX'),
        ('LUIS GONZALEZ','LUIS GONZALEZ'),
        ('UPS','UPS'),
    )
    PACKAGE = (
        ('ALMEX','ALMEX'),
        ('FEDEX','FEDEX'),
        ('UPS','UPS'),
        ('PAQUETE EXPRESS','PAQUETE EXPRESS'),
        ('DHL','DHL'),
        ('ESTAFETA','ESTAFETA'),
        ('MAS A PRISA','MAS A PRISA'),
        ('3 GUERRAS','3 GUERRAS'),
        ('RED PACK','RED PACK'),
    )
    organization = models.ForeignKey('mirari.Organization', blank=True, null=True, on_delete=models.CASCADE, related_name='+',)
    operationType = models.CharField('Tipo de operación', choices=OPERATIONTYPE, max_length=250)
    status = models.CharField('Estatus', choices=STATUS, max_length=250, default="BORRADOR")
    provider = models.ForeignKey('STR.Provider', null=True, on_delete=models.SET_NULL, related_name='+', verbose_name="Proveedor")
    client = models.ForeignKey('STR.Client', null=True, on_delete=models.SET_NULL, related_name='+', verbose_name="Cliente")
    responsibleName = models.CharField('Nombre de quien solicita', max_length=250, blank=True, null=True)
    initialDateTime = models.DateTimeField(auto_now_add=True)
    finalDateTime = models.DateTimeField(blank=True, null=True)
    fordwarder = models.CharField('Promotor', choices=FORDWARDER, max_length=250, blank=True, null=True)
    serial = models.CharField('Serie', max_length=250, blank=True, null=True)
    package = models.CharField('Paqueteria', choices=PACKAGE, max_length=250, blank=True, null=True)
    guideNumber = models.CharField('Numero de Guía', max_length=250, blank=True, null=True)
    orderNumber = models.CharField('Numero de Pedido', max_length=250, blank=True, null=True)
    producttype = models.CharField('Tipo de producto', choices=PRODUCTTYPE, max_length=250, blank=True, null=True)
    outType = models.CharField('Tipo de salida', choices=OUTTYPE, max_length=250, blank=True, null=True)
    paymentCondition = models.CharField('Condiciones de pago', choices=PAYMENTCONDITION, max_length=250, default="30 dias", blank=True, null=True)
    document = models.CharField('Documento de referencia', max_length=250, blank=True, null=True)
    priority = models.IntegerField('Prioridad', default=0)
    responsible = models.ForeignKey('mirari.User', blank=True, null=True, on_delete=models.SET_NULL, related_name='+', verbose_name="Responsable")
    notes = models.TextField('Notas', max_length=250, blank=True, null=True)
    product = models.ForeignKey('STR.Product', on_delete=models.SET_NULL, related_name='+', blank=True, null=True)
    VARS = VARS
    class Meta(Model_base.Meta):
        verbose_name = VARS['NAME']
        verbose_name_plural = VARS['PLURAL']
        permissions = permissions(VARS)
    def __str__(self):
        return 'InventoryOrder'
    def url_update(self):
        if not 'update' in self.exclude_permissions():
            return reverse('STR:InventoryOrder__UpdateView', kwargs={'app': self.VARS['APP'], 'model': self.VARS['MODEL'], 'pk': self.pk}) + '?type=' + self.operationType
        else:
            return None
    def url_update(self):
        if not 'update' in self.exclude_permissions():
            return reverse('STR:InventoryOrder__UpdateView', kwargs={'app': self.VARS['APP'], 'model': self.VARS['MODEL'], 'pk': self.pk}) + '?type=' + self.operationType
        else:
            return None
    def url_print(self):
        if not 'update' in self.exclude_permissions():
            return reverse('STR:printInventoryOrder__UpdateView', kwargs={'app': self.VARS['APP'], 'model': self.VARS['MODEL'], 'pk': self.pk}) + '?type=' + self.operationType
        else:
            return None
    def get_provider(self):
        if self.operationType == 'in':
            if self.provider:
                return self.provider.name
            else:
                return '-'
        if self.operationType == 'out':
            if self.client:    
                return self.client.name
            else:
                return '-'
    def get_initialDateTime(self):
        return self.initialDateTime.strftime('%d-%m-%Y %H:%M')
    def QUERY(self, view):
        return InventoryOrder.objects.filter(organization__pk=view.request.session.get('organization'), active=True, operationType=view.request.GET.get('type', ''))

########################################################################################
VARS = {
    'NAME':'Producto de Orden de Inventario',
    'PLURAL':'Productos de Orden de Inventario',
    'MODEL':'InventoryOrderProoduct',
    'NEW':'NUEVA',
    'NEW_GENDER': 'un nuevo',
    'THIS': 'este',
    'APP':APP,
    'EXCLUDE_PERMISSIONS':['all'],
}
class InventoryOrderProoduct(Model_base):
    product = models.ForeignKey('STR.Product', on_delete=models.SET_NULL, related_name='+', blank=True, null=True)
    quantity = models.IntegerField()
    cost = models.FloatField(blank=True, null=True)
    specialCost = models.FloatField(blank=True, null=True)
    inventoryorder = models.ForeignKey('STR.InventoryOrder', on_delete=models.CASCADE, related_name='+')
    VARS = VARS
    class Meta(Model_base.Meta):
        verbose_name = VARS['NAME']
        verbose_name_plural = VARS['PLURAL']
        permissions = permissions(VARS)
    def __str__(self):
        return 'InventoryOrder'

class InventoryOrderProoductSerializer(Basic_Serializer):
    product = serializers.SerializerMethodField()
    class Meta(Basic_Serializer.Meta):
        model = InventoryOrderProoduct
    def get_product(self, obj):
        return ProductSerializer(obj.product).data

#
#class ProductHistory(Model_base):
    #HISTORYTYPE = (
        #('ENTRADA','ENTRADA'),
        #('SALIDA','SALIDA'),
        #('ACTUALIZACION','ACTUALIZACION'),
    #)
    #user = models.ForeignKey('mirari.User', blank=True, null=True, on_delete=models.SET_NULL)
    #historyType = models.CharField('Tipo de producto', choices=HISTORYTYPE, max_length=250, default="productQuantity")
    #datetime = models.DateTimeField(auto_now_add=True)
    #product = models.ForeignKey('STR.Product', blank=True, null=True, on_delete=models.SET_NULL)
    #id_bckp = models.IntegerField(blank=True, null=True)
    #class Meta(Model_base.Meta):
        #verbose_name = VARS['NAME']
        #verbose_name_plural = VARS['PLURAL']
        #permissions = permissions(VARS)
    #def __str__(self):
        #return self.name
    #def QUERY(self, view):
        #return ProductHistory.filter(product__organization__pk=view.request.session.get('organization'))