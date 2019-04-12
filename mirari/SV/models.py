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
            'url': 'property_url_update',
        },
        {
            'field': 'property_get_have_casher',
            'title': 'COBRA VENDEDOR?',
        },
        {
            'field': 'number_tickets',
            'title': '# Tickets',
        },
        {
            'field': 'property_getSerialNumber',
            'title': 'FOLIO',
        },
        {
            'field': 'property_get_color',
            'title': 'COLOR',
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
    },
    'SEARCH': ['name'],
    'SORTEABLE': ['name'],
    'EXCLUDE_FORM': ['serial'],
    'FORM': ('name','have_casher','color','vendors','cashers','orders','is_active','number_tickets','printer','header_line_black_1','header_line_black_2','header_line_1','header_line_2','footer_line_1'),
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
    orders = models.ManyToManyField('mirari.User', verbose_name='Pedidos', blank=True, related_name='+',)
    printer = models.CharField('Impresora ID', max_length=80, blank=True, null=True)
    VARS = VARS
    class Meta(Model_base.Meta):
        verbose_name = VARS['NAME']
        verbose_name_plural = VARS['PLURAL']
        permissions = permissions(VARS)
    def __str__(self):
        return '{0}'.format(self.name)
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
    def get_color(self):
        return self.render_color(self.color)
    def get_serial(self):
        return self.serial.get_serial()
    def getCut(self):
        #return Cut.objects.get(id=118) #### Enviar corte
        cut = Cut.objects.filter(sellpoint=self, final_time__isnull=True).first()
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
    'SELECTQ': {
        'parent': {
            'plugin': 'select2',
        },
    },
    'FORM': ('name','color','parent','is_active'),
}
class Menu(Model_base, MPTTModel):
    organization = models.ForeignKey('mirari.Organization', on_delete=models.CASCADE)
    name = models.CharField('Nombre del menú', max_length=30)
    color = models.CharField('Color del menú', default='#3d3b56', max_length=100)
    is_active = models.BooleanField('Esta activo?', default=True, help_text='Desactiva todos los productos de un menú')
    parent = TreeForeignKey('self', null=True, blank=True, related_name='+', db_index=True, on_delete=models.PROTECT, verbose_name='', help_text='Elige otro menú solo si este menú depende de otro')
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
    'FORM': ('name','sellpoints','menu','is_active'),
}
class Product(Model_base):
    organization = models.ForeignKey('mirari.Organization', on_delete=models.CASCADE)
    name = models.CharField('Nombre del producto', max_length=250)
    code = models.ForeignKey('mirari.ProductsServicesSAT', blank=True, null=True,on_delete=models.PROTECT, verbose_name="Código de producto en el SAT", help_text='Código de registro ante el SAT', related_name='+')
    units = models.ForeignKey('mirari.UnitsCodesSat', blank=True, null=True,on_delete=models.PROTECT, verbose_name="Código de unidad en el SAT", help_text="Unidad de medida para este producto", related_name='+')
    sellpoints = models.ManyToManyField('Sellpoint', related_name='+', verbose_name="", help_text="Se vende en estas sucursales")
    menu = models.ManyToManyField('Menu', related_name='+', verbose_name="", help_text="Elige el o los menus donde se vende este producto")
    is_active = models.BooleanField('Esta activo?', default=True, help_text='Desactivar producto?')
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
                    <div class="m-portlet m-portlet--full-height" style="border-style:solid;border-width:1px;color:#e6e6e6;margin-bottom: .5rem;">
                        <div class="m-portlet__body m--padding-5 m--padding-right-10 m--padding-left-10 ">
                            <div class="m-widget3">
                                <div class="m-widget3__item">
                                    <div class="m-widget3__header">
                                        <div class="m-widget3__info" style="padding-left: 0rem;">
                                            <span class="m-widget3__username">{8}</span>
                                            <span class="m-widget3__time m--margin-left-5">
                                                {1}
                                            </span>
                                        </div>
                                        <a href="{9}" class="btn btn-outline-brand m-btn m-btn--icon m-btn--icon-only m-btn--custom m-btn--pill btn-sm m--margin-right-25 m--margin-top-5 m--pull-right" title="Editar" style="width: 20px;height: 20px;">
                                            <i class="la la-edit" style="font-size:12px;"></i>
                                        </a>
                                    </div>
                                    <div class="m-widget3__body mt-1">
                                        <p class="m-widget3__text" style="font-size:11px;">
                                            {2} {3} {7} {5} {6}
                                        </p>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>
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
        return mark_safe('<span class="m-badge m-badge--wide m-badge--rounded m-badge--'+self.render_string_color(self.iva)+' m-badge--wide">I.V.A.</span>')
    def get_badge_ieps(self):
        return mark_safe('<span class="m-badge m-badge--wide m-badge--rounded m-badge--'+self.render_string_color(self.ieps)+' m-badge--wide">IEPS</span>')
    def get_badge_is_dynamic(self):
        return mark_safe('<span class="m-badge m-badge--wide m-badge--rounded m-badge--'+self.render_string_color(self.is_dynamic)+' m-badge--wide">Dinámico</span>')
    def get_badge_is_favorite(self):
        return mark_safe('<span class="m-badge m-badge--wide m-badge--rounded m-badge--'+self.render_string_color(self.is_favorite)+' m-badge--wide">Favorito</span>')
    def get_badge_is_active(self):
        return mark_safe('<span class="m-badge m-badge--wide m-badge--rounded m-badge--'+self.render_string_color(self.is_active)+' m-badge--wide">Activo</span>')
    def get_sellpoint(self):
        return mark_safe(self.render_boolean_del('<span class="m--font-'+self.sellpoint.render_string_color(self.sellpoint.is_active)+'" style="color:'+self.sellpoint.color+'!important">'+self.sellpoint.name+'</span>', self.sellpoint.is_active))

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
    'LIST': [
        {
            'field': 'barcode',
            'title': 'Folio',
        },
        #{
            #'field': 'property_getCutSerial',
            #'title': 'Corte',
        #},
        {
            'field': 'property_getSellpoint',
            'title': 'Punto de Venta',
        },
        #{
            #'field': 'username',
            #'title': 'Usuario',
        #},
        {
            'field': 'ticketType',
            'title': 'Tipo',
        },
        {
            'field': 'property_getIepsMoney',
            'title': 'IEPS',
        },
        {
            'field': 'property_getIvaMoney',
            'title': 'I.V.A.',
        },
        {
            'field': 'property_getTotalMoney',
            'title': 'Total',
        },
        {
            'field': 'property_getOnAccountMoney',
            'title': 'A cuenta',
        },
        {
            'field': 'status',
            'title': 'Estatus',
        },
    ],
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
}
class Ticket(Model_base):
    STATUS_TICKET = (
        ('COBRADO','COBRADO'),
        ('PENDIENTE','PENDIENTE'),
    )
    TICKETTYPE = (
        ('VENTA','VENTA'),
        ('REMISION','REMISION'),
        ('PAGO','PAGO'),
        ('DEVOLUCION','DEVOLUCION'),
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
                self.datetimeOfDelivery = datetime.datetime.strptime(ticket['datetimeOfDelivery'], '%m/%d/%Y %H:%M:%S')
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
    ticket = models.ForeignKey('Ticket', on_delete=models.CASCADE)
    product = models.ForeignKey('ProductAttributes', null=True, on_delete=models.SET_NULL)
    productName = models.CharField(max_length=250, null=True, blank=True)
    alias = models.CharField(max_length=250, null=True, blank=True)
    quantity = models.FloatField(default=0)
    price = models.FloatField(default=0)
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
        self.total = product['total']
        self.iva = product['ivaTotal']
        self.ieps = product['iepsTotal']
        self.save()
        for offer in product['offers']:
            self.offers.add(Offer.objects.get(id=offer['id']))
        return self

########################################################################################
class CutProduct():
    product = ''
    productName = ''
    quantity = 0
    price = 0
    total = 0
    iva = False
    ieps = True
    offers = []
    def __init__(self, product):
        self.product = product.id
        self.productName = product.productName
        self.quantity = product.quantity
        self.price = product.price
        self.total = product.total
        self.iva = product.iva
        self.ieps = product.ieps
    def update(self, product):
        self.quantity += float(product.quantity)
        self.total += product.total
        self.iva += product.iva
        self.ieps += product.ieps
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
    'SERIALIZER': ('getColor',),
    'LIST': [
        {
            'field': 'serial',
            'title': 'Folio',
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
            'field': 'property_getFinal_time',
            'title': 'Fecha/Hora',
            'template': 
            """
                <a href="{{property_url_detail}}" style="text-decoration:none;color:{{property_getColor}}!important;">
                    {{property_getFinal_time}}
                </a>
            """,
        },
        {
            'field': 'property_getIvaMoney',
            'title': 'IVA',
            'template': 
            """
                <a href="{{property_url_detail}}" style="text-decoration:none;color:{{property_getColor}}!important;">
                    {{property_getIvaMoney}}
                </a>
            """,
        },
        {
            'field': 'property_getIepsMoney',
            'title': 'IEPS',
            'template': 
            """
                <a href="{{property_url_detail}}" style="text-decoration:none;color:{{property_getColor}}!important;">
                    {{property_getIepsMoney}}
                </a>
            """,
        },
        {
            'field': 'property_getSubtotalMoney',
            'title': 'Subtotal',
            'template': 
            """
                <a href="{{property_url_detail}}" style="text-decoration:none;color:{{property_getColor}}!important;">
                    {{property_getSubtotalMoney}}
                </a>
            """,
        },
        {
            'field': 'property_getFaltanteMoney',
            'title': 'Faltante',
            'template': 
            """
                <a href="{{property_url_detail}}" style="text-decoration:none;color:{{property_getColor}}!important;">
                    {{property_getFaltanteMoney}}
                </a>
            """,
        },
        {
            'field': 'property_getTotalMoney',
            'title': 'Total Corte',
            'template': 
            """
                <a href="{{property_url_detail}}" style="text-decoration:none;color:{{property_getColor}}!important;">
                    {{property_getTotalMoney}}
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
    VARS = VARS
    class Meta(Model_base.Meta):
        verbose_name = VARS['NAME']
        verbose_name_plural = VARS['PLURAL']
        permissions = permissions(VARS)
    def __str__(self):
        return '{0}'.format(self.id)
    def my_organization(self):
        return self.sellpoint.my_organization()
    def QUERY(self, view):
        return Cut.objects.filter(sellpoint__organization__pk=view.request.session.get('organization'), active=True)
    def url_detail(self):
        return reverse('SV:Cut__DetailView', kwargs={'app': self.VARS['APP'], 'model': self.VARS['MODEL'], 'pk': self.pk})
    def new(self, sellpoint):
        self.sellpoint = sellpoint
        cut = Cut.objects.filter(sellpoint = self.sellpoint).first()
        if cut:
            self.serial = cut.serial + 1
        self.save()
        return self
    def getSellpoint(self):
        return self.sellpoint.name
    def getFinal_time(self):
        if self.final_time:
            return self.render_datetime(self.final_time)
        return '-'
    def getTotal(self):
        total = 0
        for ticket in self.getTickets(status='COBRADO'):
            total += ticket.total
        return "{0:.2f}".format(total)
    def getIva(self):
        total = 0
        for ticket in self.getTickets(status='COBRADO'):
            total += ticket.iva
        return "{0:.2f}".format(total)
    def getIeps(self):
        total = 0
        for ticket in self.getTickets(status='COBRADO'):
            total += ticket.ieps
        return "{0:.2f}".format(total)
    def getSubtotal(self):
        total = 0
        for ticket in self.getTickets(status='COBRADO'):
            total += ticket.total - ticket.ieps - ticket.iva
        return "{0:.2f}".format(total)
    def getLenFaltante(self):
        return len(self.getTickets(status='PENDIENTE'))
    def getFaltante(self):
        total = 0
        for ticket in self.getTickets(status='PENDIENTE'):
            total += ticket.total
        return "{0:.2f}".format(total)
    def getTickets(self, status='all'):
        if status=='all':
            tickets = Ticket.objects.filter(cut=self).exclude(rasurado = True)
        elif status=='PENDIENTE':
            tickets = Ticket.objects.filter(cut=self, status='PENDIENTE').exclude(rasurado = True)
        elif status=='COBRADO':
            tickets = Ticket.objects.filter(cut=self, status='COBRADO').exclude(rasurado = True)
        elif status=='100':
            tickets = Ticket.objects.filter(cut=self)
        return tickets.filter(ticketType='VENTA')
    def getLenTickets(self):
        return len(self.getTickets())
    def getOffersLen(self):
        total = 0
        for ticket in Ticket.objects.filter(cut=self):
            total += ticket.getLenOffers()
        return total
    def makeCut(self):
        if self.getTickets():
            self.final_time = datetime.datetime.now()
        self.save()
        return self
    def getTotalMoney(self):
        return Money(self.getTotal(), Currency.MXN).format('es_MX')
    def getIvaMoney(self):
        return Money(self.getIva(), Currency.MXN).format('es_MX')
    def getIepsMoney(self):
        return Money(self.getIeps(), Currency.MXN).format('es_MX')
    def getSubtotalMoney(self):
        return Money(self.getSubtotal(), Currency.MXN).format('es_MX')
    def getFaltanteMoney(self):
        return Money(self.getFaltante(), Currency.MXN).format('es_MX')
    def getColor(self):
        return self.sellpoint.color
    def getCutProducts(self):
        products = []
        for ticket in self.getTickets():
            for product in ticket.getProducts():
                cutProduct = CutProduct(product)
                exist = False
                for arrayCutProduct in products:
                    if arrayCutProduct.productName == product.productName and arrayCutProduct.price == product.price:
                        arrayCutProduct.update(product)
                        exist = True
                        break
                if not exist:
                    products.append(cutProduct)
        return  sorted(products, key=lambda x: x.quantity, reverse=True)
    def makeRasurado(self, value):
        total = 0
        self.getTickets(status='100').update(rasurado=False)
        for ticket in self.getTickets(status='100'):
            total += ticket.total
        finaltotal = total * value / 100
        print(finaltotal)
        for ticket in self.getTickets(status='100').exclude(invoiced=True).order_by('-total'):
            if total <= finaltotal:
                break
            else:
                ticket.rasurado = True
                ticket.save()
                total -= ticket.total
        self.rasurado = value
        self.save()
        return True

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
    'FORM': [
        Div(
            Div(
                Div('name'),
                Div('is_active'),
                Div('initialDate'),
                Div('finalDate'),
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
                Div('conditionMenus'),
                Div('conditionProducts'),
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
        'conditionProducts': {
            'model': ['SV', 'Product'],
            'plugin': 'selectmultiple',
            'query': [
                (
                    ('organization__pk', 'self.request.session.get("organization")'),
                ),
            ],
        },
        'conditionMenus': {
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
    CONDITIONTYPE = (
        ('productQuantity','Cantidad de productos mínima'),
        ('productValue','Valor fijo del producto'),
    )
    DISCOUNNTTYPE = (
        ('productPercent','Porcentaje del producto'),
        ('productValue','Valor fijo del producto'),
    )
    organization = models.ForeignKey('mirari.Organization', related_name='+', on_delete=models.CASCADE)
    sellpoints = models.ManyToManyField('Sellpoint', related_name='+', blank=True, verbose_name='Puntos de venta que afecta', help_text='Si no eliges ninguno afecta a todas')
    clients = models.ManyToManyField('Client', related_name='+', blank=True, verbose_name='Clientes a los que aplica')
    name = models.CharField('Nombre del descuento', max_length=250)
    discountProducts = models.ManyToManyField('Product', verbose_name='Productos a los que afecta el descuento', blank=True, related_name='+',)
    discountMenus = models.ManyToManyField('Menu', verbose_name='Menus a los que afecta el descuento', blank=True, related_name='+',)
    discountType = models.CharField('Forma de aplicar el descuento', choices=DISCOUNNTTYPE, max_length=250, default="% del producto")
    discountValue = models.FloatField('Valor del descuento')
    conditionType = models.CharField('Forma de generar el descuento', choices=CONDITIONTYPE, max_length=250, default="% del producto")
    conditionValue = models.FloatField('Valor del descuento')
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

