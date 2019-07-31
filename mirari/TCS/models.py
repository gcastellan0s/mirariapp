# -*- coding: utf-8 -*-
from rest_framework import serializers
from mirari.mirari.models import *
from .vars import *

from datetime import timedelta

########################################################################################
VARS = {
    'NAME':'Empresa',
    'PLURAL':'Empresas',
    'MODEL':'Company',
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
class Company(Model_base):
    organization = models.ForeignKey('mirari.Organization', blank=True, null=True, on_delete=models.CASCADE, related_name='+',)
    name = models.CharField('Nombre de la empresa', max_length=250)
    id_bckp = models.IntegerField(blank=True, null=True)
    VARS = VARS
    class Meta(Model_base.Meta):
        verbose_name = VARS['NAME']
        verbose_name_plural = VARS['PLURAL']
        permissions = permissions(VARS)
    def __str__(self):
        return self.name


########################################################################################
VARS = {
    'NAME':'Tienda',
    'PLURAL':'Tiendas',
    'MODEL':'Store',
    'NEW':'NUEVA',
    'NEW_GENDER': 'una nueva',
    'THIS': 'esta',
    'APP':APP,
    'SELECTQ': {
        'company': {
            'plugin': 'select2',
        },
    },
    'LIST': [
        {
            'field': 'name',
            'title': 'NOMBRE',
        },
        {
            'field': 'getCompany',
            'title': 'COMPAÑIA',
        },
        {
            'field': 'state',
            'title': 'ESTADO',
        },
    ],
    'FORM': ('name','company','state','adress','phone'),
}
class Store(Model_base):
    company = models.ForeignKey('Company', on_delete=models.CASCADE, related_name='+', verbose_name="Empresa")
    state  = models.CharField('Estado', max_length=250, blank=True, null=True)
    adress = models.CharField('Domicilio', max_length=250, blank=True, null=True)
    phone = models.CharField('Teléfono', max_length=250, blank=True, null=True)
    name = models.CharField('Nombre de la tienda', max_length=250)
    id_bckp = models.IntegerField(blank=True, null=True)
    VARS = VARS
    class Meta(Model_base.Meta):
        verbose_name = VARS['NAME']
        verbose_name_plural = VARS['PLURAL']
        permissions = permissions(VARS)
    def __str__(self):
        return self.name
    def QUERY(self, view):
        return Store.objects.filter(company__organization__pk=view.request.session.get('organization'), active=True)
    def getCompany(self):
        return self.company.name

########################################################################################
VARS = {
    'NAME':'Marca',
    'PLURAL':'Marcas',
    'MODEL':'Brand',
    'NEW':'NUEVA',
    'NEW_GENDER': 'una nueva',
    'THIS': 'esta',
    'APP':APP,
    'SELECTQ': {
        'company': {
            'plugin': 'selectmultiple',
        },
    },
    'LIST': [
        {
            'field': 'name',
            'title': 'NOMBRE',
        },
        {
            'field': 'getCompanys',
            'title': 'COMPAÑIAS',
        },
    ],
    'FORM': ('name','company',),
}
class Brand(Model_base):
    organization = models.ForeignKey('mirari.Organization', on_delete=models.CASCADE, related_name='+',)
    company = models.ManyToManyField('Company', verbose_name="Empresas que la venden")
    name = models.CharField('Nombre de la marca', max_length=250)
    id_bckp = models.IntegerField(blank=True, null=True)
    VARS = VARS
    class Meta(Model_base.Meta):
        verbose_name = VARS['NAME']
        verbose_name_plural = VARS['PLURAL']
        permissions = permissions(VARS)
    def __str__(self):
        return self.name
    def QUERY(self, view):
        return Brand.objects.filter(company__organization__pk=view.request.session.get('organization'), active=True).distinct()
    def getCompanys(self):
        return self.render_list(self.company, 'name')


########################################################################################
VARS = {
    'NAME':'Modelo',
    'PLURAL':'Modelos',
    'MODEL':'Modelo',
    'NEW':'NUEVO',
    'NEW_GENDER': 'un nuevo',
    'THIS': 'este',
    'APP':APP,
    'SELECTQ': {
        'brand': {
            'plugin': 'select2',
        },
    },
    'LIST': [
        {
            'field': 'getBrand',
            'title': 'MARCA',
        },
        {
            'field': 'name',
            'title': 'NOMBRE',
        },
        {
            'field': 'description',
            'title': 'DESCRIPCIÓN',
        },
    ],
    'FORM': ('name','brand','description'),
}
class Modelo(Model_base):
    brand = models.ForeignKey('Brand', on_delete=models.SET_NULL, null=True, verbose_name="Marca")
    name = models.CharField('Nombre del modelo', max_length=250)
    description = models.CharField('Descripción', max_length=250, blank=True, null=True)
    id_bckp = models.IntegerField(blank=True, null=True)
    VARS = VARS
    class Meta(Model_base.Meta):
        verbose_name = VARS['NAME']
        verbose_name_plural = VARS['PLURAL']
        permissions = permissions(VARS)
    def __str__(self):
        return self.name
    def QUERY(self, view):
        return Modelo.objects.filter(brand__company__organization__pk=view.request.session.get('organization'), active=True).distinct()
    def getBrand(self):
        return self.brand.name

########################################################################################
VARS = {
    'NAME':'Informacion de Orden',
    'PLURAL':'Informacion de Orden',
    'MODEL':'Modelo',
    'NEW':'NUEVA',
    'NEW_GENDER': 'una nueva',
    'THIS': 'esta',
    'APP':APP,
    'EXCLUDE_PERMISSIONS': ['delete','create','update'],
    'LIST': [
        {
            'field': 'id',
            'title': 'INFORMACIÓN',
            'template': 
                """
                    <a href="{{url_update}}" class="a-no">
                        <span>INFORMACION DE LA ORDEN EN LAS IMPRESIONES</span>
                    </a>
                """,
            
        },
    ],
}
class OrderServiceInformation(Model_base):
    organization = models.ForeignKey('mirari.Organization', on_delete=models.CASCADE, related_name='+',)
    VARS = VARS
    class Meta(Model_base.Meta):
        verbose_name = VARS['NAME']
        verbose_name_plural = VARS['PLURAL']
        permissions = permissions(VARS)
    def __str__(self):
        return 'Orden de servicio'
    def QUERY(self, view):
        return OrderServiceInformation.objects.filter(organization__pk=view.request.session.get('organization'), active=True).distinct()

########################################################################################
VARS = {
    'NAME':'Orden de servicio',
    'PLURAL':'Ordenes de servicio',
    'MODEL':'OrderService',
    'NEW':'NUEVA',
    'NEW_GENDER': 'una nueva',
    'THIS': 'esta',
    'APP':APP,
    'EXCLUDE_PERMISSIONS': ['delete'],
    'HIDE_CHECKBOX_LIST': True,
    'HIDE_BUTTONS_LIST': True,
    'SERIALIZER': ('get_serial_html','get_creation_date_html','get_technical_html','get_concept_html','get_store_html','get_brand_html','get_modelo_html','get_service_date_html','get_client_name_html', 'get_email_html', 'get_contact_phone1_html', 'get_contact_phone2_html','get_contact_phone3_html','get_adress_html','get_icon_os_html','get_icon_ics_html','get_icon_ics_2_html','get_icon_ics_3_html','get_icon_on_html','get_icon_cn_html'),
    'PAGEList': 'OrderService__ListView.pug',
    'PAGECreate': 'OrderService__CreateView.pug',
    'LISTLENGTH':10,
    'LISTDOM': "<'row'<'col-sm-12 col-md-6'p><'col-sm-12 col-md-6'i>><'row'<'col-sm-12'tr>><'row'<'col-sm-12 col-md-4'p><'col-sm-12 col-md-2 mt-2'l><'col-sm-12 col-md-6'i>>",
    'LIST': [
        {
            'field': 'serial',
            'title': 'ORDEN',
            'template': 
                """
                    <a href="{{url_update}}" class="a-no">
                        <span>
                            {{get_serial_html}}
                            {{get_creation_date_html}}
                            {{get_technical_html}}
                            {{get_concept_html}}
                            {{get_store_html}}
                            {{get_brand_html}}
                            {{get_modelo_html}}
                        </span>
                    </a>
                """,
        },
        {
            'field': 'service_date',
            'title': 'SERVICIO',
            'template': 
                """
                    <a href="{{url_update}}" class="a-no">
                        <span>
                            {{get_service_date_html}}
                            {{get_client_name_html}}
                            {{get_email_html}}
                            {{get_contact_phone1_html}}
                            {{get_contact_phone2_html}}
                            {{get_contact_phone3_html}}
                            {{get_adress_html}}
                        </span>
                    </a>
                """,
        },
        {
            'field': 'get_user_html',
            'title': 'INFORMACIÓN',
            'template': 
                """
                    <a href="{{url_update}}" class="a-no">
                        <span>{{get_user_html}}</span>
                    </a>
                """,
            
        },
        {
            'field': 'icon_os',
            'title': 'ICON',
            'width':250,
            'template': 
                """
                    <a href="{{url_update}}" class="a-no">
                        <span>
                            {{get_icon_os_html}}
                            {{get_icon_ics_html}}
                            {{get_icon_ics_2_html}}
                            {{get_icon_ics_3_html}}
                            {{get_icon_on_html}}
                            {{get_icon_cn_html}}
                        </span>
                    </a>
                """,
        },
    ],
    'LISTLENGTH': 10,
    'SEARCH': ['serial', 'client_name', 'email'],
    'SELECTQ': {
        'technical': {
            'model': ['mirari', 'User'],
            'plugin': 'select2',
            'query': [
                (
                    ('organization__pk', 'self.request.session.get("organization")'),
                ),
            ],
            'sercheable': ('visible_username__icontains','email__icontains'),
            'limits': 50,
            'placeholder': 'Elige un técnico',
            'field_filter': (
                ('zone', """$("input[name='zone']:checked").val()"""),
            ),
            'minimumInputLength': '0',
        },
        'company': {
            'model': ['TCS', 'Company'],
            'plugin': 'select2',
            'query': [
                (
                    ('organization__pk', 'self.request.session.get("organization")'),
                ),
            ],
            'placeholder': 'Elige una empresa',
        },
        'store': {
            'model': ['TCS', 'Store'],
            'plugin': 'select2',
            'query': 'none',
            'sercheable': ('name__icontains',),
            'limits': 50,
            'placeholder': 'Elige una tienda',
            'field_filter': (
                ('company', """$("#id_company").val()"""),
            ),
            'minimumInputLength': '0',
        },
        'brand': {
            'model': ['TCS', 'Brand'],
            'plugin': 'select2',
            'query': 'none',
            'sercheable': ('name__icontains',),
            'limits': 50,
            'placeholder': 'Elige una marca',
            'field_filter': (
                ('company', """$("#id_company").val()"""),
            ),
            'minimumInputLength': '0',
        },
        'modelo': {
            'model': ['TCS', 'Modelo'],
            'plugin': 'select2',
            'query': 'none',
            'sercheable': ('name__icontains',),
            'limits': 50,
            'placeholder': 'Elige un modelo',
            'field_filter': (
                ('brand', """$("#id_brand").val()"""),
            ),
            'minimumInputLength': '0',
        },
    },
    'FORM': [
        Div(
            Div(
                InlineRadios('service'),
                css_class="col-md-4"
            ),
            Div(
                InlineRadios('zone'),
                css_class="col-md-4"
            ),
            Div('service_date', css_class="col-md-4"),
            Div(
                InlineRadios('concept'),
                css_class="col-md-8"
            ),
            Div('technical', css_class="col-md-4"),
            css_class="form-group m-form__group row"
        ),
        Div(
            Div('client_name', css_class="col-md-4"),
            Div('email', css_class="col-md-4"),
            Div('contact_phone1', css_class="col-md-4"),
            Div('contact_phone2', css_class="col-md-4"),
            Div('address', css_class="col-md-8"),
            Div('colony', css_class="col-md-5"),
            Div('city', css_class="col-md-5"),
            Div('cp', css_class="col-md-2"),
            Div('address_reference', css_class="col-md-12"),
            Div('client_notes', css_class="col-md-8"),
            Div('company', css_class="col-md-4"),
            css_class="form-group m-form__group row"
        ),
        Div(
            Div('store', css_class="col-md-4"),
            Div('brand', css_class="col-md-4"),
            Div('modelo', css_class="col-md-4"),
            Div('report_name', css_class="col-md-3"),
            Div('serial_number', css_class="col-md-3"),
            Div('buy_date', css_class="col-md-3"),
            Div('delivery_date', css_class="col-md-3"),
            css_class="form-group m-form__group row"
        ),
        Div(
            Div(
                Div('icon_os'),
                Div('icon_ics'),
                Div('icon_ics_2'),
                Div('icon_ics_3'),
                Div('icon_on'),
                Div('icon_cn'),
                css_class="col-md-4"
            ),
            Div(
                Div('hidden_notes'),
                Div('order_notes'),
                css_class="col-md-8"
            ),
            css_class="form-group m-form__group row"
        ),
    ],
    'FORM_CLASS': 'small_form',
}
class OrderService(Model_base):
    estatus_choices = ESTATUS
    serial = models.IntegerField(verbose_name="Folio de la orden")
    organization = models.ForeignKey('mirari.Organization', blank=True, null=True, on_delete=models.CASCADE, related_name='+',)
    creation_date = models.DateTimeField(auto_now_add=True, editable=True)
    user = models.ForeignKey('mirari.User', related_name='+', on_delete=models.SET_NULL, null=True)
    technical = models.ForeignKey('mirari.User', related_name='+', on_delete=models.SET_NULL, null=True, verbose_name="Tecnico")
    status = models.CharField(max_length=250, choices=ESTATUS, verbose_name="Estatus", default="Nueva") #Esta parte esta agregada directamente al codigo OrderService__CreateView.html
    service = models.CharField(max_length=250, choices=SERVICIO, default="Icon", verbose_name="Tipo de servicio")
    zone = models.CharField(max_length=250, choices=ZONAS, default="Local", verbose_name="Zona")
    concept = models.CharField(max_length=250, choices=CONCEPTO, default="Armado", verbose_name="Concepto")
    service_date = models.DateField(verbose_name="Fecha programada")
    buy_date = models.DateField(blank=True, null=True, verbose_name="Fecha de compra")
    delivery_date = models.DateField(blank=True, null=True, verbose_name="Fecha de entrega")
    client_name = models.CharField(max_length=500, verbose_name="Nombre completo del cliente")
    email = models.CharField(max_length=250, blank=True, verbose_name="Email del cliente")
    contact_phone1 = models.CharField(max_length=250, blank=True, verbose_name="Teléfono casa")
    contact_phone2 = models.CharField(max_length=250, blank=True, verbose_name="Teléfono oficina")
    contact_phone3 = models.CharField(max_length=250, blank=True, verbose_name="Teléfono movil")
    address = models.CharField(max_length=500, blank=True, verbose_name="Dirección")
    colony = models.CharField(max_length=250, blank=True, verbose_name="Colonia")
    city = models.CharField(max_length=250, blank=True, verbose_name="Ciudad")
    cp = models.CharField(max_length=250, blank=True, verbose_name="CP")
    address_reference = models.CharField(max_length=500, blank=True, verbose_name="Referencias")
    address_lat = models.FloatField(blank=True, null=True)
    address_lng = models.FloatField(blank=True, null=True)
    client_notes = models.TextField(blank=True, verbose_name="Notas sobre el cliente")
    company = models.ForeignKey('Company', on_delete=models.SET_NULL, null=True, verbose_name="Empresa")
    companyName = models.CharField(max_length=250, blank=True, null=True)
    store = models.ForeignKey('Store', on_delete=models.SET_NULL, null=True, verbose_name="Tienda")
    storeName = models.CharField(max_length=250, blank=True, null=True)
    brand = models.ForeignKey('Brand', on_delete=models.SET_NULL, null=True, verbose_name="Marca")
    brandName = models.CharField(max_length=250, blank=True, null=True)
    report_name = models.CharField(max_length=250, blank=True, verbose_name="Nombre de quien reporta")
    modelo = models.ForeignKey('Modelo', on_delete=models.SET_NULL, null=True, blank=True, verbose_name="Modelo")
    modeloName = models.CharField(max_length=250, blank=True, null=True)
    serial_number = models.CharField(max_length=250, blank=True, verbose_name="Numero de serie")
    hidden_notes = models.TextField(blank=True, verbose_name="Notas OCULTAS<small>(No se imprimen en la orden)</small>")
    order_notes = models.TextField(blank=True, verbose_name="Notas IMPRESAS<small>(Impresas en la orden)</small>")
    icon_os = models.CharField(max_length=250, blank=True)
    icon_ics = models.CharField('icon ics 1', max_length=250, blank=True)
    icon_ics_2 = models.CharField('icon ics 2', max_length=250, blank=True, default="")
    icon_ics_3 = models.CharField('icon ics 3', max_length=250, blank=True, default="")
    icon_on = models.CharField(max_length=250, blank=True)
    icon_cn = models.CharField(max_length=250, blank=True)
    id_bckp = models.IntegerField(blank=True, null=True)
    comments = models.TextField(blank=True, verbose_name="Comentarios")
    VARS = VARS
    class Meta(Model_base.Meta):
        verbose_name = VARS['NAME']
        verbose_name_plural = VARS['PLURAL']
        permissions = permissions(VARS)
        ordering = ['-id']
    def __str__(self):
        return str(self.serial)
    def url_add(self):
        return reverse('mirari:Generic__CreateView', kwargs={'app': self.VARS['APP'], 'model': self.VARS['MODEL']})
    def select2filter(self, query):
        if self.request.GET.get('field') == 'technical':
            profile = apps.get_model('mirari', 'Profile').objects.filter(name__icontains=self.request.GET.get('zone'), organization__id=self.request.session['organization']).first()
            if profile:
                query = query.filter( groups = profile )
            else:
                query = None
        if self.request.GET.get('field') == 'store':
            if self.request.GET.get('company'):
                query = query.filter(company = apps.get_model('TCS', 'Company').objects.filter(pk=self.request.GET.get('company')).first())
            else:
                query = query.none()
        if self.request.GET.get('field') == 'brand':
            if self.request.GET.get('company'):
                query = query.filter(company = apps.get_model('TCS', 'Company').objects.filter(pk=self.request.GET.get('company')).first())
            else:
                query = query.none()
        if self.request.GET.get('field') == 'modelo':
            if self.request.GET.get('brand'):
                query = query.filter(brand = apps.get_model('TCS', 'Brand').objects.filter(pk=self.request.GET.get('brand')).first())
            else:
                query = query.none()
        return query
    def save(self, *args, **kwargs):
        if not self.serial:
            self.serial = Serial.objects.filter(organization=self.organization, content_type=ContentType.objects.get_for_model(self)).first().get_serial()
        orderServiceConcept = None
        if not self.pk:
            orderServiceConcept = OrderServiceConcept()
        super().save()
        if orderServiceConcept:
            orderServiceConcept.orderservice = self
            if self.service == 'Icon':
                if self.concept == 'Armado':
                    orderServiceConcept.concept = '**Armado'
                    orderServiceConcept.quantity = 23
                elif self.concept == 'Revision':
                    orderServiceConcept.concept = '**Revision'
                    orderServiceConcept.quantity = 50
                elif self.concept == 'OrdenesIcon':
                    orderServiceConcept.concept = '**Orden Icon'
                    orderServiceConcept.quantity = 50
                elif self.concept == 'Mantenimiento':
                    orderServiceConcept.concept = '**Mantenimiento'
                    orderServiceConcept.quantity = 50
                elif self.concept == 'Servicio':
                    orderServiceConcept.concept = '**Servicio'
                    orderServiceConcept.quantity = 50
            if self.service == 'Tecnoservicio':
                if self.concept == 'Armado':
                    orderServiceConcept.concept = '**Armado'
                    orderServiceConcept.quantity = 650
                elif self.concept == 'Revision':
                    orderServiceConcept.concept = '**Revision'
                    orderServiceConcept.quantity = 350
                elif self.concept == 'OrdenesIcon':
                    orderServiceConcept.concept = '**Orden Icon'
                    orderServiceConcept.quantity = 50
                elif self.concept == 'Mantenimiento':
                    orderServiceConcept.concept = '**Mantenimiento'
                    orderServiceConcept.quantity = 750
                elif self.concept == 'Servicio':
                    orderServiceConcept.concept = '**Servicio'
                    orderServiceConcept.quantity = 750
            if self.service == 'Tc2':
                if self.concept == 'Armado':
                    orderServiceConcept.concept = '**Armado'
                    orderServiceConcept.quantity = 300
                elif self.concept == 'Revision':
                    orderServiceConcept.concept = '**Revision'
                    orderServiceConcept.quantity = 300
                elif self.concept == 'OrdenesIcon':
                    orderServiceConcept.concept = '**Orden Icon'
                    orderServiceConcept.quantity = 300
                elif self.concept == 'Mantenimiento':
                    orderServiceConcept.concept = '**Mantenimiento'
                    orderServiceConcept.quantity = 300
                elif self.concept == 'Servicio':
                    orderServiceConcept.concept = '**Servicio'
                    orderServiceConcept.quantity = 300
            orderServiceConcept.save()
    def FORM_VALID(self, view, form):
        if not form.instance.pk:
            form.instance.user = view.request.user
        return form
    def APIRESPONSE(self, view):
        api = view.request.GET.get('api', '')
        if api == 'addConcept':
            if view.request.POST.get('concept') and view.request.POST.get('quantity'):
                orderserviceconcept = OrderServiceConcept()
                orderserviceconcept.orderservice = view.get_object()
                orderserviceconcept.user = view.request.user
                orderserviceconcept.concept = '['+view.request.user.visible_username+'] '+ view.request.POST.get('concept')
                orderserviceconcept.quantity = view.request.POST.get('quantity')
                orderserviceconcept.save()
            return JsonResponse({'OrderServiceConcept':OrderServiceConceptSerializer(OrderServiceConcept.objects.filter(orderservice=view.get_object()).order_by('creation_date'),many=True).data})
        if api == 'addComment':
            if view.request.POST.get('comment'):
                orderservicecomment = OrderServiceComment()
                orderservicecomment.orderservice = view.get_object()
                orderservicecomment.user = view.request.user
                orderservicecomment.comment = view.request.POST.get('comment')
                orderservicecomment.save()
            return JsonResponse({'OrderServiceComment': OrderServiceCommentSerializer(OrderServiceComment.objects.filter(orderservice=view.get_object()).order_by('creation_date'),many=True).data})
        if api == 'updateStatus':    
            if view.request.POST.get('status'):
                obj = view.get_object()
                obj.status = view.request.POST.get('status')
                obj.save()
            return JsonResponse({'api':'ok'})
        if api == 'getCalendar':   
            start = datetime.datetime.utcfromtimestamp(int(view.request.GET.get('start'))).date()
            end = datetime.datetime.utcfromtimestamp(int(view.request.GET.get('end'))).date()
            class OrderServiceCalendar_Serializer(serializers.ModelSerializer):
                class Meta:
                    model = OrderService
                    fields = ('title','start','end', 'id', 'url_update','className', 'description')
            query = self.QUERY(self, view)
            query = query.filter(service_date__range=(start, end))
            if view.request.GET.get('zone', None):
                query = query.filter(zone = view.request.GET.get('zone'))
            serializer = OrderServiceCalendar_Serializer(query, many=True)
            return JsonResponse(serializer.data,  safe=False)
        return JsonResponse({'message':'No se encontro el método'}, status=500)
    def QUERY(self, view):
        team_codes = view.request.user.get_groups()
        if 'OPERADOR' in team_codes or 'ADMINISTRADOR' in team_codes or view.request.user.is_superuser:
            orderService = OrderService.objects.filter(organization__pk=view.request.session.get('organization'), active=True).distinct()
        else:
            orderService = OrderService.objects.filter(organization__pk=view.request.session.get('organization'), technical=view.request.user, active=True).distinct()
        if len(view.request.GET.get('search[value]', '')) > 3:
            return orderService.filter(service_date__gt=datetime.datetime.now()-timedelta(days=365))
        return orderService.filter(service_date__gt=datetime.datetime.now()-timedelta(days=30))
    def get_id_html(self):
        return '<strong class="mr-2 m--icon-font-size-lg3">{0}</strong> <small>[{1}]</small><br />'.format(self.id, self.service.upper())
    def get_serial_html(self):
        return """
            <strong class="mr-2 h3 {2}">
                {0}
            </strong> 
            <small class="m--font-brandºº">[{1}]</small>
            <br />
        """.format(self.serial, self.service.upper(), self.getColorStatus())
    def get_creation_date_html(self):
        return """
            <i class="fa fa-calendar m--icon-font-size-sm5 mr-1 text-muted"></i>
            {0}<br />
            """.format(self.creation_date.strftime('%d %b %Y %I:%M %p'))
    def get_user_html(self):
        return """
            <i class="fa fa-user-edit m--icon-font-size-sm5 mr-1 text-muted"></i> 
            OPERADOR: {0}
            <br />
        """.format(self.user)
    def get_technical_html(self):
        return """
            <i class="fa fa-user-cog m--icon-font-size-sm5 mr-1 text-muted"></i> 
            {0}
            <br />
        """.format(self.technical)
    def get_concept_html(self):
        return """<i class="fa fa-cog m--icon-font-size-sm5 mr-1 text-muted"></i>{0}<br />""".format(self.concept)
    def get_store_html(self):
        if self.store:
            return """<i class="fa fa-store m--icon-font-size-sm5 mr-1 text-muted"></i>{0}<br />""".format(self.store)
        else:
            return ''
    def get_brand_html(self):
        if self.brand:
            return """<i class="fa fa-tags m--icon-font-size-sm5 mr-1 text-muted"></i>{0} """.format(self.brand)
        else:
            return ''
    def get_modelo_html(self):
        if self.modelo:
            return """<i class="fa fa-tag m--icon-font-size-sm5 mr-1 text-muted"></i>{0}<br />""".format(self.modelo)
        else:
            return ''
    def get_service_date_html(self):
        if self.service_date:
            return """<i class="fa fa-calendar-check m--icon-font-size-sm5 mr-1 text-muted"></i><strong>{0}</strong><br />""".format(self.service_date.strftime('%d %b %Y'))
        else:
            return '<i class="fa fa-calendar m--icon-font-size-sm5 mr-1 text-muted"></i>'
    def get_client_name_html(self):
        if self.client_name:
            return """<i class="fa fa-user m--icon-font-size-sm5 mr-1 text-muted"></i>{0}<br />""".format(self.client_name.title())
        else:
            return ''
    def get_email_html(self):
        if self.email:
            return """<i class="fa fa-envelope m--icon-font-size-sm5 mr-1 text-muted"></i>MAIL: {0}<br />""".format(self.email)
        else:
            return ''
    def get_contact_phone1_html(self):
        if self.contact_phone1:
            return """<i class="fa fa-phone m--icon-font-size-sm5 mr-1 text-muted"></i>TEL: {0}<br />""".format(self.contact_phone1)
        else:
            return ''
    def get_contact_phone2_html(self):
        if self.contact_phone2:
            return """<i class="fa fa-building m--icon-font-size-sm5 mr-1 text-muted"></i>OFI: {0}<br />""".format(self.contact_phone2)
        else:
            return ''
    def get_contact_phone3_html(self):
        if self.contact_phone3:
            return """<i class="fa fa-mobile m--icon-font-size-sm5 mr-1 text-muted"></i>CEL: {0}<br />""".format(self.contact_phone3)
        else:
            return ''
    def get_adress_html(self):
        adress = ''
        if self.address:
            adress += self.address + ', '
        if self.colony:
            adress += 'col. ' + self.colony + ', ' 
        if self.city:
            adress += self.city + ' '
        if self.cp:
            adress += 'CP ' + self.cp
        return """<i class="fa fa-map-marker-alt m--icon-font-size-sm5 mr-1 text-muted"></i> {0}<br />""".format(adress)
    def get_icon_os_html(self):
        if self.icon_os:
            return  """<i class="fa fa-cog m--icon-font-size-sm5 mr-1 text-muted"></i>OS: {0}<br />""".format(self.icon_os)
        return ''
    def get_icon_ics_html(self):
        if self.icon_ics:
            return  """<i class="fa fa-cog m--icon-font-size-sm5 mr-1 text-muted"></i>ICS: {0}<br />""".format(self.icon_ics)
        return ''
    def get_icon_ics_2_html(self):
        if self.icon_ics_2:
            return  """<i class="fa fa-cog m--icon-font-size-sm5 mr-1 text-muted"></i>ICS2: {0}<br />""".format(self.icon_ics_2)
        return ''
    def get_icon_ics_3_html(self):
        if self.icon_ics_3:
            return  """<i class="fa fa-cog m--icon-font-size-sm5 mr-1 text-muted"></i>ICS3: {0}<br />""".format(self.icon_ics_3)
        return ''
    def get_icon_on_html(self):
        if self.icon_on:
            return  """<i class="fa fa-cog m--icon-font-size-sm5 mr-1 text-muted"></i>ON: {0}<br />""".format(self.icon_on)
        return ''
    def get_icon_cn_html(self):
        if self.icon_cn:
            return  """<i class="fa fa-cog m--icon-font-size-sm5 mr-1 text-muted"></i>CN: {0}<br />""".format(self.icon_cn)
        return ''
    def get_total(self):
        orderserviceconcept = OrderServiceConcept.objects.filter(orderservice = self)
        total = 0
        for concept in orderserviceconcept:
            total += concept.quantity
        return total
    def title(self):
        return '{0} {1}'.format(self.serial, self.service)
    def start(self):
        return self.service_date.strftime("%Y-%m-%d")
    def end(self):
        return self.service_date.strftime("%Y-%m-%d")
    def description(self):
        v = 'No asignado'
        if self.technical:
            if self.technical.visible_username:
                v = self.technical.visible_username
        c = 'No asignado'
        if self.client_name:
            c = self.client_name
        return mark_safe("""T. {0} | C. {1}""".format(v, c))
    def className(self):
        if self.status == 'Alerta':
            return 'fc-event-warning fc-event-solid-warning'
        elif self.status == 'Espera de refacciones':
            return 'fc-event-warning fc-event-solid-warning'
        elif self.status == 'Terminada':
            return 'fc-event-dark fc-event-solid-dark'
        elif self.status == 'Cancelada':
            return 'fc-event-danger fc-event-solid-danger'
        elif self.status == 'Especial':
            return 'fc-event-success fc-event-solid-success'
        return 'fc-event-info fc-event-solid-info'
    def getColorStatus(self):
        if self.status == 'Alerta':
            return 'text-warning'
        elif self.status == 'Espera de refacciones':
            return 'text-warning'
        elif self.status == 'Terminada':
            return 'text-dark'
        elif self.status == 'Cancelada':
            return 'text-danger'
        elif self.status == 'Especial':
            return 'text-success'
        return 'text-info'

########################################################################################
VARS = {
    'NAME':'Comentario de Orden',
    'PLURAL':'Comentarios de Orden',
    'MODEL':'OrderServiceComment',
    'NEW':'NUEVO',
    'NEW_GENDER': 'un nuevo',
    'THIS': 'este',
    'APP':APP,
}
class OrderServiceComment(Model_base):
    orderservice = models.ForeignKey('OrderService', on_delete=models.CASCADE, related_name='+',)
    user = models.ForeignKey('mirari.User', related_name='+', on_delete=models.SET_NULL, null=True)
    comment = models.TextField()
    creation_date = models.DateTimeField(auto_now_add=True, editable=True)
    id_bckp = models.IntegerField(blank=True, null=True)
    VARS = VARS
    class Meta(Model_base.Meta):
        verbose_name = VARS['NAME']
        verbose_name_plural = VARS['PLURAL']
        permissions = permissions(VARS)
    def __str__(self):
        return str(self.pk)
class OrderServiceCommentSerializer(serializers.ModelSerializer):
    username = serializers.CharField(source='user.visible_username')
    class Meta:
        model = OrderServiceComment
        fields = ('__all__')

########################################################################################
VARS = {
    'NAME':'Concepto de Orden',
    'PLURAL':'Conceptos de Orden',
    'MODEL':'OrderServiceConcept',
    'NEW':'NUEVO',
    'NEW_GENDER': 'un nuevo',
    'THIS': 'este',
    'APP':APP,
}
class OrderServiceConcept(Model_base):
    orderservice = models.ForeignKey('OrderService', on_delete=models.CASCADE, related_name='+',)
    user = models.ForeignKey('mirari.User', related_name='+', on_delete=models.SET_NULL, null=True)
    concept = models.CharField(max_length=250, blank=True,)
    quantity = models.FloatField()
    creation_date = models.DateTimeField(auto_now_add=True, editable=True)
    id_bckp = models.IntegerField(blank=True, null=True)
    VARS = VARS
    class Meta(Model_base.Meta):
        verbose_name = VARS['NAME']
        verbose_name_plural = VARS['PLURAL']
        permissions = permissions(VARS)
    def __str__(self):
        return str(self.pk)
class OrderServiceConceptSerializer(serializers.ModelSerializer):
    #username = serializers.CharField(source='user.visible_username')
    class Meta:
        model = OrderServiceConcept
        fields = ('__all__')

########################################################################################
VARS = {
    'NAME':'Historial de Orden',
    'PLURAL':'Historial de Ordenes',
    'MODEL':'OrderServiceHistory',
    'NEW':'NUEVA',
    'NEW_GENDER': 'una nueva',
    'THIS': 'esta',
    'APP':APP,
    'EXCLUDE_PERMISSIONS': ['all'],
}
class OrderServiceHistory(Model_base):
    orderservice = models.ForeignKey('OrderService', blank=True, null=True, on_delete=models.CASCADE, related_name='+',)
    user = models.ForeignKey('mirari.User', related_name='+', on_delete=models.SET_NULL, null=True)
    notes = models.TextField(blank=True, verbose_name="Notas <small>(Impresas en la orden)</small>")
    id_bckp = models.IntegerField(blank=True, null=True)
    VARS = VARS
    class Meta(Model_base.Meta):
        verbose_name = VARS['NAME']
        verbose_name_plural = VARS['PLURAL']
        permissions = permissions(VARS)
    def __str__(self):
        return str(self.pk)