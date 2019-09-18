# -*- coding: utf-8 -*-
from mirari.mirari.models import *
from .vars import *

from mirari.mirari.viewbase import Basic_Serializer

from imagekit.models import ImageSpecField, ProcessedImageField
from imagekit.processors import ResizeToFill

IVA = settings.IVA
IEPS = settings.IEPS

########################################################################################
VARS = {
    'NAME':'Punto de venta',
    'PLURAL':'Puntos de venta',
    'MODEL':'Sellpoint',
    'NEW':'NUEVO',
    'NEW_GENDER': 'un nuevo',
    'THIS': 'este',
    'APP':APP,
    'PAGEDetail': 'Sellpoint__CreateView.pug',
    'LIST': [
        {
            'field': 'name',
            'title': 'Nombre',
            'url': 'url_update',
            'sorteable': True,
            'serchable': True,
        },
        {
            'field': 'get_haveExpenses',
            'title': 'GASTOS',
            'url': 'url_update',
        },
        {
            'field': 'get_have_casher',
            'title': 'COBRA VENDEDOR?',
            'url': 'url_update',
        },
        {
            'field': 'number_tickets',
            'title': '# Tickets',
            'url': 'url_update',
        },
        {
            'field': 'getSerialNumber',
            'title': 'FOLIO',
            'url': 'url_update',
        },
        {
            'field': 'get_color',
            'title': 'COLOR',
            'url': 'url_update',
        },
        {
            'field': 'getPrinter',
            'title': 'IMPRESORA',
            'url': 'url_update',
        },
    ],
    'HIDE_BUTTONS_UPDATE': True,
    'SELECTQ': {
        'cashers': {
            'plugin': 'selectmultiple',
        },
        'vendors': {
            'plugin': 'selectmultiple',
        },
        'orders': {
            'plugin': 'selectmultiple',
        },
        'supervisors': {
            'plugin': 'selectmultiple',
        },
        'fiscalDataTickets': {
            'plugin': 'select2',
        },
        'fiscalDataCuts': {
            'plugin': 'select2',
        },
    },
    'FORM': ('name','have_casher','color','vendors','cashers','orders', 'supervisors','is_active','printer','barcode','number_tickets','haveExpenses','haveExchange','header_line_black_1','header_line_black_2','header_line_1','header_line_2','footer_line_1', 'fiscalDataTickets', 'fiscalDataCuts'),
}
class Sellpoint(Model_base):
    organization = models.ForeignKey('mirari.Organization', related_name='+', on_delete=models.CASCADE)
    name = models.CharField('Nombre del punto de venta', max_length=250)
    serial = models.ForeignKey('mirari.Serial', verbose_name="Serie de folios", related_name='+', on_delete=models.SET_NULL, null=True, blank=True, help_text='Asocia una serie a este punto de venta. <strong> Déjalo vacio para asignar folios aleatorios </strong>')
    creation_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)
    have_casher = models.BooleanField('Tiene Caja?', default=False, help_text='Tienes vendedores autorizados para cobrar en esta sucursal?')
    color = models.CharField('Color del Punto de Venta', max_length=50, default='#191919')
    number_tickets = models.IntegerField('Numero de tickets que imprime', default=1)
    header_line_black_1 = models.CharField('Linea 1 del encabezado del ticket', max_length=80, blank=True, null=True)
    header_line_black_2 = models.CharField('Linea 2 del encabezado del ticket', max_length=80, blank=True, null=True)
    header_line_1 = models.CharField('Linea 1 del texto del ticket', max_length=80, blank=True, null=True)
    header_line_2 = models.CharField('Linea 2 del texto del ticket', max_length=80, blank=True, null=True)
    footer_line_1 = models.CharField('Linea 1 del pie del ticket', max_length=80, blank=True, null=True)
    is_active = models.BooleanField('Esta activo?', default=True, help_text='Desactiva este punto de venta')
    cashers = models.ManyToManyField('mirari.User', verbose_name='Cajeros', blank=True, related_name='+',)
    vendors = models.ManyToManyField('mirari.User', verbose_name='Vendedores', blank=True, related_name='+',)
    supervisors = models.ManyToManyField('mirari.User', verbose_name='Supervisores', blank=True, related_name='+',)
    orders = models.ManyToManyField('mirari.User', verbose_name='Pedidos', blank=True, related_name='+',)
    printer = models.CharField('Impresora ID', max_length=80, blank=True, null=True)
    barcode = models.BooleanField('Muestra Escaner?', default=False, help_text='Activalo para conectar un escaner a una PC')
    haveExpenses = models.BooleanField('Crea Gastos?', default=True, help_text='Crea gastos esta sucursal?')
    haveExchange = models.BooleanField('Entrega cambio', default=False, help_text='Entrega cámbio?')

    have_credit = models.BooleanField('Tiene credito?', default=False, help_text='Tiene credito')
    have_credit_cards = models.BooleanField('Tiene credito?', default=False, help_text='Tiene credito')
    have_disscounts = models.BooleanField('Tiene credito?', default=False, help_text='Tiene credito')
    have_expenses = models.BooleanField('Tiene credito?', default=False, help_text='Tiene credito')
    have_orders = models.BooleanField('Tiene credito?', default=False, help_text='Tiene credito')
    priority = models.IntegerField('Numero de tickets que imprime', default=0)

    fiscalDataTickets = models.ForeignKey('INV.FiscalMX', blank=True, null=True, related_name='+', on_delete=models.SET_NULL, verbose_name="RFC que factura Tickets", help_text="Debes darlo de alta en la pestaña de Mi Factura")
    fiscalDataCuts = models.ForeignKey('INV.FiscalMX', blank=True, null=True, related_name='+', on_delete=models.SET_NULL, verbose_name="RFC que factura Cortes", help_text="Debes darlo de alta en la pestaña de Mi Factura")

    id_bckp = models.IntegerField(blank=True, null=True)

    VARS = VARS
    class Meta(Model_base.Meta):
        verbose_name = VARS['NAME']
        verbose_name_plural = VARS['PLURAL']
        permissions = permissions(VARS)
    def __str__(self):
        return '{0}'.format(self.name)
    def save(self, *args, **kwargs):
        self.name = self.name.upper()
        super().save()
        if not self.serial:
            content_type = ContentType.objects.get(app_label=APP, model=self.VARS['MODEL'].lower())
            serial = Serial.objects.create(organization=self.organization, name=self.name.lower(), content_type=content_type)
            self.serial = serial
            self.save()
    def QUERY(self, view):
        sellpoints = Sellpoint.objects.filter(organization__pk=view.request.session.get('organization'), active=True)
        if not view.request.user.is_superuser:
            sellpoints = sellpoints.filter(supervisors = view.request.user)
        return sellpoints
    def getMySellpoints(self, user):
        return Sellpoint.objects.filter(organization=user.organization, active=True, is_active=True).filter(Q(cashers=user)|Q(vendors=user)|Q(orders=user)).distinct()
    def getMySellpointsVendor(self, user):
        return Sellpoint.objects.filter(organization=user.organization, active=True, is_active=True).filter(vendors=user)
    def getMySellpointsCasher(self, user):
        return Sellpoint.objects.filter(organization=user.organization, active=True, is_active=True).filter(cashers=user)
    def getMySellpointsOrder(self, user):
        return Sellpoint.objects.filter(organization=user.organization, active=True, is_active=True).filter(orders=user)
    def getMySellpointsSupervisor(self, user):
        return Sellpoint.objects.filter(organization=user.organization, active=True, is_active=True).filter(supervisors=user)
    def get_have_casher(self):
        return self.render_boolean(not self.have_casher)
    def get_haveExpenses(self):
        return self.render_boolean(self.haveExpenses)
    def get_color(self):
        return self.render_color(self.color)
    def get_serial(self):
        return self.serial.get_serial()
    def getPrinter(self):
        return self.render_if(self.printer)
    def getCut(self):
        cut = Cut.objects.filter(sellpoint=self, final_time__isnull=True).first()
        if not cut:
            cut = Cut().new(self)
        return cut
    def lastCut(self):
        cut = Cut.objects.filter(sellpoint=self, final_time__isnull=False).first()
        if not cut:
            cut = Cut().new(self)
        return cut
    def getSerialNumber(self):
        return self.serial.serial
    def canStampTickets(self):
        if not self.fiscalDataTickets:
            return False
        if not self.fiscalDataTickets.noCer:
            return False
        return True
class SellpointSerializer(Basic_Serializer):
    class Meta(Basic_Serializer.Meta):
        model = Sellpoint
        fields = None
        exclude = ('active','creation_date','is_active','modified_date','serial',)

########################################################################################
VARS = {
    'NAME':'Menu',
    'PLURAL':'Menus',
    'MODEL':'Menu',
    'NEW':'NUEVO',
    'NEW_GENDER':'un nuevo',
    'THIS':'este',
    'APP':APP,
    'LIST': [
        {
            'field': 'get_name',
            'title': 'Nombre',
            'url': 'url_update',
        },
        {
            'field': 'get_color',
            'title': 'Color',
            'url': 'url_update',
        },
        {
            'field': 'get_is_active',
            'title': 'Activo?',
            'url': 'url_update',
        },
    ],
    'HIDE_BUTTONS_UPDATE': True,
    'FORM': ('name','color','parent','is_active'),
    'SELECTQ': {
        'parent': {
            'plugin': 'select2',
        },
    },
    'SEARCH': ['name'],
}
class Menu(Model_base, MPTTModel):
    organization = models.ForeignKey('mirari.Organization', on_delete=models.CASCADE)
    name = models.CharField('Nombre del menú', max_length=30)
    color = models.CharField('Color del menú', default='#3d3b56', max_length=100)
    is_active = models.BooleanField('Esta activo?', default=True, help_text='Desactiva todos los productos de un menú')
    parent = TreeForeignKey('self', null=True, blank=True, related_name='+', db_index=True, on_delete=models.PROTECT, verbose_name='Depende de?', help_text='Elige otro menú solo si este menú depende de otro')
    nivel = models.PositiveIntegerField(default=1)
    id_bckp = models.IntegerField(blank=True, null=True)
    VARS = VARS
    class Meta(Model_base.Meta):
        verbose_name = VARS['NAME']
        verbose_name_plural = VARS['PLURAL']
        permissions = permissions(VARS)
    def __str__(self):
        return '{0}'.format(self.name)
    def get_name(self):
        deep = '---' * len(self.get_ancestors(ascending=False, include_self=False))
        return deep+' '+self.name
    def get_color(self):
        return self.render_color(self.color)
    def get_is_active(self):
        return self.render_boolean(self.is_active)
    def get_parent(self):
        if self.parent:
            return self.render_if(self.parent.str_obj())
        else:
            return self.render_if(self.parent)
    def get_products(self):
        return Product.objects.filter(menu = self, is_active=True)
class MenuSerializer(Basic_Serializer):
    childrens = serializers.SerializerMethodField()
    descendants = serializers.SerializerMethodField()
    class Meta(Basic_Serializer.Meta):
        model = Menu
        fields = ('color','id','name','is_root_node','is_leaf_node','is_child_node','childrens','descendants')
    def get_childrens(self, obj):
        return MenuSerializer(obj.get_children(), many=True).data
    def get_descendants(self, obj):
        return MenuSerializer(obj.get_descendants(include_self=False), many=True).data

########################################################################################
VARS = {
    'NAME':'Producto',
    'PLURAL':'Productos',
    'MODEL':'Product',
    'NEW':'NUEVO',
    'NEW_GENDER':'un nuevo',
    'THIS':'este',
    'APP':APP,
    'LIST': [
        {
            'field': 'name',
            'title': 'Productos en sucursales',
            'template': '{{get_productattributes}}',
            'serchable': True,
        },
        {
            'field': 'get_name',
            'title': 'Información de producto',
            'template': 
                """
                    <a href="{{url_update}}" style="text-decoration:none;" class="a-no">
                        <span>
                            <strong class="mr-2">{{get_name}}</strong>{{get_is_active}}
                            <br /> 
                            {{get_menu}} {{get_photoIcon}}<br />
                            <small>
                                {{get_code}}<br /> 
                                {{get_units}}
                            </small>
                        </span>
                    </a>
                """,
        },
    ],
    'PAGEList': 'Product__ListView.pug',
    'SERIALIZER': ['get_code','get_units','get_is_active','get_productattributes','get_menu','get_sellpoint','get_photoIcon'],
    'FILTERS': {
        'is_active': {
            'size':'4',
            'label':'Mostrar activos?',
            'list': [
                [1,'Mostrar activos'],
                [0,'Mostrar desactivados'],
            ],
        },
        'menu': {
            'size':'4',
            'label':'Filtar Menu',
            'model':['SV','Menu'],
            'query':[
                (
                    ('organization','Organization.objects.get(pk=self.request.session.get("organization"))'),
                    ('active','True'),
                )
            ],
        }
    },
    'HIDE_CHECKBOX_LIST': True,
    'HIDE_BUTTONS_UPDATE': True,
    'FORM': [
        Div(
            Div(
                HTML('<h3 class="kt-section__title">INFORMACIÓN GENERAL</h3>'),
                Div('name'),
                Div('description'),
                Div('sellpoints'),
                Div('menu'),
                Div('is_active'),
                HTML('<h3 class="kt-section__title">FOTO DEL PRODUCTO</h3>'),
                Div('photo'),
            css_class="col-md-8"),
            Div(
                HTML('<h3 class="kt-section__title">DATOS SUGERIDOS</h3>'),
                Div('price'),
                Div(
                    Div('iva', css_class="col-md-6"),
                    Div('ieps', css_class="col-md-6"),
                    Div('is_dynamic', css_class="col-md-6"),
                    Div('is_favorite', css_class="col-md-6"),
                css_class="row"),
                HTML('<h3 class="kt-section__title">FACTURACIÓN</h3>'),
                Div('code'),
                Div('units'),
            css_class="col-md-4"),
        css_class="form-group m-form__group row"),
    ],
    'FORM_SIZE': ['col-xl-12','col-xl-12'],
    'SELECTQ': {
        'code': {
            'model': ['mirari', 'ProductsServicesSAT'],
            'query': 'none',
            'plugin': 'select2',
            'sercheable': ['code__icontains', 'name__icontains'],
            'limits': 50,
            'placeholder': 'Elige un producto o código del producto',
        },
        'units': {
            'model': ['mirari', 'UnitsCodesSat'],
            'query': 'none',
            'plugin': 'select2',
            'sercheable': ['code__icontains', 'name__icontains'],
            'limits': 50,
            'placeholder': 'Elige una unidad o código de la unidad',
        },
        'sellpoints': {
            'plugin': 'selectmultiple',
        },
        'menu': {
            'plugin': 'selectmultiple',
        },
    },
}
def pathProductImage(self, filename):
    upload_to = "O/%s%s/SV/Prod/%s" % (self.organization.id, self.organization.code, filename)
    return upload_to
class Product(Model_base):
    organization = models.ForeignKey('mirari.Organization', on_delete=models.CASCADE)
    name = models.CharField('Nombre del producto', max_length=250)
    description = models.CharField('Atributo o descripción', max_length=250, blank=True, null=True, help_text='Muy breve descripción del producto.')
    code = models.ForeignKey('mirari.ProductsServicesSAT', blank=True, null=True,on_delete=models.PROTECT, verbose_name="Código de producto en el SAT", help_text='Código de registro ante el SAT', related_name='+')
    units = models.ForeignKey('mirari.UnitsCodesSat', blank=True, null=True,on_delete=models.PROTECT, verbose_name="Código de unidad en el SAT", help_text="Unidad de medida para este producto", related_name='+')
    sellpoints = models.ManyToManyField('Sellpoint', related_name='+', verbose_name="Puntos de venta", help_text="Se vende en estas sucursales", blank=True, null=True)
    menu = models.ManyToManyField('Menu', related_name='+', verbose_name="Menus", help_text="Elige el o los menus donde se vende este producto")
    is_active = models.BooleanField('Esta activo?', default=True, help_text='Desactivar producto?')
    price = models.FloatField('Precio en esta sucursal ', default=0, help_text='Precio para todas las sucursales (sugerido)')
    iva = models.BooleanField('I.V.A. ', default=True, help_text='Este producto graba IVA? (sugerido)')
    ieps = models.BooleanField('IEPS. ', default=False, help_text='Este producto graba IEPS? (sugerido)')
    bar_code = models.CharField('Código de Barras ', max_length=250, blank=True, null=True, help_text='')
    is_dynamic = models.BooleanField('Precio dinámico ', default=False, help_text='El precio es dinámico? (sugerido)')
    is_favorite = models.BooleanField('Es favorito? ', default=False, help_text='Este producto es favorito? (sugerido)')
    photo = ProcessedImageField(upload_to=pathProductImage, processors=[ResizeToFill(100, 100)], format='JPEG', options={'quality': 60}, blank=True, null=True, verbose_name="Imagen del producto", help_text="Esta imagen se muestra en el botón del punto de venta")
    id_bckp = models.IntegerField(blank=True, null=True)
    VARS = VARS
    class Meta(Model_base.Meta):
        verbose_name = VARS['NAME']
        verbose_name_plural = VARS['PLURAL']
        permissions = permissions(VARS)
    def __str__(self):
        return mark_safe('{0} <small>({1})</small>'.format(self.name, self.description))
    def QUERY(self, view):
        return Product.objects.filter(organization__pk=view.request.session.get('organization'), active=True)
    def get_is_active(self):
        return self.render_boolean(self.is_active)
    def get_code(self):
        if self.code:
            return self.code.str_obj()
        else:
            return '-'
    def get_units(self):
        if self.units:
            return self.units.str_obj()
        else:
            return '-'
    def get_name(self):
        name = self.name
        if self.description:
            name += ' <small>' + self.description + '</small>'
        return name
    def get_menu(self):
        string_menu = ''
        for menu in self.menu.all():
            string_menu += mark_safe(self.render_boolean_del('<small class="m--font-'+menu.render_string_color(menu.is_active)+'"><i class="fa fa-circle mr-2" style="color:'+menu.color+'!important"></i>'+menu.name+'</small>', menu.is_active))
            string_menu += ', '
        return string_menu[0:len(string_menu)-2]
    def get_photoIcon(self):
        if self.photo:
            return '<i class="fas fa-photo"></i>'
        else:
            return  ''
    def get_productattributes(self):
        string = ''
        for sellpoint in self.sellpoints.all():
            productattributes = ProductAttributes.objects.get(product=self,sellpoint=sellpoint)
            quantity = int(productattributes.quantity)
            string += """
                    <a href="javascript:void(0)" class="getProduct" idProduct="{9}">
                        <div class="kt-portlet mb-1" style="border: 1px solid {10};background-color: #f1f1f1;">
                            <div class="row">
                                <div class="col-8 pr-1">
                                    <div class="kt-portlet__body pt-1 pb-2 px-3">
                                        <h6 class="text-dark"><span class="text-muted">PUNTO DE VENTA:</span> {8}</h6>
                                        <div class="kt-section__content kt-section__content--solid">
                                            <span id="iva__{9}">{2}</span>
                                            <span id="ieps__{9}">{3}</span>
                                            <span id="active__{9}">{7}</span>
                                            <span id="dynamic__{9}">{5}</span>
                                            <span id="favorite__{9}">{6}</span>
                                        </div>
                                    </div>
                                </div>
                                <div class="col-4 pl-1">
                                    <div class="kt-portlet__body pt-2 pb-0 px-3">
                                        <h6 class="text-dark"><span class="text-muted">PRECIO:</span> <span id="price__{9}">{1}</span></h6>
                                        <h6 class="text-dark"><span class="text-muted">EXISTENCIA:</span> <span id="quantity__{9}">{11}</span></h6>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </a>
                """.format(
                productattributes.get_alias(),
                productattributes.get_format_price(),
                productattributes.get_badge_iva(),
                productattributes.get_badge_ieps(),
                productattributes.get_bar_code(),
                productattributes.get_badge_is_dynamic(),
                productattributes.get_badge_is_favorite(),
                productattributes.get_badge_is_active(),
                productattributes.get_sellpoint(),
                productattributes.id,
                productattributes.sellpoint.color,
                quantity,
            )
        if not string:
            string = '<strong>No hay puntos de venta asociados</strong>'
        return mark_safe(string)
def sellpoints_changed(sender, **kwargs):
    action = kwargs.pop('action', None)
    instance = kwargs.pop('instance', None)
    if action == 'post_add':
        for sellpoint in instance.sellpoints.all():
            exist = ProductAttributes.objects.filter(product=instance,sellpoint=sellpoint).first()
            productAttributes = ProductAttributes.objects.get_or_create(product=instance,sellpoint=sellpoint)[0]
            productAttributes.active=True
            if not exist:
                productAttributes.price = instance.price
                productAttributes.iva = instance.iva
                productAttributes.ieps = instance.ieps
                productAttributes.bar_code = instance.bar_code
                productAttributes.is_dynamic = instance.is_dynamic
                productAttributes.is_favorite = instance.is_favorite
            productAttributes.save()
    if action == 'pre_remove':
        for sellpoint in instance.sellpoints.all():
            productAttributes = ProductAttributes.objects.get_or_create(product=instance,sellpoint=sellpoint)[0]
            productAttributes.active=False
            productAttributes.save()
m2m_changed.connect(sellpoints_changed, sender=Product.sellpoints.through)
class ProductSerializer(Basic_Serializer):
    class Meta(Basic_Serializer.Meta):
        model = Product

########################################################################################
VARS = {
    'NAME':'Atributo de producto',
    'PLURAL':'Atributos de producto',
    'MODEL':'ProductAttributes',
    'NEW':'NUEVO',
    'NEW_GENDER': 'un nuevo',
    'THIS':'este',
    'APP':APP,
    'EXCLUDE_PERMISSIONS': ['all'],
    'REDIRECT_MODEL':['SV','Product'],
    'FORM': ('alias','price','quantity','bar_code','iva','ieps','is_dynamic','is_favorite','is_active',),
    'RULES': """
        price: {
            min: 0,
        },
    """,
}
class ProductAttributes(Model_base):
    product = models.ForeignKey('Product', related_name='Product', on_delete=models.CASCADE)
    sellpoint = models.ForeignKey('Sellpoint', related_name='Sellpoint', on_delete=models.CASCADE)
    alias = models.CharField(max_length=250, blank=True, null=True, help_text="Nombre con el que se imprime este producto", default="")
    price = models.FloatField('Precio en esta sucursal',default=0)
    quantity = models.FloatField(default=0)
    iva = models.BooleanField('I.V.A.', default=True, help_text="Graba IVA?")
    ieps = models.BooleanField('IEPS.', default=True, help_text="Graba IEPS?")
    bar_code = models.CharField('Código de Barras', max_length=250, blank=True, null=True,)
    is_dynamic = models.BooleanField('Precio dinámico', default=False, help_text='Este producto tiene precio variable?')
    is_favorite = models.BooleanField('Es favorito?', default=False, help_text='Se muestra siempre este producto?')
    is_active = models.BooleanField('Esta activo?', default=True, help_text='Desactivar producto?')
    id_bckp = models.IntegerField(blank=True, null=True)
    VARS = VARS
    class Meta(Model_base.Meta):
        verbose_name = VARS['NAME']
        verbose_name_plural = VARS['PLURAL']
        permissions = permissions(VARS)
    def __str__(self):
        return '{0} | {1}'.format(self.sellpoint, self.product.name)
    def my_organization(self):
        return self.sellpoint.my_organization()
    def check_is_active(self):
        if not self.product.is_active:
            return False
        elif not self.product.menu.is_active:
            return False
        elif not self.sellpoint.is_active:
            return False
        return self.is_active
    def get_format_price(self):
        return '${:20,.2f}'.format(self.price)
    def get_alias(self):
        name = self.product.name
        if self.product.description:
            name += self.product.description
        return name
    def get_bar_code(self):
        return self.render_if(self.bar_code)
    def get_badge_iva(self):
        return mark_safe('<span class="kt-badge kt-badge--'+self.render_string_color(self.iva)+' kt-badge--inline">I.V.A.</span>')
    def get_badge_ieps(self):
        return mark_safe('<span class="kt-badge kt-badge--'+self.render_string_color(self.ieps)+' kt-badge--inline">IEPS</span>')
    def get_badge_is_dynamic(self):
        return mark_safe('<span class="kt-badge kt-badge--'+self.render_string_color(self.is_dynamic)+' kt-badge--inline">Dinámico</span>')
    def get_badge_is_favorite(self):
        return mark_safe('<span class="kt-badge kt-badge--'+self.render_string_color(self.is_favorite)+' kt-badge--inline">Favorito</span>')
    def get_badge_is_active(self):
        return mark_safe('<span class="kt-badge kt-badge--'+self.render_string_color(self.is_active)+' kt-badge--inline">Activo</span>')
    def get_sellpoint(self):
        return mark_safe(self.render_boolean_del('<span class="kt--font-'+self.sellpoint.render_string_color(self.sellpoint.is_active)+'" style="color:'+self.sellpoint.color+'!important">'+self.sellpoint.name+'</span>', self.sellpoint.is_active))
class ProductAttributesSerializer(Basic_Serializer):
    product = serializers.SerializerMethodField()
    class Meta(Basic_Serializer.Meta):
        model = ProductAttributes
        fields = None
        exclude = ('active',)
    def get_product(self, obj):
        return ProductSerializer(obj.product, read_only=True).data

########################################################################################
VARS = {
    'NAME':'Ticket',
    'PLURAL':'Tickets',
    'MODEL':'Ticket',
    'NEW':'NUEVO',
    'NEW_GENDER': 'un nuevo',
    'THIS':'este',
    'APP':APP,
    'EXCLUDE_PERMISSIONS': ['create','delete'],
    'LIST': [
        {
            'field': 'barcode',
            'title': 'Folio',
            'serchable': True,
            'template': 
            """
                <a href="#" ticket={{id}} style="text-decoration:none;" class="a-no getTicket">
                    {{barcode}}
                </a>
            """,
        },
        {
            'field': 'getSellpointName',
            'title': 'Punto de Venta',
            'template': 
            """
                <a href="#" ticket={{id}} style="text-decoration:none;color:{{getSellpointColor}}!important;" class="a-no getTicket">
                    {{getSellpointName}}
                </a>
            """,
        },
        {
            'field': 'ticketType',
            'title': 'Tipo',
            'template': 
            """
                <a href="#" ticket={{id}} style="text-decoration:none;" class="a-no getTicket">
                    {{ticketType}}
                </a>
            """,
        },
        {
            'field': 'status',
            'title': 'ESTATUS',
            'template': 
            """
                <a href="#" ticket={{id}} id ="statusTicket{{id}}" style="text-decoration:none;" class="a-no getTicket">
                    {{status}}
                </a>
            """,
        },
        {
            'field': 'getDate',
            'title': 'Fecha/Hora',
            'template': 
            """
                <a href="#" ticket={{id}} style="text-decoration:none;" class="a-no getTicket">
                    {{getDate}}
                </a>
            """,
        },
        {
            'field': 'getCut',
            'title': 'Corte',
            'template': 
            """
                <a href="#" ticket={{id}} style="text-decoration:none;" class="a-no getTicket">
                    {{getCut}}
                </a>
            """,
        },
        {
            'field': 'getOnAccount',
            'title': 'A cuenta',
            'template': 
            """
                <a href="#" ticket={{id}} style="text-decoration:none;" class="a-no getTicket">
                    {{getOnAccount.MXN}}
                </a>
            """,
        },
        {
            'field': 'getTotal',
            'title': 'TOTAL',
            'template': 
            """
                <a href="#" ticket={{id}} style="text-decoration:none;" class="a-no getTicket">
                    {{getTotal.TOTAL.MXN}}
                </a>
            """,
        },
    ],
    'PAGELENGTH': 50,
    'HIDE_CHECKBOX_LIST': True,
    'HIDE_BUTTONS_LIST': True,
    'SERIALIZER': ['getSellpointColor'],
    'FILTERS': {
        'status': {
            'size':'4',
            'label':'Filtrar estatus',
            'list': [
                ['COBRADO','Mostrar Cobrados'],
                ['PENDIENTE','Mostrar Pendientes'],
            ],
        },
        'sellpoint': {
            'size':'4',
            'label':'Punto de venta',
            'model':['SV','Sellpoint'],
            'query':[
                (
                    ('organization','Organization.objects.get(pk=self.request.session.get("organization"))'),
                    ('active','True'),
                    ('is_active','True'),
                    ('supervisors','self.request.user'),
                )
            ],
        }
    },
    'PAGEList': 'Ticket__ListView.pug',
}
class Ticket(Model_base):
    STATUS_TICKET = (
        ('COBRADO','COBRADO'),
        ('PENDIENTE','PENDIENTE'),
        ('CANCELADO','CANCELADO'),
    )
    TICKETTYPE = (
        ('VENTA','VENTA'),
        ('REMISION','REMISION'),
        ('DEVOLUCION','DEVOLUCION'),
        ('GASTO','GASTO'),
    )
    sellpoint = models.ForeignKey('Sellpoint', null=True, blank=True, on_delete=models.SET_NULL)
    barcode = models.CharField(max_length=13, default="0000000000000")
    key = models.CharField(max_length=12)
    user = models.ForeignKey('mirari.User', null=True, blank=True, on_delete=models.SET_NULL)
    username = models.CharField(max_length=250, null=True, blank=True)
    status = models.CharField(choices=STATUS_TICKET, max_length=50, default="PENDIENTE")
    date = models.DateTimeField(auto_now_add=True)
    format_time = models.CharField(max_length=50, null=True, blank=True)
    format_date = models.CharField(max_length=50, null=True, blank=True)
    cut = models.ForeignKey('Cut', null=True, blank=True, on_delete=models.SET_NULL)
    total = models.FloatField(default=0)
    iva = models.FloatField(default=0)
    ieps = models.FloatField(default=0)
    onAccount = models.FloatField(default=0)
    client = models.ForeignKey('Client', null=True, blank=True, on_delete=models.SET_NULL)
    clientID = models.CharField(max_length=20, null=True, blank=True)
    clientName = models.CharField(max_length=250, null=True, blank=True)
    datetimeOfDelivery = models.DateTimeField(null=True, blank=True)
    destination = models.CharField(max_length=250, null=True, blank=True)
    notes = models.TextField(null=True, blank=True)
    email = models.CharField(max_length=250, null=True, blank=True)
    phone = models.CharField(max_length=15, null=True, blank=True)
    rfc = models.CharField(max_length=20, null=True, blank=True)
    ticketType = models.CharField(choices=TICKETTYPE, max_length=100, default="VENTA")
    rasurado = models.BooleanField(default=False)
    invoiced = models.BooleanField(default=False)
    creditPayment = models.BooleanField(default=False)
    id_bckp = models.IntegerField(blank=True, null=True)
    VARS = VARS
    class Meta(Model_base.Meta):
        verbose_name = VARS['NAME']
        verbose_name_plural = VARS['PLURAL']
        permissions = permissions(VARS)
    def __str__(self):
        return '{0} | {1}'.format(self.sellpoint, self.barcode)
    def QUERY(self, view):
        return Ticket.objects.filter(sellpoint__organization__pk=view.request.session.get('organization'), active=True, sellpoint__supervisors=view.request.user)
    def my_organization(self):
        return self.sellpoint.my_organization()
    def new(self, ticket):
        self.sellpoint = Sellpoint.objects.get(id = ticket['sellpoint']['id'])
        lastTicket = Ticket.objects.filter(key=ticket['key'], total=ticket['total'], sellpoint=self.sellpoint).first()
        if lastTicket:
            return lastTicket
        self.barcode = self.sellpoint.get_serial()
        self.key = ticket['key']
        self.user = User.objects.get(id=ticket['user'])
        self.username = self.user.visible_username
        self.status = ticket['status']
        self.format_time = ticket['format_time']
        self.format_date = ticket['format_date']
        self.total = ticket['total']
        self.iva = ticket['iva']
        self.ieps = ticket['ieps']
        self.ticketType = ticket['ticketType']
        self.onAccount = ticket['onAccount']
        if ticket['clientID']:
            client = Client.objects.filter(uid=ticket['clientID']).filter(organization=self.sellpoint.organization).first()
            if not client:
                client = Client().createFromTicket(ticket, self.sellpoint)
            self.client = client
            self.clientID = ticket['clientID']
            self.client.balance -= float(self.total) - float(self.onAccount)
            self.client.save()
            if ticket['clientName']:
                self.clientName = ticket['clientName']
            else:
                self.clientName = ticket['clientID']
            if ticket.get('datetimeOfDelivery'):
                self.datetimeOfDelivery = datetime.datetime.strptime(ticket['datetimeOfDelivery'], '%d/%m/%Y %H:%M:%S')
            self.destination = ticket.get('destination')
            self.notes = ticket.get('notes')
            self.email = ticket.get('email')
            self.phone = ticket.get('phone')
            self.rfc = ticket.get('rfc')
        self.cut = self.sellpoint.getCut()
        self.save()
        self.cut.ticketTypes.add(self.ticketType)
        for product in ticket['products']:
            TicketProducts().addTicket(self, product)
        return self
    def scanner(self):
        if (self.status == 'PENDIENTE'):
            self.status = 'COBRADO'
            self.save()
        return self
    def getProducts(self):
        return TicketProducts.objects.filter(ticket=self)
    def getOnAccount(self):
        if not self.onAccount:
            return {
                'INT': 0,
                'MXN': '-',
            }
        return {
            'INT': self.onAccount,
            'MXN': Money( "{0:.2f}".format(float(self.onAccount)), Currency.MXN).format('es_MX'),
        }
    def getTotal(self):
        totaldiscounts = 0
        for ticketProduct in self.getProducts():
            totaldiscounts += ticketProduct.getTotalDisscount()
        return {
            'TOTALDISCOUNTS':{
                'INT': totaldiscounts,
                'MXN': Money( "{0:.2f}".format(totaldiscounts), Currency.MXN).format('es_MX'),
            },
            'TOTAL':{
                'INT': self.total,
                'MXN': Money( "{0:.2f}".format(self.total), Currency.MXN).format('es_MX'),
            }
        }
    def getSubTotal(self):
        return {
            'INT': self.total - self.iva - self.ieps,
            'MXN': Money( "{0:.2f}".format(self.total - self.iva - self.ieps), Currency.MXN).format('es_MX'),
        }
    def getIva(self):
        return {
            'INT': self.iva,
            'MXN': Money( "{0:.2f}".format(self.iva), Currency.MXN).format('es_MX'),
        }
    def getIeps(self):
        return {
            'INT': self.ieps,
            'MXN': Money( "{0:.2f}".format(self.ieps), Currency.MXN).format('es_MX'),
        }
    def getLens(self):
        return {
            'PRODUCTS': len(self.getProducts()),
            'OFFERSTYPE': len(self.getOffersType()),
            'OFFERSTOTAL': len(self.getOffersTotal()),
            'PRODUCTSWITHOFFERS': len(self.getProductsWithOffers()),
        }
    def getOffersType(self):
        offers = []
        for ticketProduct in self.getProducts():
            for offer in ticketProduct.offers.all():
                if not offer in offers:
                    offers.append(offer)
        return offers
    def getOffersTotal(self):
        offers = []
        for ticketProduct in self.getProducts():
            for offer in ticketProduct.offers.all():
                offers.append(offer)
        return offers
    def getProductsWithOffers(self):
        products = []
        for ticketProduct in self.getProducts():
            if len(ticketProduct.offers.all())>0:
                if not ticketProduct.product in products:
                    products.append(ticketProduct.product)
        return products
    def stampTicket(self, cfdiReceptorRfc='', cfdiReceptorNombre='', cfdiReceptorUsocfdi='', receptorRfc='CAMG890722JB7', receptorRazonSocial='g@gustavo-castellanos.com', zipCode='06500'):
        INV = {}
        INV['organization'] = self.sellpoint.organization
        INV['serie'] = 'SuVenta'
        INV['folio'] = self.barcode
        INV['fecha'] = str(datetime.datetime.now().isoformat())[:19]
        INV['noCertificado'] = self.sellpoint.fiscalDataTickets.noCer
        INV['moneda'] = 'MXN'
        INV['tipoDeComprobante'] = 'I'
        INV['condicionesDePago'] = 'CONDICIONES'
        INV['lugarExpedicion'] = zipCode
        INV['metodoPago'] = 'PUE'
        INV['formaPago'] = '01'
        INV['cfdiEmisorRfc'] =  self.sellpoint.fiscalDataTickets.rfc
        INV['cfdiEmisorNombre'] = self.sellpoint.fiscalDataTickets.razonSocial
        INV['cfdiEmisorRegimenFiscal'] = '601'
        INV['cfdiReceptorRfc'] = receptorRfc.upper()
        INV['cfdiReceptorNombre'] = receptorRazonSocial
        INV['cfdiReceptorUsocfdi'] = 'G03'
        INV['cfdiEmisorStreet'] = self.sellpoint.fiscalDataTickets.street
        INV['cfdiEmisorExtNumber'] = self.sellpoint.fiscalDataTickets.extNumber
        INV['cfdiEmisorIntNumber'] = self.sellpoint.fiscalDataTickets.intNumber
        INV['cfdiEmisorRegion'] = self.sellpoint.fiscalDataTickets.region
        INV['cfdiEmisorProvince'] = self.sellpoint.fiscalDataTickets.province
        INV['cfdiEmisorState'] = self.sellpoint.fiscalDataTickets.state
        INV['cfdiEmisorZipcode'] = self.sellpoint.fiscalDataTickets.zipcode
        INV['cfdiEmisorCountry'] = self.sellpoint.fiscalDataTickets.country
        conceptos = []
        impuestos = 0
        total = 0
        descuentos = 0
        for ticketProduct in self.getProducts():
            if  ticketProduct.offerprice > 0:
                try:
                    claveProdServ = ticketProduct.product.code.code
                    claveUnidad = ticketProduct.product.product.units.codigo
                    nombreUnidad = ticketProduct.product.product.units.nombre
                except:
                    claveProdServ = '50181900'
                    claveUnidad = 'H87'
                    nombreUnidad = 'Pieza'
                impuestosBase = 1
                if ticketProduct.iva:
                    impuestosBase+=.16
                if ticketProduct.ieps:
                    impuestosBase+=.08
                cantidad=float('{0:.1f}'.format(ticketProduct.quantity))
                valorUnitario=float('{0:.2f}'.format(ticketProduct.offerprice))/impuestosBase
                c = {
                    'claveProdServ':claveProdServ,
                    'claveUnidad':claveUnidad,
                    'unidad':nombreUnidad,
                    'cantidad':'{0:.1f}'.format(cantidad),
                    'noIdentificacion':'01',
                    'descripcion':ticketProduct.productName,
                    'valorUnitario':'{0:.2f}'.format(valorUnitario),
                    'importe':'{0:.2f}'.format(cantidad*valorUnitario),
                    'descuento':'{0:.2f}'.format(ticketProduct.getTotalDisscount()),
                    'impuestosTransladados':[],
                }
                if ticketProduct.iva:
                    impuestosTransladados = {
                        'base':c['importe'],
                        'impuesto':'002',
                        'tipoFactor':'Tasa',
                        'tasaoCuota':'{0:.6f}'.format(IVA),
                        'importe':'{0:.2f}'.format(float(c['importe'])*IVA),
                    }
                    c['impuestosTransladados'].append(impuestosTransladados)
                    impuestos += float(impuestosTransladados['importe'])
                if ticketProduct.ieps:
                    impuestosTransladados = {
                        'base':c['importe'],
                        'impuesto':'003',
                        'tipoFactor':'Tasa',
                        'tasaoCuota':'{0:.6f}'.format(IEPS),
                        'importe':'{0:.2f}'.format(float(c['importe'])*IEPS),
                    }
                    c['impuestosTransladados'].append(impuestosTransladados)
                    impuestos += float(impuestosTransladados['importe'])
                conceptos.append(c)
                total += float(c['importe'])
        INV['conceptos'] = conceptos
        INV['subTotal'] = '{0:.2f}'.format(total)
        INV['total'] = '{0:.2f}'.format(total+impuestos)
        return self.sellpoint.fiscalDataTickets.makeInvoice(INV)
    def getCutSerial(self):
        return self.cut.serial
    def getSellpointName(self):
        return self.sellpoint.name
    def getSellpointColor(self):
        return self.sellpoint.color
    def getDate(self):
        return mark_safe(self.render_datetime(self.date) +' <br/> <small>'+self.format_date+' '+self.format_time+'</small>')
    def getCut(self):
        return self.cut.serial
class TicketSerializer(Basic_Serializer):
    sellpoint = serializers.SerializerMethodField()
    products = serializers.SerializerMethodField()
    getOnAccount = serializers.ReadOnlyField()
    getTotal = serializers.ReadOnlyField()
    getSubTotal = serializers.ReadOnlyField()
    getIva = serializers.ReadOnlyField()
    getIeps = serializers.ReadOnlyField()
    getLens = serializers.ReadOnlyField()
    class Meta(Basic_Serializer.Meta):
        model = Ticket
    def get_sellpoint(self, obj):
        return SellpointSerializer(obj.sellpoint, read_only=True).data
    def get_products(self, obj):
        return TicketProductsSerializer(TicketProducts.objects.filter(ticket=obj), many=True).data
class TicketsSerializer(Basic_Serializer):
    class Meta(Basic_Serializer.Meta):
        model = Ticket
########################################################################################
VARS = {
    'NAME':'Producto del ticket',
    'PLURAL':'Productos del ticket',
    'MODEL':'TicketProducts',
    'NEW':'NUEVO',
    'NEW_GENDER': 'un nuevo',
    'THIS':'este',
    'APP':APP,
    'EXCLUDE_PERMISSIONS': ['all'],
}
class TicketProducts(Model_base):
    ticket = models.ForeignKey('Ticket', on_delete=models.CASCADE, null=True)
    product = models.ForeignKey('ProductAttributes', null=True, on_delete=models.SET_NULL)
    productName = models.CharField(max_length=250, null=True, blank=True)
    alias = models.CharField(max_length=250, null=True, blank=True)
    quantity = models.FloatField(default=0)
    price = models.FloatField(default=0)
    offerprice = models.FloatField(default=0)
    total = models.FloatField(default=0)
    iva = models.FloatField(default=0)
    ieps = models.FloatField(default=0)
    offers = models.ManyToManyField('Offer', related_name='+', blank=True)
    id_bckp = models.IntegerField(blank=True, null=True)
    VARS = VARS
    class Meta(Model_base.Meta):
        verbose_name = VARS['NAME']
        verbose_name_plural = VARS['PLURAL']
        permissions = permissions(VARS)
    def __str__(self):
        return '{0} | {1}'.format(self.product, self.ticket)
    def my_organization(self):
        return self.ticket.my_organization()
    def addTicket(self, ticket, product):
        self.ticket = ticket
        self.product = ProductAttributes.objects.get(id=product['id'])
        self.productName = product['productName']
        self.alias = product['alias']
        self.quantity = product['quantity']
        self.price = product['price']
        self.offerprice = product['offerprice']
        self.total = product['total']
        self.iva = product['ivaTotal']
        self.ieps = product['iepsTotal']
        self.save()
        self.product.quantity -= self.quantity
        self.product.save()
        for offer in product['offers']:
            self.offers.add(Offer.objects.get(id=offer['id']))
        return self
    def getTotalDisscount(self):
        if not self.price == self.offerprice:
            return self.total - (self.offerprice * self.quantity)
        return 0
class TicketProductsSerializer(Basic_Serializer):
    offers = serializers.SerializerMethodField()
    getTotalDisscount = serializers.ReadOnlyField()
    class Meta(Basic_Serializer.Meta):
        model = TicketProducts
    def get_offers(self, obj):
        return OfferSerializer(obj.offers.all(), many=True).data

########################################################################################
VARS = {
    'NAME':'Corte',
    'PLURAL':'Cortes',
    'MODEL':'Cut',
    'NEW':'NUEVO',
    'NEW_GENDER': 'un nuevo',
    'THIS':'este',
    'APP':APP,
    'EXCLUDE_PERMISSIONS': ['create','update','delete'],
    'EXTEND_PERMISSIONS': [('Can_Change__Cuts', 'Modifica cortes'),],
    'PAGEList': 'Cut__ListView.pug',
    'PAGEDetail': 'Cut__DetailView.pug',
    'LIST': [
        {
            'field':"url_delete", 
            'title':"#", 
            'width':40, 
            'select':'true', 
            'permission': ('Can_Change__Cuts',),
        },
        {
            'field': 'serial',
            'title': 'Folio',
            'width': 100,
            'template': 
            """
                <a href="{{url_detail}}" style="text-decoration:none;color:{{getColor}}!important;">
                    {{serial}}
                </a>
            """,
        },
        {
            'field': 'getFinal_time',
            'title': 'Fecha/Hora',
            'template': 
            """
                <a href="{{url_detail}}" style="text-decoration:none;color:{{getColor}}!important;">
                    <strong>{{getFinal_time}}</strong>
                    <br />
                    <small>{{getSellpoint}}</small>
                </a>
            """,
        },
        {
            'field': 'id',
            'title': 'IMPUESTOS',
            'template': 
            """
                <a href="{{url_detail}}" style="text-decoration:none;color:{{getColor}}!important;">
                    IVA: {{getIvaDetail.__ALL.COBRADO.MXN}} <br />
                    IEPS: {{getIepsDetail.__ALL.COBRADO.MXN}} <br />
                    Subtotal: {{getSubTotalDetail.__ALL.COBRADO.MXN}} <br />
                </a>
            """,
        },
        {
            'field': 'getLens',
            'title': 'Faltates',
            'template': 
            """
                <a href="{{url_detail}}" style="text-decoration:none;color:{{getColor}}!important;">
                    <strong>{{getTotalDetail.__ALL.PENDIENTE.MXN}}</strong> <br /> 
                    #{{getLens.__ALL.PENDIENTE}} tickets
                </a>
            """,
        },
        {
            'field': 'id',
            'title': 'Totales',
            'template': 
            """
                <a href="{{url_detail}}" style="text-decoration:none;color:{{getColor}}!important;">
                    <strong>{{getTotalDetail.__ALL.COBRADO.MXN}}</strong> <br />
                    #{{getLens.__ALL.TOTAL}} clientes <br />
                    <small>+Faltante:</small> {{getTotalDetail.__ALL.TOTAL.MXN}}<br />
                </a>
            """,
        },
        {
            'field': 'rasurado',
            'title': 'Rasurado',
            'permission': ('Can_Change__Cuts',),
        },
    ],
    'SERIALIZER': ('getColor','getSellpoint','getIvaDetail','getIepsDetail','getSubTotalDetail','getTotalDetail'),
    'FILTERS': {
            'sellpoint': {
            'size':'4',
            'label':'Punto de venta',
            'model':['SV','Sellpoint'],
            'query':[
                (
                    ('organization','Organization.objects.get(pk=self.request.session.get("organization"))'),
                    ('is_active','True'),
                    ('active','True'),
                    ('supervisors','self.request.user'),
                )
            ],
        }
    },
}
negativeTicketTypes = ('DEVOLUCION','GASTO')
class Cut(Model_base):
    sellpoint = models.ForeignKey('Sellpoint', null=True, blank=True, on_delete=models.SET_NULL)
    initial_time = models.DateTimeField(auto_now_add=True)
    final_time = models.DateTimeField(null=True, blank=True,)
    rasurado = models.PositiveIntegerField(default=100)
    serial = models.IntegerField(default=1)
    show = models.BooleanField(default=True)
    ticketTypes = TaggableManager()
    id_bckp = models.IntegerField(blank=True, null=True)
    VARS = VARS
    class Meta(Model_base.Meta):
        verbose_name = VARS['NAME']
        verbose_name_plural = VARS['PLURAL']
        permissions = permissions(VARS)
    def __str__(self):
        return '{0}'.format(self.id)
    def QUERY(self, view):
        cuts = Cut.objects.filter(sellpoint__organization__pk=view.request.session.get('organization'), active=True)
        if not view.request.user.is_superuser:
            cuts = cuts.filter(sellpoint__supervisors = view.request.user)
        return cuts.order_by('-final_time')
    def my_organization(self):
        return self.sellpoint.my_organization()
    ########
    def new(self, sellpoint):
        self.sellpoint = sellpoint
        cut = Cut.objects.filter(sellpoint = self.sellpoint).first()
        if cut:
            self.serial = cut.serial + 1
        self.save()
        return self
    def makeCut(self):
        if self.getLens()['__ALL']['TOTAL']:
            self.final_time = datetime.datetime.now()
            self.save()
        else:
            return False
        return self
    def makeRasurado(self, value):
        total = 0
        value = int(value)
        tickets = self.getTickets(hideRasurado=False)
        tickets.update(rasurado=False)
        for ticket in tickets:
            total += ticket.total
        finaltotal = total * value / 100
        for ticket in tickets.exclude(invoiced=True).order_by('-total'):
            if total <= finaltotal:
                break
            else:
                ticket.rasurado = True
                ticket.save()
                total -= ticket.total
        self.rasurado = value
        self.save()
        return True
    def getTickets(self, status='', ticketType='', hideRasurado=True):
        tickets = Ticket.objects.filter(cut=self)
        if status:
            tickets = tickets.filter(status=status)
        if ticketType:
            tickets = tickets.filter(ticketType=ticketType)
        if hideRasurado:
            tickets = tickets.exclude(rasurado=True)
        return tickets
    def getIva(self, status='', ticketType=''):
        iva = 0
        for ticket in self.getTickets(status=status, ticketType=ticketType):
            iva += ticket.iva
        return "{0:.2f}".format(iva)
    def getIeps(self, status='', ticketType=''):
        ieps = 0
        for ticket in self.getTickets(status=status, ticketType=ticketType):
            ieps += ticket.ieps
        return "{0:.2f}".format(ieps)
    def getSubtotal(self, status='', ticketType=''):
        total = 0
        for ticket in self.getTickets(status=status, ticketType=ticketType):
            total += ticket.total - ticket.ieps - ticket.iva
        return "{0:.2f}".format(total)
    def getTotal(self, status='', ticketType=''):
        total = 0
        for ticket in self.getTickets(status=status, ticketType=ticketType):
            ticketTotal = ticket.total
            if ticket.onAccount > 0:
                ticketTotal = ticket.onAccount
            if ticket.ticketType in negativeTicketTypes:
                ticketTotal = ticketTotal * -1
            total += ticketTotal
        return "{0:.2f}".format(total)
    def getCutProducts(self, status='', ticketType=''):
        products = []
        for ticket in self.getTickets(status=status, ticketType=ticketType):
            for product in ticket.getProducts():
                cutProduct = CutProduct(product)
                exist = False    
                for cutproduct in products:
                    if cutproduct.productName == product.productName and cutproduct.price == product.price:
                        cutProduct = cutproduct.update(product)
                        exist = True
                        break
                cutProduct.addOffers(product)
                if not exist:
                    products.append(cutProduct)
        return sorted(products, key=lambda x: x.quantity, reverse=True)
    ########
    def getIvaDetail(self):
        cobrado = float(self.getIva(status='COBRADO'))
        pendiente = float(self.getIva(status='PENDIENTE'))
        cancelado = float(self.getIva(status='CANCELADO'))
        total = float("{0:.2f}".format(cobrado + pendiente))
        result = {'__ALL':{
            'COBRADO': {
                'NUMBER': cobrado,
                'MXN': Money(str(cobrado), Currency.MXN).format('es_MX'),
            },
            'PENDIENTE': {
                'NUMBER': pendiente,
                'MXN': Money(str(pendiente), Currency.MXN).format('es_MX'),
            },
            'CANCELADO': {
                'NUMBER': cancelado,
                'MXN': Money(str(cancelado), Currency.MXN).format('es_MX'),
            },
            'TOTAL': {
                'NUMBER': total,
                'MXN': Money(str(total), Currency.MXN).format('es_MX'),
            },
        }}
        if len(self.ticketTypes.all()) > 1:
            for ttype in self.ticketTypes.all():
                cobrado = float(self.getIva(status='COBRADO', ticketType=ttype))
                pendiente = float(self.getIva(status='PENDIENTE', ticketType=ttype))
                cancelado = float(self.getIva(status='CANCELADO', ticketType=ttype))
                total = float("{0:.2f}".format(cobrado + pendiente))
                result[str(ttype)]={
                    'COBRADO': {
                        'NUMBER': cobrado,
                        'MXN': Money(str(cobrado), Currency.MXN).format('es_MX'),
                    },
                    'PENDIENTE': {
                        'NUMBER': pendiente,
                        'MXN': Money(str(pendiente), Currency.MXN).format('es_MX'),
                    },
                    'CANCELADO': {
                        'NUMBER': cancelado,
                        'MXN': Money(str(cancelado), Currency.MXN).format('es_MX'),
                    },
                    'TOTAL': {
                        'NUMBER': total,
                        'MXN': Money(str(total), Currency.MXN).format('es_MX'),
                    },
                }
        return result
    def getIepsDetail(self):
        cobrado = float(self.getIeps(status='COBRADO'))
        pendiente = float(self.getIeps(status='PENDIENTE'))
        cancelado = float(self.getIeps(status='CANCELADO'))
        total = float("{0:.2f}".format(cobrado + pendiente))
        result = {'__ALL':{
            'COBRADO': {
                'NUMBER': cobrado,
                'MXN': Money(str(cobrado), Currency.MXN).format('es_MX'),
            },
            'PENDIENTE': {
                'NUMBER': pendiente,
                'MXN': Money(str(pendiente), Currency.MXN).format('es_MX'),
            },
            'CANCELADO': {
                'NUMBER': cancelado,
                'MXN': Money(str(cancelado), Currency.MXN).format('es_MX'),
            },
            'TOTAL': {
                'NUMBER': total,
                'MXN': Money(str(total), Currency.MXN).format('es_MX'),
            },
        }}
        if len(self.ticketTypes.all()) > 1:
            for ttype in self.ticketTypes.all():
                cobrado = float(self.getIeps(status='COBRADO', ticketType=ttype))
                pendiente = float(self.getIeps(status='PENDIENTE', ticketType=ttype))
                cancelado = float(self.getIeps(status='CANCELADO', ticketType=ttype))
                total = float("{0:.2f}".format(cobrado + pendiente))
                result[str(ttype)]={
                    'COBRADO': {
                        'NUMBER': cobrado,
                        'MXN': Money(str(cobrado), Currency.MXN).format('es_MX'),
                    },
                    'PENDIENTE': {
                        'NUMBER': pendiente,
                        'MXN': Money(str(pendiente), Currency.MXN).format('es_MX'),
                    },
                    'CANCELADO': {
                        'NUMBER': cancelado,
                        'MXN': Money(str(cancelado), Currency.MXN).format('es_MX'),
                    },
                    'TOTAL': {
                        'NUMBER': total,
                        'MXN': Money(str(total), Currency.MXN).format('es_MX'),
                    },
                }
        return result
    def getSubTotalDetail(self):
        cobrado = float(self.getSubtotal(status='COBRADO'))
        pendiente = float(self.getSubtotal(status='PENDIENTE'))
        cancelado = float(self.getSubtotal(status='CANCELADO'))
        total = float("{0:.2f}".format(cobrado + pendiente))
        result = {'__ALL':{
            'COBRADO': {
                'NUMBER': cobrado,
                'MXN': Money(str(cobrado), Currency.MXN).format('es_MX'),
            },
            'PENDIENTE': {
                'NUMBER': pendiente,
                'MXN': Money(str(pendiente), Currency.MXN).format('es_MX'),
            },
            'CANCELADO': {
                'NUMBER': cancelado,
                'MXN': Money(str(cancelado), Currency.MXN).format('es_MX'),
            },
            'TOTAL': {
                'NUMBER': total,
                'MXN': Money(str(total), Currency.MXN).format('es_MX'),
            },
        }}
        if len(self.ticketTypes.all()) > 1:
            for ttype in self.ticketTypes.all():
                cobrado = float(self.getSubtotal(status='COBRADO', ticketType=ttype))
                pendiente = float(self.getSubtotal(status='PENDIENTE', ticketType=ttype))
                cancelado = float(self.getSubtotal(status='CANCELADO', ticketType=ttype))
                total = float("{0:.2f}".format(cobrado + pendiente))
                result[str(ttype)]={
                    'COBRADO': {
                        'NUMBER': cobrado,
                        'MXN': Money(str(cobrado), Currency.MXN).format('es_MX'),
                    },
                    'PENDIENTE': {
                        'NUMBER': pendiente,
                        'MXN': Money(str(pendiente), Currency.MXN).format('es_MX'),
                    },
                    'CANCELADO': {
                        'NUMBER': cancelado,
                        'MXN': Money(str(cancelado), Currency.MXN).format('es_MX'),
                    },
                    'TOTAL': {
                        'NUMBER': total,
                        'MXN': Money(str(total), Currency.MXN).format('es_MX'),
                    },
                }
        return result
    def getTotalDetail(self):
        cobrado = float(self.getTotal(status='COBRADO'))
        pendiente = float(self.getTotal(status='PENDIENTE'))
        cancelado = float(self.getTotal(status='CANCELADO'))
        total = float("{0:.2f}".format(cobrado + pendiente))
        result = {'__ALL':{
            'COBRADO': {
                'NUMBER': cobrado,
                'MXN': Money(str(cobrado), Currency.MXN).format('es_MX'),
            },
            'PENDIENTE': {
                'NUMBER': pendiente,
                'MXN': Money(str(pendiente), Currency.MXN).format('es_MX'),
            },
            'CANCELADO': {
                'NUMBER': cancelado,
                'MXN': Money(str(cancelado), Currency.MXN).format('es_MX'),
            },
            'TOTAL': {
                'NUMBER': total,
                'MXN': Money(str(total), Currency.MXN).format('es_MX'),
            },
        }}
        if len(self.ticketTypes.all()) > 1:
            for ttype in self.ticketTypes.all():
                cobrado = float(self.getTotal(status='COBRADO', ticketType=ttype))
                pendiente = float(self.getTotal(status='PENDIENTE', ticketType=ttype))
                cancelado = float(self.getTotal(status='CANCELADO', ticketType=ttype))
                total = float("{0:.2f}".format(cobrado + pendiente))
                result[str(ttype)]={
                    'COBRADO': {
                        'NUMBER': cobrado,
                        'MXN': Money(str(cobrado), Currency.MXN).format('es_MX'),
                    },
                    'PENDIENTE': {
                        'NUMBER': pendiente,
                        'MXN': Money(str(pendiente), Currency.MXN).format('es_MX'),
                    },
                    'CANCELADO': {
                        'NUMBER': cancelado,
                        'MXN': Money(str(cancelado), Currency.MXN).format('es_MX'),
                    },
                    'TOTAL': {
                        'NUMBER': total,
                        'MXN': Money(str(total), Currency.MXN).format('es_MX'),
                    },
                }
        return result
    def getLens(self):
        cobrado = len(self.getTickets(status='COBRADO'))
        pendiente = len(self.getTickets(status='PENDIENTE'))
        cancelado = len(self.getTickets(status='CANCELADO'))
        total = cobrado + pendiente
        result = {'__ALL':{
            'COBRADO': cobrado,
            'PENDIENTE': pendiente,
            'CANCELADO': cancelado,
            'TOTAL': total,
        }}
        if len(self.ticketTypes.all()) > 1:
            for ttype in self.ticketTypes.all():
                cobrado = len(self.getTickets(status='COBRADO', ticketType=ttype))
                pendiente = len(self.getTickets(status='PENDIENTE', ticketType=ttype))
                cancelado = len(self.getTickets(status='CANCELADO', ticketType=ttype))
                total = cobrado + pendiente
                result[str(ttype)]={
                    'COBRADO': cobrado,
                    'PENDIENTE': pendiente,
                    'CANCELADO': cancelado,
                    'TOTAL': total,
                }
        return result
    def getTicketTypes(self):
        ticketType = ['__ALL']
        for ttype in self.ticketTypes.all():
            ticketType.append(str(ttype))
        return ticketType
    def getProductsDetail(self):
        result = {'__ALL':{
            'COBRADO': CutProductSerializer(self.getCutProducts(status='COBRADO'), many=True).data,
            'PENDIENTE': CutProductSerializer(self.getCutProducts(status='PENDIENTE'), many=True).data,
            'CANCELADO': CutProductSerializer(self.getCutProducts(status='CANCELADO'), many=True).data,
        }}
        if len(self.ticketTypes.all()) > 1:
            for ttype in self.ticketTypes.all():
                result[str(ttype)]={
                    'COBRADO': CutProductSerializer(self.getCutProducts(status='COBRADO', ticketType=ttype), many=True).data,
                    'PENDIENTE': CutProductSerializer(self.getCutProducts(status='PENDIENTE', ticketType=ttype), many=True).data,
                    'CANCELADO': CutProductSerializer(self.getCutProducts(status='CANCELADO', ticketType=ttype), many=True).data,
                }
        return result
    ########
    def getSellpoint(self):
        return self.sellpoint.name
    def getFinal_time(self):
        if self.final_time:
            return self.render_datetime(self.final_time)
        return '-'
    def getColor(self):
        return self.sellpoint.color
class CutSerializer(Basic_Serializer):
    getIvaDetail = serializers.ReadOnlyField()
    getIepsDetail = serializers.ReadOnlyField()
    getSubTotalDetail = serializers.ReadOnlyField()
    getTotalDetail = serializers.ReadOnlyField()
    getLens = serializers.ReadOnlyField()
    getTicketTypes = serializers.ReadOnlyField()
    SellpointDetail = serializers.SerializerMethodField()
    getProductsDetail = serializers.ReadOnlyField()
    class Meta(Basic_Serializer.Meta):
        model = Cut
    def get_SellpointDetail(self, obj):
        return SellpointSerializer(obj.sellpoint, read_only=True).data
class CutIDSerializer(Basic_Serializer):
    class Meta(Basic_Serializer.Meta):
        model = Cut
class CutProduct():
    product = ''
    productName = ''
    quantity = 0
    price = 0
    total = 0
    iva = False
    ieps = True
    offerprice = 0
    offersTotal = 0
    offers = {}
    def __init__(self, product):
        self.product = product.id
        self.productName = product.productName
        self.quantity = float(product.quantity)
        self.price = product.price
        self.offerprice = product.offerprice
        self.total = product.total
        self.iva = product.iva
        self.ieps = product.ieps
        self.offers = {}
    def update(self, product):
        self.quantity += float(product.quantity)
        self.total += product.total
        self.iva += product.iva
        self.ieps += product.ieps
        return self
    def addOffers(self, product):
        if not product.price == product.offerprice:
            self.offersTotal -= (float(product.quantity)*product.price) - (float(product.quantity)*product.offerprice)
        for offer in product.offers.all():
            if not offer.id in self.offers:
                self.offers[offer.id] = {
                    'quantity': 1,
                    'offerName': offer.name
                }
            else:
                self.offers[offer.id]['quantity'] += 1
        return self
    def getPrice(self):
        return {
            'NUMBER': self.price,
            'MXN': Money("{0:.2f}".format(self.price), Currency.MXN).format('es_MX'),
        }
    def getTotal(self):
        return {
            'NUMBER': self.total,
            'MXN': Money("{0:.2f}".format(self.total), Currency.MXN).format('es_MX'),
        }
    def getIva(self):
        return {
            'NUMBER': self.iva,
            'MXN': Money("{0:.2f}".format(self.iva), Currency.MXN).format('es_MX'),
        }
    def getIeps(self):
        return {
            'NUMBER': self.ieps,
            'MXN': Money("{0:.2f}".format(self.ieps), Currency.MXN).format('es_MX'),
        }
    def getOffersTotal(self):
        return {
            'NUMBER': self.offersTotal,
            'MXN': Money("{0:.2f}".format(self.offersTotal), Currency.MXN).format('es_MX'),
        }
class CutProductSerializer(serializers.Serializer):
    product = serializers.IntegerField()
    productName = serializers.CharField(max_length=250)
    quantity = serializers.FloatField()
    getPrice = serializers.ReadOnlyField()
    getTotal = serializers.ReadOnlyField()
    getIva = serializers.ReadOnlyField()
    getIeps = serializers.ReadOnlyField()
    getOffersTotal = serializers.ReadOnlyField()
    offers = serializers.DictField()

#########################################################################################
VARS = {
    'NAME':'Descuento',
    'PLURAL':'Descuentos',
    'MODEL':'Offer',
    'NEW':'NUEVO',
    'NEW_GENDER': 'un nuevo',
    'THIS':'este',
    'APP':APP,
    'LIST': [
        {
            'field': 'name',
            'title': 'Nombre',
        },
        {
            'field': 'getDiscountValueName',
            'title': 'Tipo de condición',
        },
        {
            'field': 'conditionValue',
            'title': 'Valor',
        },
        {
            'field': 'getDiscountTypeName',
            'title': 'Tipo de descuento',
        },
        {
            'field': 'discountValue',
            'title': 'Valor',
        },
        {
            'field': 'getIs_active',
            'title': 'Activo?',
        },
    ],
    'SEARCH': ['name'],
    'FORM': [
        Div(
            Div(
                Div('name'),
                Div('is_active'),
                Div('sellpoints'),
                Div('clients'),
                css_class="col-md-3"
            ),
            Div(
                Div('discountType'),
                Div('discountValue'),
                Div('discountMenus'),
                Div('discountProducts'),
                css_class="col-md-5"
            ),
            Div(
                Div('conditionType'),
                Div('conditionValue'),
                css_class="col-md-4"
            ),
            css_class="form-group m-form__group row"
        ),
    ],
    'FORM_SIZE': ['col-md-12','col-md-12'],
    'FORM_CLASS': 'm-form small_form',
    'SELECTQ': {
        'discountProducts': {
            'model': ['SV', 'Product'],
            'plugin': 'selectmultiple',
            'query': [
                (
                    ('organization__pk', 'self.request.session.get("organization")'),
                ),
            ],
        },
        'discountMenus': {
            'model': ['SV', 'Menu'],
            'plugin': 'selectmultiple',
            'query': [
                (
                    ('organization__pk', 'self.request.session.get("organization")'),
                ),
            ],
        },
        'sellpoints': {
            'model': ['SV', 'Sellpoint'],
            'plugin': 'select2',
            'query': [
                (
                    ('organization__pk', 'self.request.session.get("organization")'),
                    ('active', 'True'),
                    ('is_active', 'True'),
                ),
            ],
        },
        'clients': {
            'model': ['SV', 'Client'],
            'plugin': 'select2',
            'query': [
                (
                    ('organization__pk', 'self.request.session.get("organization")'),
                    ('active', 'True'),
                    ('is_active', 'True'),
                ),
            ],
        },
    },
    'FILTERS': {
        'is_active': {
            'size':'4',
            'label':'Mostrar activos?',
            'list': [
                [1,'Mostrar activos'],
                [0,'Mostrar desactivados'],
            ],
        },
    },
}
class Offer(Model_base):
    DISCOUNNTTYPE = (
        ('productPercent','Porcentaje del producto'),
        ('productValue','Valor fijo del producto'),
        ('totalPercent','Descuento del total del ticket'),
    )
    CONDITIONTYPE = (
        ('productQuantity','Cantidad de productos mínima'),
        ('productValue','Valor fijo del producto'),
    )
    organization = models.ForeignKey('mirari.Organization', related_name='+', on_delete=models.CASCADE)
    sellpoints = models.ManyToManyField('Sellpoint', related_name='+', blank=True, verbose_name='Puntos de venta que afecta', help_text='Si no eliges ninguno afecta a todas')
    clients = models.ManyToManyField('Client', related_name='+', blank=True, verbose_name='Clientes a los que aplica')
    name = models.CharField('Nombre del descuento', max_length=250)
    discountProducts = models.ManyToManyField('Product', verbose_name='Productos a los que afecta el descuento', blank=True, related_name='+',)
    discountMenus = models.ManyToManyField('Menu', verbose_name='Menus a los que afecta el descuento', blank=True, related_name='+',)
    discountType = models.CharField('Forma de aplicar el descuento', choices=DISCOUNNTTYPE, max_length=250, default="productValue")
    discountValue = models.FloatField('Valor del descuento')
    conditionType = models.CharField('Forma de generar el descuento', choices=CONDITIONTYPE, max_length=250, default="productQuantity")
    conditionValue = models.FloatField('Valor del descuento', default=1)
    conditionProducts = models.ManyToManyField('Product', verbose_name='Productos que generan el descuento', blank=True, related_name='+', help_text='Si no eliges ninguno usa los mismos que afecta el descuento')
    conditionMenus = models.ManyToManyField('Menu', verbose_name='Menus que generan el descuento', blank=True, related_name='+', help_text='Si no eliges ninguno usa los mismos que afecta el descuento')
    initialDate = models.DateTimeField('Fecha inicial', null=True, blank=True, help_text="Fecha y hora del inicio")
    finalDate = models.DateTimeField('Fecha final', null=True, blank=True, help_text="Fecha y hora del fin")
    is_active = models.BooleanField('Esta activo?', default=True, help_text='Desactivar Descuento?')
    VARS = VARS
    class Meta(Model_base.Meta):
        verbose_name = VARS['NAME']
        verbose_name_plural = VARS['PLURAL']
        permissions = permissions(VARS)
    def __str__(self):
        return '{0}'.format(self.name)
    def get_sellpoints(self):
        if not self.sellpoints.all():
            return Sellpoint.objects.filter(organization = self.organization)
        return self.sellpoints.all()
    def get_discountProducts(self):
        productsMenu = []
        for menu in self.discountMenus.all():
            for product in menu.get_products():
                if not product in productsMenu:
                    productsMenu.append(product)
        for product in self.discountProducts.all():
            if not product in productsMenu:
                productsMenu.append(product)
        return productsMenu
    def get_conditionProducts(self):
        productsMenu = []
        for menu in self.conditionMenus.all():
            for product in menu.get_products():
                if not product in productsMenu:
                    productsMenu.append(product)
        for product in self.conditionProducts.all():
            if not product in productsMenu:
                productsMenu.append(product)
        if not productsMenu:
            productsMenu = self.get_discountProducts()
        return productsMenu
    def get_sellpointsId(self):
        ids = []
        for sellpoint in self.get_sellpoints():
            ids.append(sellpoint.id)
        return ids
    def get_discountProductsId(self):
        ids = []
        for product in self.get_discountProducts():
            ids.append(product.id)
        return ids
    def get_conditionProductsId(self):
        ids = []
        for product in self.get_conditionProducts():
            ids.append(product.id)
        return ids
    def get_conditionProductsId(self):
        ids = []
        for product in self.get_conditionProducts():
            ids.append(product.id)
        return ids
    def getDiscountTypeName(self):
        return self.get_discountType_display()
    def getDiscountValueName(self):
        return self.get_conditionType_display()
    def getIs_active(self):
        return self.render_boolean(self.is_active)
class OfferSerializer(Basic_Serializer):
    mySellpoints = serializers.ReadOnlyField(source='get_sellpointsId')
    myDiscountProducts = serializers.ReadOnlyField(source='get_discountProductsId')
    myConditionProducts = serializers.ReadOnlyField(source='get_conditionProductsId')
    class Meta(Basic_Serializer.Meta):
        model = Offer
        fields = ('name','mySellpoints','myDiscountProducts','myConditionProducts','initialDate','id','finalDate','clients','discountType','conditionType','discountValue','conditionValue')

########################################################################################
VARS = {
    'NAME':'Perfil cliente',
    'PLURAL':'Perfiles de cliente',
    'MODEL':'ClientProfile',
    'NEW':'NUEVO',
    'NEW_GENDER':'un nuevo',
    'THIS':'este',
    'APP':APP,
    'FORM': ('name',),
    'LIST': [
        {
            'field': 'name',
            'title': 'Nombre',
        },
        {
            'field': 'code',
            'title': 'Código',
        },
    ],
}
class ClientProfile(Model_base):
    organization = models.ForeignKey('mirari.Organization', related_name='+', on_delete=models.CASCADE)
    code = models.CharField('Código del perfil', max_length=250)
    name = models.CharField('Nombre del perfil', max_length=250)
    VARS = VARS
    class Meta(Model_base.Meta):
        verbose_name = VARS['NAME']
        verbose_name_plural = VARS['PLURAL']
        permissions = permissions(VARS)
    def __str__(self):
        return '{0}'.format(self.name)
    def QUERY(self, view):
        return ClientProfile.objects.filter(organization__pk=view.request.session.get('organization'), active=True)

########################################################################################
VARS = {
    'NAME':'Cliente',
    'PLURAL':'Clientes',
    'MODEL':'Client',
    'NEW':'NUEVO',
    'NEW_GENDER':'un nuevo',
    'THIS':'este',
    'APP':APP,
    'FORM': ('name','email','rfc','phone','sellpoints', 'clientProfile'),
    'SELECTQ': {
        'sellpoints': {
            'model': ['SV', 'Sellpoint'],
            'plugin': 'selectmultiple',
            'query': [
                (
                    ('organization__pk', 'self.request.session.get("organization")'),
                    ('active', 'True'),
                ),
            ],
        },
    },
    'LIST': [
        {
            'field': 'name',
            'title': 'Nombre',
        },
        {
            'field': 'uid',
            'title': 'ID',
        },
        {
            'field': 'property_getEmail',
            'title': 'Email',
        },
        {
            'field': 'property_getClientProfile',
            'title': 'Perfil',
        },
        {
            'field': 'property_getBalance',
            'title': 'Balance',
        },
    ],
}
class Client(Model_base):
    uid = models.CharField('Codigo de cliente', max_length=50, blank=True, null=True)
    organization = models.ForeignKey('mirari.Organization', related_name='+', on_delete=models.CASCADE)
    user = models.ForeignKey('mirari.User', related_name='+', on_delete=models.SET_NULL, verbose_name="", blank=True, null=True)
    sellpoints = models.ManyToManyField('Sellpoint', related_name='+', blank=True, verbose_name='Donde factura? ', help_text='Si no eliges ninguno afecta a todas')
    name = models.CharField('Nombre del cliente', max_length=250)
    phone = models.CharField(verbose_name='Telefono', max_length=10, blank=True, null=True, help_text="Teléfono de contacto a 10 digitos")
    rfc = models.CharField(verbose_name='RFC', max_length=15, blank=True, null=True, help_text="RFC de facturación")
    email = models.CharField(verbose_name='Correo', max_length=255, blank=True, null=True, help_text="Email de contacto")
    clientProfile = models.ForeignKey('clientProfile', related_name='+', on_delete=models.SET_NULL, verbose_name="Perfil de cliente", blank=True, null=True)
    is_active = models.BooleanField('Esta activo?', default=True, help_text='Desactivar Cliente?')
    balance = models.FloatField(default=0, blank=True, null=True)
    VARS = VARS
    class Meta(Model_base.Meta):
        verbose_name = VARS['NAME']
        verbose_name_plural = VARS['PLURAL']
        permissions = permissions(VARS)
    def __str__(self):
        return '{0}'.format(self.name)
    def save(self, *args, **kwargs):
        super().save()
        if not self.uid:
            self.uid = str(self.id)
            self.save()
    def QUERY(self, view):
        return Client.objects.filter(organization__pk=view.request.session.get('organization'), active=True)
    def getTickets(self):
        return Ticket.objects.filter(client=self)[0:100]
    def getRFC(self):
        return self.render_if(self.rfc)
    def getEmail(self):
        return self.render_if(self.email)
    def getClientProfile(self):
        if not self.clientProfile:
            return '-'
        return self.clientProfile.name
    def getBalance(self):
        money = Money("{0:.2f}".format(self.balance), Currency.MXN).format('es_MX')
        if self.balance < 0:
            return '<span class"m--font-danger">'+money+'</span>'
        else:
            return '<span class"m--font-success">'+money+'</span>'
    def createFromTicket(self, ticket, sellpoint):
        self.organization = sellpoint.organization
        if ticket['clientName']:
            self.name = ticket['clientName']
        else:
            self.name = ticket['clientID']
        self.uid = ticket['clientID']
        self.phone = ticket.get('phone')
        self.rfc = ticket.get('rfc')
        self.email = ticket.get('email')
        self.clientProfile = ClientProfile.objects.filter(code='PUBLICO GENERAL', organization=sellpoint.organization).first()
        self.save()
        return self
class ClientSerializer(Basic_Serializer):
    clientProfile = serializers.SerializerMethodField()
    class Meta(Basic_Serializer.Meta):
        model = Client
    def get_clientProfile(self, obj):
        return ClientProfileSerializer(obj.clientProfile, read_only=True).data
class ClientProfileSerializer(Basic_Serializer):
    class Meta(Basic_Serializer.Meta):
        model = ClientProfile
class ClientDetailsSerializer(Basic_Serializer):

    clientProfile = serializers.SerializerMethodField()
    tickets = serializers.SerializerMethodField()
    class Meta(Basic_Serializer.Meta):
        model = Client
    def get_clientProfile(self, obj):
        return ClientProfileSerializer(obj.clientProfile, read_only=True).data
    def get_tickets(self, obj):
        return TicketsSerializer(obj.getTickets(), many=True).data


VARS = {
    'NAME':'Grupo puntos de venta',
    'PLURAL':'Grupos de puntos de venta',
    'MODEL':'SellpointGroups',
    'NEW':'NUEVO',
    'NEW_GENDER': 'un nuevo',
    'THIS': 'este',
    'APP':APP,
    'PAGEDetail': 'GetReport__DetailView.pug',
    'LIST': [
        {
            'field': 'name',
            'title': 'Nombre',
            'url': 'url_detail',
            'sorteable': True,
            'serchable': True,
        },
    ],
    'SELECTQ': {
        'sellpoints': {
            'plugin': 'selectmultiple',
        },
    },
    'FORM': ('name','sellpoints'),
}
class SellpointGroups(Model_base):
    organization = models.ForeignKey('mirari.Organization', related_name='+', on_delete=models.CASCADE)
    name = models.CharField('Nombre del grupo', max_length=250)
    sellpoints = models.ManyToManyField('Sellpoint', verbose_name='Puntos de venta', blank=True, related_name='+',)
    VARS = VARS
    class Meta(Model_base.Meta):
        verbose_name = VARS['NAME']
        verbose_name_plural = VARS['PLURAL']
        permissions = permissions(VARS)
    def __str__(self):
        return '{0}'.format(self.name)