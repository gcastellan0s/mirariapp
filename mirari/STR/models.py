# -*- coding: utf-8 -*-
from rest_framework import serializers
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
        },
        #{
            #'field': 'id',
            #'title': 'ID',
        #},
        #{
            #'field': 'get_category',
            #'title': 'CATEGORIA',
        #},
        {
            'field': 'get_uid',
            'title': 'UID',
        },
        {
            'field': 'get_codebar',
            'title': 'CODIGO DE BARRAS',
        },
        {
            'field': 'get_photo',
            'title': 'FOTO',
        },
    ],
    'FORM_CLASS': 'kt-form kt-form--fit kt-form--label-right form-horizontal',
    'FORM': [
        Div(
            Div('name', css_class="col-md-12"),
            Div('codebar', css_class="col-md-10"),
            Div(
                HTML('<a href="#" class="btn btn-brand"><i class="fas fa-barcode"></i> CAPTURAR</a>'),
                css_class="col-md-2"
            ),
            css_class="form-group m-form__group row mt-3"
        ),
        Div('canBySell', css_class="col-md-12"),
        Div('canByBuy', css_class="col-md-12"),
        TabHolder(
            Tab('First Tab',
                HTML('<h4 class="kt-section__title ml-2 mb-4">INFORMACIÓN GENERAL</h4>'),
            ),
            Tab('Second Tab',
                HTML('<h4 class="kt-section__title ml-2 mb-4">INFORMACIÓN GENERAL</h4>'),
            )
        )
        Div(
            HTML('<h4 class="kt-section__title ml-2 mb-4">INFORMACIÓN GENERAL</h4>'),
        ),
        Div(
            Div(
                Div('typeProduct', css_class="col-md-12"),
                Div('category', css_class="col-md-12"),
                Div('uid', css_class="col-md-12"),
                css_class="col-md-7"
            ),
            Div(
                Div('sellPrice', css_class="col-md-12"),
                Div('costPrice', css_class="col-md-12"),
                css_class="col-md-5"
            ),
            css_class="form-group m-form__group row"
        ),
        Div('photo', css_class="col-md-12"),
        Div('notes', css_class="col-md-12"),
        Div(
            HTML('<h4 class="kt-section__title ml-2 mb-4">INVENTARIO</h5>'),
        ),
        Div(
            Div(
                Div('weight', css_class="col-md-12"),
                Div('volume', css_class="col-md-12"),
                css_class="col-md-5"
            ),
            Div(
                Div('deliveryTerm', css_class="col-md-12"),
                Div('minimumQuantity', css_class="col-md-12"),
                Div('maximumQuantity', css_class="col-md-12"),
                css_class="col-md-7"
            ),
            css_class="form-group m-form__group row"
        ),
        Div(
            HTML('<h4 class="kt-section__title ml-2 mb-4">INFORMACIÓN EXTRA</h5>'),
        ),
        Div('users', css_class="col-md-12"),
        Div('providers', css_class="col-md-12"),
        Div('deliveryDescription', css_class="col-md-12"),
        Div('receptionsDescription', css_class="col-md-12"),
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
            'sercheable': ('name__icontains'),
            'limits': 50,
            'placeholder': 'Elige una categoría',
            'minimumInputLength': '0',
        },
        'users': {
            'model': ['mirari', 'User'],
            'plugin': 'select2',
            'query': [
                (
                    ('organization__pk', 'self.request.session.get("organization")'),
                ),
            ],
            'sercheable': ('visible_username__icontains'),
        },
        'providers': {
            'model': ['STR', 'Provider'],
            'plugin': 'select2',
            'query': [
                (
                    ('organization__pk', 'self.request.session.get("organization")'),
                ),
            ],
            'sercheable': ('name__icontains'),
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
    category = models.ForeignKey('STR.CategoryProduct', blank=True, null=True, on_delete=models.SET_NULL, verbose_name="Categoría", related_name  ='+',)
    uid = models.CharField('Referencia interna (PKU)', max_length=30, blank=True, null=True)
    codebar = models.CharField('Código de barras', max_length=30, unique=True, blank=True, null=True)
    sellPrice = models.FloatField('Venta $', blank=True, null=True)
    costPrice = models.FloatField('Costo $', blank=True, null=True)
    notes = models.TextField(blank=True, verbose_name="NOTAS INTERNAS")
    weight = models.FloatField('Peso', blank=True, null=True)
    volume = models.FloatField('Volumen', blank=True, null=True)
    deliveryTerm = models.IntegerField('Plazo de entrega', blank=True, null=True)
    users = models.ManyToManyField('mirari.User', verbose_name="Responsables", blank=True, null=True)
    providers = models.ManyToManyField('STR.Provider', verbose_name="Proveedores", blank=True, null=True)
    deliveryDescription = models.TextField(blank=True, verbose_name="Descripción para entregas")
    receptionsDescription = models.TextField(blank=True, verbose_name="Descripción para recepciones")
    minimumQuantity = models.IntegerField('Cantidad mínima', blank=True, null=True)
    maximumQuantity = models.IntegerField('Cantidad máxima', blank=True, null=True)
    photo = ProcessedImageField(upload_to=pathProductImage, format='JPEG', options={'quality': 60}, blank=True, null=True, verbose_name="Imagen del producto")
    id_bckp = models.IntegerField(blank=True, null=True)
    VARS = VARS
    class Meta(Model_base.Meta):
        verbose_name = VARS['NAME']
        verbose_name_plural = VARS['PLURAL']
        permissions = permissions(VARS)
    def __str__(self):
        return self.name
    def get_category(self):
        return self.render_if(self.category)
    def get_uid(self):
        return self.render_if(self.uid)
    def get_codebar(self):
        return self.render_if(self.codebar)
    def get_photo(self):
        return self.render_if(self.photo)


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
            'field': 'status',
            'title': 'STATUS',
        },
    ],
    'FORM': ('provider','document','priority','responsible','notes','product'),
    'SELECTQ': {
        'provider': {
            'model': ['STR', 'Provider'],
            'plugin': 'select2',
            'query': [
                (
                    ('organization__pk', 'self.request.session.get("organization")'),
                ),
            ],
            'sercheable': ('name__icontains'),
            'limits': 50,
            'placeholder': 'Elige un proveedor',
            'minimumInputLength': '0',
        },
        'responsible': {
            'model': ['mirari', 'User'],
            'plugin': 'select2',
            'sercheable': ('visible_username__icontains'),
            'limits': 50,
            'placeholder': 'Elige un responsable',
            'query': [
                (
                    ('organization__pk', 'self.request.session.get("organization")'),
                ),
            ],
        },
        'product': {
            'model': ['STR', 'Product'],
            'plugin': 'select2',
            'sercheable': ('codebar__icontains'),
            'limits': 50,
            'placeholder': 'Elige un producto', 
            'query': [
                (
                    ('organization__pk', 'self.request.session.get("organization")'),
                ),
            ],
        },
    },
}
class InventoryOrder(Model_base):
    OPERATIONTYPE = (
        ('ORDEN DE ENTREGA','ORDEN DE ENTREGA'),
        ('RECEPCION','RECEPCION'),
    )
    STATUS = (
        ('BORRADOR','BORRADOR'),
        ('EN ESPERA','EN ESPERA'),
        ('PREPARADO','PREPARADO'),
        ('HECHO','HECHO'),
    )
    organization = models.ForeignKey('mirari.Organization', blank=True, null=True, on_delete=models.CASCADE, related_name='+',)
    operationType = models.CharField('Tipo de operación', choices=OPERATIONTYPE, max_length=250)
    status = models.CharField('Estatus', choices=STATUS, max_length=250, default="BORRADOR")
    provider = models.ForeignKey('STR.Provider', blank=True, null=True, on_delete=models.SET_NULL, related_name='+', verbose_name="Proveedor")
    initialDateTime = models.DateTimeField(auto_now_add=True)
    finalDateTime = models.DateTimeField(blank=True, null=True)
    document = models.CharField('Documento de referencia', max_length=250, blank=True, null=True)
    priority = models.IntegerField('Prioridad', default=0)
    responsible = models.ForeignKey('mirari.User', blank=True, null=True, on_delete=models.SET_NULL, related_name='+', verbose_name="Responsable")
    notes = models.TextField('Notas', max_length=250, blank=True, null=True)
    product = models.ForeignKey('STR.Product', on_delete=models.CASCADE, related_name='+', blank=True, null=True)
    VARS = VARS
    class Meta(Model_base.Meta):
        verbose_name = VARS['NAME']
        verbose_name_plural = VARS['PLURAL']
        permissions = permissions(VARS)
    def __str__(self):
        return self.id


########################################################################################
VARS = {
    'NAME':'Producto de Orden de Inventario',
    'PLURAL':'Producto de Orden de Inventario',
    'MODEL':'InventoryOrderProduct',
    'NEW':'NUEVO',
    'NEW_GENDER': 'un nuevo',
    'THIS': 'este',
    'APP':APP,
    'EXCLUDE_PERMISSIONS': ['all'],
}
class InventoryOrderProduct(Model_base):
    STATUS = (
        ('BORRADOR','BORRADOR'),
        ('EN ESPERA','EN ESPERA'),
        ('PREPARADO','PREPARADO'),
        ('HECHO','HECHO'),
    )
    inventoryOrder = models.ForeignKey('STR.InventoryOrder', on_delete=models.CASCADE, related_name='+',)
    product = models.ForeignKey('STR.Product', on_delete=models.CASCADE, related_name='+',)
    quantity = models.IntegerField('Cantidad')
    VARS = VARS
    class Meta(Model_base.Meta):
        verbose_name = VARS['NAME']
        verbose_name_plural = VARS['PLURAL']
        permissions = permissions(VARS)
    def __str__(self):
        return self.id


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