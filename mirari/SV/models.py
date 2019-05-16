# -*- coding: utf-8 -*-
from mirari.mirari.models import *
from .vars import *

########################################################################################
VARS = {
    'NAME':'Punto de venta',
    'PLURAL':'Puntos de venta',
    'MODEL':'Sellpoint',
    'NEW':'NUEVO',
    'NEW_GENDER': 'un nuevo',
    'THIS': 'este',
    'APP':APP,
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
        },
        {
            'field': 'get_have_casher',
            'title': 'COBRA VENDEDOR?',
        },
        {
            'field': 'number_tickets',
            'title': '# Tickets',
        },
        {
            'field': 'getSerialNumber',
            'title': 'FOLIO',
        },
        {
            'field': 'get_color',
            'title': 'COLOR',
        },
        {
            'field': 'printer',
            'title': 'IMPRESORA',
        },
    ],
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
    },
    'FORM': ('name','have_casher','color','vendors','cashers','orders', 'supervisors','is_active','printer','barcode','number_tickets','haveExpenses','header_line_black_1','header_line_black_2','header_line_1','header_line_2','footer_line_1'),
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
    VARS = VARS
    class Meta(Model_base.Meta):
        verbose_name = VARS['NAME']
        verbose_name_plural = VARS['PLURAL']
        permissions = permissions(VARS)
    def __str__(self):
        return '{0}'.format(self.name)
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
    def get_have_casher(self):
        return self.render_boolean(not self.have_casher)
    def get_haveExpenses(self):
        return self.render_boolean(not self.haveExpenses)
    def get_color(self):
        return self.render_color(self.color)
    def get_serial(self):
        return self.serial.get_serial()
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
    def save(self, *args, **kwargs):
        self.name = self.name.upper()
        super().save()
        if not self.serial:
            content_type = ContentType.objects.get(app_label=APP, model=self.VARS['MODEL'].lower())
            serial = Serial.objects.create(organization=self.organization, name=self.name.lower(), content_type=content_type)
            self.serial = serial
            self.save()

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
            'field': 'name',
            'title': 'Nombre',
        },
        {
            'field': 'property_get_parent',
            'title': 'Depende de',
        },
        {
            'field': 'property_get_color',
            'title': 'Color',
        },
        {
            'field': 'property_get_is_active',
            'title': 'Activo?',
        },
    ],
    'SEARCH': ['name'],
    'SORTEABLE': ['name'],
    'FORM': ('name','color','parent','is_active'),
}
class Menu(Model_base, MPTTModel):
    organization = models.ForeignKey('mirari.Organization', on_delete=models.CASCADE)
    name = models.CharField('Nombre del menú', max_length=30)
    color = models.CharField('Color del menú', default='#3d3b56', max_length=100)
    is_active = models.BooleanField('Esta activo?', default=True, help_text='Desactiva todos los productos de un menú')
    parent = TreeForeignKey('self', null=True, blank=True, related_name='+', db_index=True, on_delete=models.PROTECT, verbose_name='Depende de?', help_text='Elige otro menú solo si este menú depende de otro')
    nivel = models.PositiveIntegerField(default=1)
    VARS = VARS
    class Meta(Model_base.Meta):
        verbose_name = VARS['NAME']
        verbose_name_plural = VARS['PLURAL']
        permissions = permissions(VARS)
    def __str__(self):
        return '{0}'.format(self.name)
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

########################################################################################
VARS = {
    'NAME':'Producto',
    'PLURAL':'Productos',
    'MODEL':'Product',
    'NEW':'NUEVO',
    'NEW_GENDER':'un nuevo',
    'THIS':'este',
    'APP':APP,
    'QUERY':{
        'query': [
            (
                ('menu__organization__in','Organization.objects.filter(pk=self.request.session.get("organization")).all()'),
                ('active','True'),
            )
        ],
    },
    'LIST': [
        {
            'field': 'code',
            'title': 'Productos en sucursales',
            'template': '{{property_get_productattributes}}',
        },
        {
            'field': 'name',
            'title': 'Información de producto',
            'template': 
                """
                    <span>
                        <strong class="mr-2">{{name}}</strong>{{property_get_is_active}}<br /> 
                        {{property_get_menu}} <br />
                        <small>
                            {{property_get_code}}<br /> 
                            {{property_get_units}}
                        </small>
                    </span>
                """,
        },
    ],
    'SEARCH': ['name'],
    'SORTEABLE': ['name'],
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
    'SERIALIZER': ['get_code','get_units','get_is_active','get_productattributes','get_menu','get_sellpoint'],
    'HIDE_CHECKBOX_LIST': True,
    'SELECTQ': {
        #'code': {
            #'model': ['mirari', 'ProductsServicesSAT'],
            #'query': 'NONE',
            #'plugin': 'select2',
            #'sercheable': ['code__icontains', 'name__icontains'],
            #'limits': 50,
            #'placeholder': 'Elige un producto o código del producto',
        #},
        #'units': {
            #'model': ['mirari', 'UnitsCodesSat'],
            #'query': 'NONE',
            #'plugin': 'select2',
            #'sercheable': ['code__icontains', 'name__icontains'],
            #'limits': 50,
            #'placeholder': 'Elige una unidad o código de la unidad',
        #},
        'sellpoints': {
            'plugin': 'selectmultiple',
        },
        'menu': {
            'plugin': 'selectmultiple',
        },
    },
    'FORM': ('name','sellpoints','menu','is_active','price','iva','ieps','bar_code','is_dynamic','is_favorite'),

}
class Product(Model_base):
    organization = models.ForeignKey('mirari.Organization', on_delete=models.CASCADE)
    name = models.CharField('Nombre del producto', max_length=250)
    code = models.ForeignKey('mirari.ProductsServicesSAT', blank=True, null=True,on_delete=models.PROTECT, verbose_name="Código de producto en el SAT", help_text='Código de registro ante el SAT', related_name='+')
    units = models.ForeignKey('mirari.UnitsCodesSat', blank=True, null=True,on_delete=models.PROTECT, verbose_name="Código de unidad en el SAT", help_text="Unidad de medida para este producto", related_name='+')
    sellpoints = models.ManyToManyField('Sellpoint', related_name='+', verbose_name="", help_text="Se vende en estas sucursales")
    menu = models.ManyToManyField('Menu', related_name='+', verbose_name="", help_text="Elige el o los menus donde se vende este producto")
    is_active = models.BooleanField('Esta activo?', default=True, help_text='Desactivar producto?')
    price = models.FloatField('Precio en esta sucursal ', default=0, help_text='Graba IVA? (sugerido)')
    iva = models.BooleanField('I.V.A. ', default=True, help_text='Graba IVA? (sugerido)')
    ieps = models.BooleanField('IEPS. ', default=True, help_text='Graba IEPS? (sugerido)')
    bar_code = models.CharField('Código de Barras ', max_length=250, blank=True, null=True, help_text='(sugerido)')
    is_dynamic = models.BooleanField('Precio dinámico ', default=False, help_text='Este producto tiene precio variable? (sugerido)')
    is_favorite = models.BooleanField('Es favorito? ', default=False, help_text='Se muestra siempre este producto? (sugerido)')
    VARS = VARS
    class Meta(Model_base.Meta):
        verbose_name = VARS['NAME']
        verbose_name_plural = VARS['PLURAL']
        permissions = permissions(VARS)
    def __str__(self):
        return '{0}'.format(self.name)
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
    def get_menu(self):
        string_menu = ''
        for menu in self.menu.all():
            string_menu += mark_safe(self.render_boolean_del('<small class="m--font-'+menu.render_string_color(menu.is_active)+'" style="color:'+menu.color+'!important">'+menu.name+'</small>', menu.is_active))
            string_menu += ', '
        return string_menu[0:len(string_menu)-2]
    def get_productattributes(self):
        string = ''
        for sellpoint in self.sellpoints.all():
            productattributes = ProductAttributes.objects.get(product=self,sellpoint=sellpoint)
            string += """
                    <a href="{9}">
                        <div class="kt-portlet mb-1" style="border: 1px solid {10};">
                            <div class="kt-portlet__body py-2 px-3">
                                    {8}
                                <h5 class="text-dark">{1}</h5>
                                <div class="kt-section__content kt-section__content--solid">
                                    {2} {3} {7} {5} {6}
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
                productattributes.url_update(),
                productattributes.sellpoint.color,
            )
        if not string:
            string = '<strong>No hay puntos de venta asociados</strong>'
        return mark_safe(string)
def sellpoints_changed(sender, **kwargs):
    action = kwargs.pop('action', None)
    instance = kwargs.pop('instance', None)
    if action == 'post_add':
        for sellpoint in instance.sellpoints.all():
            productAttributes = ProductAttributes.objects.get_or_create(product=instance,sellpoint=sellpoint)[0]
            productAttributes.active=True
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
    'FORM': ('alias','price','bar_code','iva','ieps','is_dynamic','is_favorite','is_active',),
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
    iva = models.BooleanField('I.V.A.', default=True, help_text="Graba IVA?")
    ieps = models.BooleanField('IEPS.', default=True, help_text="Graba IEPS?")
    bar_code = models.CharField('Código de Barras', max_length=250, blank=True, null=True,)
    is_dynamic = models.BooleanField('Precio dinámico', default=False, help_text='Este producto tiene precio variable?')
    is_favorite = models.BooleanField('Es favorito?', default=False, help_text='Se muestra siempre este producto?')
    is_active = models.BooleanField('Esta activo?', default=True, help_text='Desactivar producto?')
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
        if self.alias:
            return self.alias
        return self.product.name
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

########################################################################################
VARS = {
    'NAME':'Ticket',
    'PLURAL':'Tickets',
    'MODEL':'Ticket',
    'NEW':'NUEVO',
    'NEW_GENDER': 'un nuevo',
    'THIS':'este',
    'APP':APP,
    'EXCLUDE_PERMISSIONS': ['create','update'],
    'SERIALIZER': ('getColor','getSellpoint','getIepsMoney','getIvaMoney','getTotalMoney','getOnAccountMoney',),
    'LIST': [
        {
            'field': 'barcode',
            'title': 'Folio',
            'template': 
            """
                <a href="{{property_url_detail}}" style="text-decoration:none;color:{{property_getColor}}!important;">
                    <strong>
                        {{barcode}}
                    </strong>
                </a>
            """,
        },
        {
            'field': 'property_getSellpoint',
            'title': 'Punto de Venta',
            'template': 
            """
                <a href="{{property_url_detail}}" style="text-decoration:none;color:{{property_getColor}}!important;">
                    <strong>
                        {{property_getSellpoint}}
                    </strong>
                </a>
            """,
        },
        {
            'field': 'ticketType',
            'title': 'Tipo',
            'template': 
            """
                <a href="{{property_url_detail}}" style="text-decoration:none;color:{{property_getColor}}!important;">
                    <strong>
                        {{ticketType}}
                    </strong>
                </a>
            """,
        },
        {
            'field': 'property_getIepsMoney',
            'title': 'IEPS',
            'template': 
            """
                <a href="{{property_url_detail}}" style="text-decoration:none;color:{{property_getColor}}!important;">
                    <strong>
                        {{property_getIepsMoney}}
                    </strong>
                </a>
            """,
        },
        {
            'field': 'property_getIvaMoney',
            'title': 'IVA',
            'template': 
            """
                <a href="{{property_url_detail}}" style="text-decoration:none;color:{{property_getColor}}!important;">
                    <strong>
                        {{property_getIvaMoney}}
                    </strong>
                </a>
            """,
        },
        {
            'field': 'property_getOnAccountMoney',
            'title': 'A CUENTA',
            'template': 
            """
                <a href="{{property_url_detail}}" style="text-decoration:none;color:{{property_getColor}}!important;">
                    <strong>
                        {{property_getOnAccountMoney}}
                    </strong>
                </a>
            """,
        },
        {
            'field': 'property_getTotalMoney',
            'title': 'TOTAL',
            'template': 
            """
                <a href="{{property_url_detail}}" style="text-decoration:none;color:{{property_getColor}}!important;">
                    <strong>
                        {{property_getTotalMoney}}
                    </strong>
                </a>
            """,
        },
        {
            'field': 'status',
            'title': 'ESTATUS',
            'template': 
            """
                <a href="{{property_url_detail}}" style="text-decoration:none;color:{{property_getColor}}!important;">
                    <strong>
                        {{status}}
                    </strong>
                </a>
            """,
        },
    ],
    'HIDE_CHECKBOX_LIST': True,
    'HIDE_BUTTONS_LIST': True,
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
                )
            ],
        }
    },
    #'HTMLPageList': 'sv__Ticket__ListView.html',
}
class Ticket(Model_base):
    STATUS_TICKET = (
        ('COBRADO','COBRADO'),
        ('PENDIENTE','PENDIENTE'),
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
    VARS = VARS
    class Meta(Model_base.Meta):
        verbose_name = VARS['NAME']
        verbose_name_plural = VARS['PLURAL']
        permissions = permissions(VARS)
    def __str__(self):
        return '{0} | {1}'.format(self.sellpoint, self.barcode)
    def QUERY(self, view):
        return Ticket.objects.filter(sellpoint__organization__pk=view.request.session.get('organization'), active=True)
    def my_organization(self):
        return self.sellpoint.my_organization()
    def new(self, ticket):
        self.sellpoint = Sellpoint.objects.get(id = ticket['sellpoint']['id'])
        lastTicket = Ticket.objects.filter(key=ticket['key'],total=ticket['total'],sellpoint=self.sellpoint).first()
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
        for product in ticket['products']:
            TicketProducts().addTicket(self, product)
        return self
    def getLenOffers(self):
        offers = []
        for ticketProduct in TicketProducts.objects.filter(ticket = self, offers = None):
            if not ticketProduct.offers in offers:
                offers.append(ticketProduct.offers)
        return len(offers)
    def scanner(self):
        if (self.status == 'PENDIENTE'):
            self.status = 'COBRADO'
            self.save()
        return self
    def getCutSerial(self):
        return self.cut.serial
    def getSellpoint(self):
        return self.sellpoint.name
    def getOnAccount(self):
        return "{0:.2f}".format(self.onAccount)
    def getTotal(self):
        return "{0:.2f}".format(self.total)
    def getIva(self):
        return "{0:.2f}".format(self.iva)
    def getIeps(self):
        return "{0:.2f}".format(self.ieps)
    def getOnAccountMoney(self):
        return Money(self.getOnAccount(), Currency.MXN).format('es_MX')
    def getTotalMoney(self):
        return Money(self.getTotal(), Currency.MXN).format('es_MX')
    def getIvaMoney(self):
        return Money(self.getIva(), Currency.MXN).format('es_MX')
    def getIepsMoney(self):
        return Money(self.getIeps(), Currency.MXN).format('es_MX')
    def getProducts(self):
        return TicketProducts.objects.filter(ticket=self)
    def getTicketType(self):
        return ", ".join(o.name for o in self.ticketType.all())
    def getColor(self):
        return self.sellpoint.color

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
        for offer in product['offers']:
            self.offers.add(Offer.objects.get(id=offer['id']))
        return self

########################################################################################
class CutProductSerializer(serializers.Serializer):
    product = serializers.IntegerField()
    productName = serializers.CharField(max_length=250)
    quantity = serializers.IntegerField()
    price = serializers.FloatField()
    total = serializers.FloatField()
    iva = serializers.FloatField()
    ieps = serializers.FloatField()
    offerprice = serializers.FloatField()
    offersTotal = serializers.FloatField()
    offers = serializers.DictField()
    getQuantity = serializers.SerializerMethodField()
    getPrice = serializers.SerializerMethodField()
    getTotalMoney = serializers.SerializerMethodField()
    getIvaMoney = serializers.SerializerMethodField()
    getIepsMoney = serializers.SerializerMethodField()
    def get_getQuantity(self, obj):
        return obj.getQuantity()
    def get_getPrice(self, obj):
        return obj.getPrice()
    def get_getTotalMoney(self, obj):
        return obj.getTotalMoney()
    def get_getIvaMoney(self, obj):
        return obj.getIvaMoney()
    def get_getIepsMoney(self, obj):
        return obj.getIepsMoney()
class CutOffer():
    quantity = 0
    offerName = ''
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
    def getQuantity(self):
        return str(int(self.quantity))
    def getPrice(self):
        return Money("{0:.2f}".format(self.price), Currency.MXN).format('es_MX')
    def getTotalMoney(self):
        return Money("{0:.2f}".format(self.total), Currency.MXN).format('es_MX')
    def getIvaMoney(self):
        return Money("{0:.2f}".format(self.iva), Currency.MXN).format('es_MX')
    def getIepsMoney(self):
        return Money("{0:.2f}".format(self.ieps), Currency.MXN).format('es_MX')
VARS = {
    'NAME':'Corte',
    'PLURAL':'Cortes',
    'MODEL':'Cut',
    'NEW':'NUEVO',
    'NEW_GENDER': 'un nuevo',
    'THIS':'este',
    'APP':APP,
    'EXCLUDE_PERMISSIONS': ['create','update','delete'],
    'SERIALIZER': ('getColor','getSellpoint','getIvaMoney','getSubtotalMoney','getIepsMoney','getLenFaltante','getLenTickets','getTotalFaltanteMoney'),
    'LIST': [
        {
            'field': 'serial',
            'title': 'Folio',
            'width': 100,
            'template': 
            """
                <a href="{{property_url_detail}}" style="text-decoration:none;color:{{property_getColor}}!important;">
                    <strong>
                        {{serial}}
                    </strong>
                </a>
            """,
        },
        {
            'field': 'property_getFinal_time',
            'title': 'Fecha/Hora',
            'template': 
            """
                <a href="{{property_url_detail}}" style="text-decoration:none;color:{{property_getColor}}!important;">
                    <small>{{property_getFinal_time}}</small>
                    <br />
                    <small>{{property_getSellpoint}}</small>
                </a>
            """,
        },
        {
            'field': 'property_getIvaMoney',
            'title': 'IMPUESTOS',
            'template': 
            """
                <a href="{{property_url_detail}}" style="text-decoration:none;color:{{property_getColor}}!important;">
                    IVA: {{property_getIvaMoney}} <br />
                    IEPS: {{property_getIepsMoney}} <br />
                    Subtotal: {{property_getSubtotalMoney}} <br />
                </a>
            """,
        },
        {
            'field': 'property_getFaltanteMoney',
            'title': 'Faltates',
            'template': 
            """
                <a href="{{property_url_detail}}" style="text-decoration:none;color:{{property_getColor}}!important;">
                    <strong>{{property_getFaltanteMoney}}</strong> <br /> 
                    #{{property_getLenFaltante}} tickets
                </a>
            """,
        },
        {
            'field': 'property_getTotalMoney',
            'title': 'Totales',
            'template': 
            """
                <a href="{{property_url_detail}}" style="text-decoration:none;color:{{property_getColor}}!important;">
                    <strong>{{property_getTotalMoney}}</strong> <br />
                    #{{property_getLenTickets}} clientes <br />
                    <small>+Faltante:</small> {{property_getTotalFaltanteMoney}}<br />
                </a>
            """,
        },
        {
            'field': 'id',
            'title': '',
            'template': 
            """
                <a href="{{property_url_detail}}" style="text-decoration:none;">
                    <strong>
                        <i class="fa fa-search"></i> DETALLES
                    </strong>
                </a>
            """,
        },
    ],
    'FILTERS': {
            'sellpoint': {
            'size':'4',
            'label':'Punto de venta',
            'model':['SV','Sellpoint'],
            'query':[
                (
                    ('organization','Organization.objects.get(pk=self.request.session.get("organization"))'),
                    ('active','True'),
                )
            ],
        }
    },
}
class Cut(Model_base):
    sellpoint = models.ForeignKey('Sellpoint', null=True, blank=True, on_delete=models.SET_NULL)
    initial_time = models.DateTimeField(auto_now_add=True)
    final_time = models.DateTimeField(null=True, blank=True,)
    rasurado = models.PositiveIntegerField(default=100)
    serial = models.IntegerField(default=1)
    show = models.BooleanField(default=True)
    ticketTypes = TaggableManager()
    VARS = VARS
    class Meta(Model_base.Meta):
        verbose_name = VARS['NAME']
        verbose_name_plural = VARS['PLURAL']
        permissions = permissions(VARS)
    def __str__(self):
        return '{0}'.format(self.id)
    def QUERY(self, view):
        return Cut.objects.filter(sellpoint__organization__pk=view.request.session.get('organization'), active=True).order_by('-final_time')
    def my_organization(self):
        return self.sellpoint.my_organization()
    def url_detail(self):
        return reverse('SV:Cut__DetailView', kwargs={'app': self.VARS['APP'], 'model': self.VARS['MODEL'], 'pk': self.pk})
    def new(self, sellpoint):
        self.sellpoint = sellpoint
        cut = Cut.objects.filter(sellpoint = self.sellpoint).first()
        if cut:
            self.serial = cut.serial + 1
        self.save()
        return self
    def makeCut(self):
        if self.getLenTickets():
            self.final_time = datetime.datetime.now()
        self.save()
        return self
    def cutTypes(self):
        ticketType = ['all']
        for ticket in self.getTickets(status='all', ticketType='all'):
            if not ticket.ticketType in ticketType:
                ticketType.append(ticket.ticketType)
                self.ticketTypes.add(ticket.ticketType)
        return self.ticketTypes
    def getTickets(self, status='all', ticketType='all', rasurado=False):
        if status=='all':
            tickets = Ticket.objects.filter(cut=self)
        else:
            tickets = Ticket.objects.filter(cut=self, status=status)
        if not ticketType == 'all':
            tickets = tickets.filter(ticketType = ticketType)
        if rasurado:
            tickets = tickets.exclude(rasurado = True)
        return tickets.exclude(rasurado = True)
    def getLenTickets(self, status='all', ticketType='all'):
        return len(self.getTickets(status=status, ticketType=ticketType))
    def getLenFaltante(self, status='PENDIENTE', ticketType='all'):
        return len(self.getTickets(status=status, ticketType=ticketType))
    def getCutProducts(self, status='all', ticketType='all'):
        products = []
        expenses = ['GASTO',0,0]
        for ticket in self.getTickets(status=status, ticketType=ticketType):
            if ticket.ticketType == 'GASTO':
                expenses[1] += 1
                expenses[2] += ticket.onAccount
            for product in ticket.getProducts():
                cutProduct = CutProduct(product)
                exist = False    
                for arrayCutProduct in products:
                    if arrayCutProduct.productName == product.productName and arrayCutProduct.price == product.price:
                        cutProduct = arrayCutProduct.update(product)
                        exist = True
                        break
                cutProduct.addOffers(product)
                if not exist:
                    products.append(cutProduct)
        if expenses[1]:
            product = TicketProducts()
            product.productName = expenses[0]
            product.quantity = expenses[1]
            product.total = expenses[2]
            cutProduct = CutProduct(product)
            products.append(cutProduct)
        return  sorted(products, key=lambda x: x.quantity, reverse=True)
    def getTotal(self, status='COBRADO', ticketType='all'):
        total = 0
        for ticket in self.getTickets(status=status, ticketType=ticketType):
            ticketTotal = ticket.total
            if ticket.onAccount > 0:
                ticketTotal = ticket.onAccount
            if ticket.ticketType == 'DEVOLUCION' or ticket.ticketType == 'GASTO':
                ticketTotal = ticketTotal * -1
            total += ticketTotal
        return "{0:.2f}".format(total)
    def getTotalMoney(self, status='COBRADO', ticketType='all'):
        return Money(self.getTotal(status=status, ticketType=ticketType), Currency.MXN).format('es_MX')
    def getIeps(self, status='COBRADO', ticketType='all'):
        total = 0
        for ticket in self.getTickets(status=status, ticketType=ticketType):
            total += ticket.ieps
        return "{0:.2f}".format(total)
    def getIva(self, status='COBRADO', ticketType='all'):
        total = 0
        for ticket in self.getTickets(status=status, ticketType=ticketType):
            total += ticket.iva
        return "{0:.2f}".format(total)
    def getSubtotal(self, status='COBRADO', ticketType='all'):
        total = 0
        for ticket in self.getTickets(status=status, ticketType=ticketType):
            total += ticket.total - ticket.ieps - ticket.iva
        return "{0:.2f}".format(total)
    def getFaltante(self, status='PENDIENTE', ticketType='all'):
        total = 0
        for ticket in self.getTickets(status=status, ticketType=ticketType):
            total += ticket.total
        return "{0:.2f}".format(total)
    def getIepsMoney(self, status='COBRADO', ticketType='all'):
        return Money(self.getIeps(status=status, ticketType=ticketType), Currency.MXN).format('es_MX')
    def getIvaMoney(self, status='COBRADO', ticketType='all'):
        return Money(self.getIva(status=status, ticketType=ticketType), Currency.MXN).format('es_MX')
    def getSubtotalMoney(self, status='COBRADO', ticketType='all'):
        return Money(self.getSubtotal(status=status, ticketType=ticketType), Currency.MXN).format('es_MX')
    def getFaltanteMoney(self, status='PENDIENTE', ticketType='all'):
        return Money(self.getFaltante(status=status, ticketType=ticketType), Currency.MXN).format('es_MX')
    def getTotalFaltanteMoney(self):
        return Money("{0:.2f}".format( float(self.getTotal()) + float(self.getFaltante())), Currency.MXN).format('es_MX')
    def getOffersLen(self, status='COBRADO', ticketType='all'):
        total = 0
        for ticket in self.getTickets(status=status, ticketType=ticketType):
            total += ticket.getLenOffers()
        return total
    #def makeRasurado(self, value):
        #total = 0
        #self.getTickets(status='100').update(rasurado=False)
        #for ticket in self.getTickets(status='100'):
            #total += ticket.total
        #finaltotal = total * value / 100
        #for ticket in self.getTickets(status='100').exclude(invoiced=True).order_by('-total'):
            #if total <= finaltotal:
                #break
            #else:
                #ticket.rasurado = True
                #ticket.save()
                #total -= ticket.total
        #self.rasurado = value
        #self.save()
        #return True
    def getSellpoint(self):
        return self.sellpoint.name
    def getFinal_time(self):
        if self.final_time:
            return self.render_datetime(self.final_time)
        return '-'
    def getColor(self):
        return self.sellpoint.color
    def TotalDetail(self):
        result = {'all':(
            self.getTotal(),
            self.getTotalMoney(),
            self.getTotal(status='PENDIENTE'),
            self.getTotalMoney(status='PENDIENTE'),
        )}
        for ttype in self.ticketTypes.all():
            result[str(ttype)]=(
                self.getTotal(ticketType=ttype), 
                self.getTotalMoney(ticketType=ttype),
                self.getTotal(status='PENDIENTE',ticketType=ttype),
                self.getTotalMoney(status='PENDIENTE',ticketType=ttype),
            )
        return result
    def IvaDetail(self):
        result = {'all':(
            self.getIva(),
            self.getIvaMoney(),
            self.getIva(status='PENDIENTE'),
            self.getIvaMoney(status='PENDIENTE'),
        )}
        for ttype in self.ticketTypes.all():
            result[str(ttype)]=(
                self.getIva(ticketType=ttype), 
                self.getIvaMoney(ticketType=ttype),
                self.getIva(status='PENDIENTE',ticketType=ttype),
                self.getIvaMoney(status='PENDIENTE',ticketType=ttype),
            )
        return result
    def IepsDetail(self):
        result = {'all':(
            self.getIeps(),
            self.getIepsMoney(),
            self.getIeps(status='PENDIENTE'),
            self.getIepsMoney(status='PENDIENTE'),
        )}
        for ttype in self.ticketTypes.all():
            result[str(ttype)]=(
                self.getIeps(ticketType=ttype), 
                self.getIepsMoney(ticketType=ttype),
                self.getIeps(status='PENDIENTE',ticketType=ttype),
                self.getIepsMoney(status='PENDIENTE',ticketType=ttype),
            )
        return result
    def SubTotalDetail(self):
        result = {'all':(
            self.getSubtotal(),
            self.getSubtotalMoney(),
            self.getSubtotal(status='PENDIENTE'),
            self.getSubtotalMoney(status='PENDIENTE'),
        )}
        for ttype in self.ticketTypes.all():
            result[str(ttype)]=(
                self.getSubtotal(ticketType=ttype), 
                self.getSubtotalMoney(ticketType=ttype),
                self.getSubtotal(status='PENDIENTE',ticketType=ttype),
                self.getSubtotalMoney(status='PENDIENTE',ticketType=ttype),
            )
        return result
    def ProductsDetail(self):
        result = {'all':CutProductSerializer(self.getCutProducts(), many=True, read_only=True).data}
        for ttype in self.ticketTypes.all():
            result[str(ttype)] = CutProductSerializer(self.getCutProducts(ticketType=ttype), many=True, read_only=True).data
        return result

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
            'field': 'property_getDiscountValueName',
            'title': 'Tipo de condición',
        },
        {
            'field': 'conditionValue',
            'title': 'Valor',
        },
        {
            'field': 'property_getDiscountTypeName',
            'title': 'Tipo de descuento',
        },
        {
            'field': 'discountValue',
            'title': 'Valor',
        },
        {
            'field': 'property_getIs_active',
            'title': 'Activo?',
        },
    ],
    'SEARCH': ['name'],
    'FORM': [
        Div(
            Div(
                Div('name'),
                Div('is_active'),
                #Div('initialDate'),
                #Div('finalDate'),
                #Div('sellpoints'),
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
                #Div('conditionMenus'),
                #Div('conditionProducts'),
                css_class="col-md-4"
            ),
            css_class="form-group m-form__group row"
        ),
    ],
    'FORM_SIZE': ('col-xl-12','col-xl-12'),
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
        #'conditionProducts': {
            #'model': ['SV', 'Product'],
            #'plugin': 'selectmultiple',
            #'query': [
                #(
                    #('organization__pk', 'self.request.session.get("organization")'),
                #),
            #],
        #},
        #'conditionMenus': {
            #'model': ['SV', 'Menu'],
            #'plugin': 'selectmultiple',
            #'query': [
                #(
                    #('organization__pk', 'self.request.session.get("organization")'),
                #),
            #],
        #},
        #'sellpoints': {
            #'model': ['SV', 'Sellpoint'],
            #'plugin': 'select2',
            #'query': [
                #(
                    #('organization__pk', 'self.request.session.get("organization")'),
                #),
            #],
        #},
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
        return self.discountType
    def getDiscountValueName(self):
        return self.conditionType
    def getIs_active(self):
        return self.render_boolean(self.is_active)

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

