# -*- encoding: utf-8 -*-
from .modelbase import *

########################################################################################
########################################################################################
VARS = {
        'NAME': 'Módulo',
        'PLURAL': 'Módulos',
        'MODEL': 'Module',
        'NEW': 'NUEVO',
        'NEW_GENDER': 'un nuevo',
        'THIS': 'este',
        'APP': APP,
        'EXCLUDE_PERMISSIONS': ['all'],
    }
class Module(Model_base):
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=100)
    VARS = VARS
    class Meta(Model_base.Meta):
        verbose_name = VARS['NAME']
        verbose_name_plural = VARS['PLURAL']
        permissions = permissions(VARS)
    def __str__(self):
        return """[ {0} ] {1}""".format(self.code, self.name)

########################################################################################
########################################################################################
VARS = {
        'NAME':"Organización",
        'PLURAL':"Organizaciones",
        'MODEL':"Organization",
        'NEW':"NUEVA",
        'NEW_GENDER': "una nueva",
        'THIS':"esta",
        'APP':APP,
        'EXCLUDE_PERMISSIONS': ['create', 'update', 'delete'],
        'LIST': [
            {
                'field': 'code',
                'title': 'Código',
                'sorteable': True,
                'serchable': True,
                'url': 'url_update',
            },
            {
                'field': 'name',
                'title': 'Nombre',
                'sorteable': True,
                'serchable': True,
                'url': 'url_update',
            },
            {
                'field': 'get_domains',
                'title': 'Dominio(s)',
                'url': 'url_update',
            },
        ],
    }
def path_system(self, filename):
    upload_to = "O/%s%s/SYSTEM/%s" % (self.id, self.code, filename)
    return upload_to
class Organization(MPTTModel, Model_base):
    parent = TreeForeignKey('self', null=True, blank=True, related_name='+', db_index=True, on_delete=models.CASCADE)
    nivel = models.PositiveIntegerField(default=1)
    sites = models.ManyToManyField(Site)
    name = models.CharField('Nombre de la organización', max_length=50)
    code = models.CharField(max_length=150, unique=True)
    default_mail = models.EmailField('Email de la sucursal', blank=True, null=True)
    contact_mail = models.EmailField('Email de contacto para clientes', blank=True, null=True)
    creation_date = models.DateTimeField(auto_now_add=True)
    modules = models.ManyToManyField('Module', blank=True, related_name='+',)
    color = models.CharField('Color de la empresa', max_length=50, default='#191919')
    TITLE = models.CharField(max_length=255, blank=True, null=True)
    SLOGAN = models.CharField(max_length=255, blank=True, null=True)
    LAYOUT = models.CharField(max_length=255, blank=True, null=True)
    STYLE = models.CharField(max_length=255, blank=True, null=True)
    ICO = ProcessedImageField(upload_to=path_system, blank=True, null=True, options={'quality': 100}, help_text="Logo 100x100")
    LOGO = ProcessedImageField(upload_to=path_system, blank=True, null=True, options={'quality': 100}, help_text="Logo 600x600")
    DASHBOARD_LOGO_WIDTH = models.PositiveIntegerField(blank=True, null=True, default="0", help_text="px")
    LOGO_WHITE = ProcessedImageField(upload_to=path_system, blank=True, null=True, options={'quality': 100}, help_text="Logo 600x600")
    LOGO_BG = ProcessedImageField(upload_to=path_system, blank=True, null=True)
    LOGO_BG_WHITE = ProcessedImageField(upload_to=path_system, blank=True, null=True)
    ######SV
    ticketInvoiceLoginButton = models.BooleanField('Botón de facturacón de tickets en el login', default=False)
    VARS = VARS
    class Meta(Model_base.Meta):
        verbose_name = VARS['NAME']
        verbose_name_plural = VARS['PLURAL']
        permissions = permissions(VARS)
    def __str__(self):
        return self.name
    def QUERY(self, view):
        return Organization.objects.filter(pk = view.request.session.get("organization"))
    def APIRESPONSE(self, view):
        api = view.request.GET.get('api', '')
        if api == 'getCodeOrganization':
            class SiteSerializer(Basic_Serializer):
                class Meta(Basic_Serializer.Meta):
                    model = Site
            class OrganizationSerializer(Basic_Serializer):
                sites = serializers.SerializerMethodField()
                class Meta(Basic_Serializer.Meta):
                    model = Organization
                def get_sites(self, obj):
                    return SiteSerializer(obj.sites.all().last()).data
            if not Organization.objects.filter(code__iexact=request.POST.get('code')).first():
                return JsonResponse({'message':'No se encontró este código de empresa'}, status=500)
            return JsonResponse({'organization':OrganizationSerializer(Organization.objects.filter(code__iexact=request.POST.get('code')).first()).data})
        return JsonResponse({'message':'No se encontro el método'}, status=500)
    def save(self, *args, **kwargs):
        self.name = self.name.upper()
        super().save()
    def my_organization(self):
        return self
    def get_parent(self):
        return self.render_if(self.parent)
    def get_root(self):
        return self.render_if(self.parent)
    def get_domains(self):
        return self.render_list(self.sites, 'domain')
    def get_my_domain(self):
        return self.sites.all().first()
    def get_modules_code(self):
        return self.modules.all().values_list('code', flat=True)
    

    

########################################################################################
########################################################################################
VARS = {
    'NAME': 'Usuario',
    'PLURAL': 'Usuarios',
    'MODEL': 'User',
    'NEW': 'NUEVO',
    'NEW_GENDER': 'un nuevo',
    'THIS': 'este',
    'APP': APP,
    'EXTEND_PERMISSIONS': [('Can_Change__Password', 'Modifica contraseñas'),],
    'LIST': [
        {
            'field': 'visible_username',
            'title': 'Usuario',
            'sorteable': True,
            'serchable': True,
            'url': 'url_update',
        },
        {
            'field': 'get_groups',
            'title': 'Perfiles',
            'url': 'url_update',
        },
        {
            'field': 'get_is_active',
            'title': 'Activo?',
            'url': 'url_update',
        },
    ],
    'HIDE_BUTTONS_UPDATE': True,
    'SEARCH': ['first_name', 'last_name', 'email'],
    'SERIALIZER': ('url_password',),
    'FORM': ('visible_username', 'first_name', 'last_name', 'email', 'is_active', 'groups', 'user_permissions', 'birthday', 'phone', 'can_change_password'),
    'SELECTQ': {
        'groups': {
            'model': ['mirari', 'Profile'],
            'plugin': 'selectmultiple',
        },
        'user_permissions': {
            'model': ['auth', 'Permission'],
            'plugin': 'selectmultiple',
            'query': [
                (
                    ('content_type__app_label__in', 'Organization.objects.get(pk=self.request.session.get("organization")).get_modules_code()'),
                ),
            ],
        },
    },
    'RULES': """
        email: {
            required: true,
            email: true,
        },
    """,
}
class User(AbstractUser, Model_base):
    organization = models.ForeignKey('Organization', blank=True, null=True, on_delete=models.CASCADE, related_name='+',)
    visible_username = models.CharField('Nombre de usuario', max_length=50, help_text="Obligatorio. Longitud máxima 30 caracteres alfanuméricos (letras, dígitos y @/./+/-/_) solamente.")
    birthday = models.DateField('Fecha nacimiento', blank=True, null=True)
    phone = models.CharField('Telefono de contacto', max_length=50, blank=True, null=True)
    gender = models.CharField('Género', choices=GENDER, max_length=50, blank=True, null=True)
    can_change_password = models.BooleanField('Puede cambiar su contraseña?', default=True, help_text='Un usuario puede cambiar su propio passwrod desde su cuenta?')
    needChangePassword = models.BooleanField('Debe cambiar la contraseña?', default=False, help_text='El usuario debe cambiar su contraseña al primer inicio de sesión?')
    id_bckp = models.IntegerField(blank=True, null=True)
    VARS = VARS
    class Meta(Model_base.Meta):
        verbose_name = VARS['NAME']
        verbose_name_plural = VARS['PLURAL']
        permissions = permissions(VARS)
    def __str__(self):
        if self.visible_username:
            return self.visible_username
        else:
            return """{0}""".format(self.username, self.email)
    def QUERY(self, view):
        return User.objects.filter(organization__pk=view.request.session.get('organization'), active=True).exclude(is_superuser=True)
    def APIRESPONSE(self, view):
        api = view.request.GET.get('api', '')
        if api == 'changeOrganization':
            if view.request.user.is_superuser:
                view.request.user.organization = Organization.objects.get(id=view.request.POST.get('organizationPK'))
                view.request.session['organization'] = view.request.POST.get('organizationPK')
                view.request.user.save()
                return JsonResponse({'api':True})
        if api == 'orderServiceID':
            orderService = apps.get_model('TCS', 'OrderService').objects.filter(serial = view.request.POST.get('orderServiceID', 0)).first()
            if orderService:
                return JsonResponse({'api':True, 'url_update': reverse('mirari:Generic__UpdateView', kwargs={'app': orderService.VARS['APP'], 'model': orderService.VARS['MODEL'], 'pk': orderService.pk})})
            return JsonResponse({'api':False, })
        return JsonResponse({'message':'No se encontro el método'}, status=500)
    def url_list(self):
        return reverse('mirari:User__ListView', kwargs={'app': self.VARS['APP'], 'model': self.VARS['MODEL']})
    def url_add(self):
        return reverse('mirari:User__CreateView', kwargs={'app': self.VARS['APP'], 'model': self.VARS['MODEL']})
    def url_update(self):
        return reverse('mirari:User__UpdateView', kwargs={'app': self.VARS['APP'], 'model': self.VARS['MODEL'], 'pk': self.pk})
    def url_password(self):
        return reverse('mirari:UserPassword__UpdateView', kwargs={'app': self.VARS['APP'], 'model': self.VARS['MODEL'], 'pk': self.pk})
    def my_organizations(self):
        if self.is_superuser:
            return Organization.objects.all()
        return self.organization.get_descendants(include_self=True)
    def get_full_name(self):
        return self.first_name + ' ' + self.last_name
    def get_last_login(self):
        if self.last_login:
            return self.render_datetime(self.last_login)
        else:
            return '-'
    def get_is_active(self):
        return self.render_boolean(self.is_active)
    def get_email(self):
        return self.render_if(self.email)
    def get_phone(self):
        return self.render_if(self.phone)
    def get_groups(self):
        return self.render_list(self.groups, 'visible_name')
    def get_all_permissions(self):
        if self.is_superuser:
            return Permission.objects.all()
        return self.user_permissions.all() | Permission.objects.filter(group__user=self)
    def get_available_permissions_pk(self):
        if self.is_superuser:
            myperms = Permission.objects.all()
        else:
            myperms = self.user_permissions.all() | Permission.objects.filter(group__user=self)
        myperms = myperms.filter(content_type__app_label__in=self.organization.get_modules_code())
        return myperms.values_list('pk', flat=True)
    ############ INT ###############################################################
    def get_my_notifications(self):
        return apps.get_model('INT','Notification')().get_user_notifications(self)
    def get_my_teams(self): ### ENTREGA UNA LISTA
        return self.render_list(apps.get_model('INT','Team')().get_user_team(self), 'name')
    def get_my_teams_codes(self):
        return self.render_list(apps.get_model('INT','Team')().get_user_team(self), 'code')
    def get_teams(self): ### ENTREGA LOS MODELOS
        return apps.get_model('INT','Team')().get_user_team(self)

########################################################################################
########################################################################################
VARS = {
    'NAME': 'Perfil',
    'PLURAL': 'Perfiles',
    'MODEL': 'Profile',
    'NEW': 'NUEVO',
    'NEW_GENDER': 'un nuevo',
    'THIS': 'este',
    'APP': APP,
    'LIST': [
        {
            'field': 'visible_name',
            'title': 'Nombre',
            'serchable': True,
            'url': 'url_update',
        },
        {
            'field': 'get_permissions',
            'title': 'Permisos',
            'width': 600,
            'url': 'url_update',
        },
    ],
    'SELECTQ': {
        'permissions': {
            'model': ['auth', 'Permission'],
            'order_by': '-id',
            'plugin': 'selectmultiple',
            'query': [
                (
                    ('content_type__app_label__in', 'Organization.objects.get(pk=self.request.session.get("organization")).get_modules_code()'),
                ),
            ],
        },
    },
    'FORM': ['visible_name','permissions'],
}
class Profile(Group, Model_base):
    organization = models.ForeignKey('Organization', blank=True, null=True, on_delete=models.CASCADE, related_name='+',)
    VARS = VARS
    class Meta(Model_base.Meta):
        verbose_name = VARS['NAME']
        verbose_name_plural = VARS['PLURAL']
        permissions = permissions(VARS)
    def __str__(self):
        return '{0}'.format(self.visible_name)
    def QUERY(self, view):
        return Profile.objects.filter(organization__pk=view.request.session.get('organization'), active=True)
    def save(self, *args, **kwargs):
        self.visible_name = self.visible_name.upper()
        self.name = self.organization.code +'__'+ self.visible_name
        super().save()
    def get_permissions(self):
        return self.render_list(self.permissions, 'name')
    
########################################################################################
########################################################################################
VARS = {
    'NAME': 'Serie',
    'PLURAL': 'Series',
    'MODEL': 'Serial',
    'NEW': 'NUEVA',
    'NEW_GENDER': 'una nueva',
    'THIS': 'esta',
    'APP': APP,
    'EXCLUDE_PERMISSIONS': ['all'],
    'LIST': [
        {
            'field': 'name',
            'title': 'Nombre',
        },
        {
            'field': 'serial',
            'title': 'Numeración',
        },
    ],
}
class Serial(Model_base):
    organization = models.ForeignKey('Organization', blank=True, null=True, on_delete=models.CASCADE, related_name='+',)
    name = models.CharField('Nombre con el que identificas la serie', max_length=120)
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    serial = models.PositiveIntegerField(default=1)
    VARS = VARS
    class Meta(Model_base.Meta):
        verbose_name = VARS['NAME']
        verbose_name_plural = VARS['PLURAL']
        permissions = permissions(VARS)
    def __str__(self):
        return '{0} ( {1} )'.format(self.name, self.serial)
    def get_serial(self):
        self.serial = self.serial + 1
        self.save()
        return self.serial

########################################################################################
########################################################################################
VARS = {
    'NAME':'Producto o Servicio',
    'PLURAL':'Productos o servicios',
    'MODEL':'ProductsServicesSAT',
    'NEW':'NUEVO',
    'NEW_GENDER':'un nuevo',
    'THIS':'este',
    'APP':APP,
    'EXCLUDE_PERMISSIONS': ['all'],
}
class ProductsServicesSAT(Model_base):
    code = models.CharField('Código de producto o servicio',max_length=120)
    name = models.CharField('Nombre de producto o servicio',max_length=255)
    VARS = VARS
    class Meta(Model_base.Meta):
        verbose_name = VARS['NAME']
        verbose_name_plural = VARS['PLURAL']
        permissions = permissions(VARS)
    def __str__(self):
        return '{1} [{0}]'.format(self.code, self.name)

########################################################################################
########################################################################################
VARS = {
    'NAME':'Clave Unidad',
    'PLURAL': 'Clave de Unidades',
    'MODEL':'UnitsCodesSat',
    'NEW':'NUEVA',
    'NEW_GENDER': 'una nueva',
    'THIS':'esta',
    'APP':APP,
    'EXCLUDE_PERMISSIONS': ['all'],
}
class UnitsCodesSat(Model_base):
    code = models.CharField('Código de producto o servicio',max_length=120)
    name = models.CharField('Nombre de producto o servicio',max_length=255)
    class Meta(Model_base.Meta):
        verbose_name = VARS['NAME']
        verbose_name_plural = VARS['PLURAL']
        permissions = permissions(VARS)
    def __str__(self):
        return '{1} [{0}]'.format(self.code, self.name)

########################################################################################
########################################################################################
VARS = {
    'NAME':'DBConnection',
    'PLURAL':'DBConnection',
    'MODEL':'DBConnection',
    'NEW':'NUEVO',
    'NEW_GENDER': 'un nuevo',
    'THIS': 'este',
    'APP':APP,
    'EXCLUDE_PERMISSIONS':['all'],
}
class DBConnection(Model_base):
    organization = models.ForeignKey('mirari.Organization', on_delete=models.CASCADE, related_name='+',)
    name = models.CharField(max_length=250, blank=True, null=True)
    db_name = models.CharField(max_length=250, blank=True, null=True)
    db_host = models.CharField(max_length=250, blank=True, null=True)
    db_user = models.CharField(max_length=250, blank=True, null=True)
    db_password = models.CharField(max_length=250, blank=True, null=True)
    db_datatable = models.CharField(max_length=250, blank=True, null=True)
    VARS = VARS
    class Meta(Model_base.Meta):
        verbose_name = VARS['NAME']
        verbose_name_plural = VARS['PLURAL']
        permissions = permissions(VARS)
    def __str__(self):
        return '{0}'.format(self.name)

########################################################################################
########################################################################################
VARS = {
    'NAME':'HostEmail',
    'PLURAL':'HostEmail',
    'MODEL':'HostEmail',
    'NEW':'NUEVO',
    'NEW_GENDER': 'un nuevo',
    'THIS': 'este',
    'APP':APP,
    'EXCLUDE_PERMISSIONS':['all'],
}
class HostEmail(Model_base):
    organization = models.ForeignKey('Organization', on_delete=models.CASCADE, related_name='+',)
    module = models.ForeignKey('Module', on_delete=models.CASCADE, related_name='+',)
    host = models.CharField(max_length=250)
    port = models.CharField(max_length=250, default='')
    username = models.CharField(max_length=250)
    password = models.CharField(max_length=250)
    email = models.CharField(max_length=250)
    prefix = models.CharField(max_length=250)
    is_available = models.BooleanField(default=True)
    default = models.BooleanField(default=False)
    VARS = VARS
    class Meta(Model_base.Meta):
        verbose_name = VARS['NAME']
        verbose_name_plural = VARS['PLURAL']
        permissions = permissions(VARS)
    def __str__(self):
        return '{0}'.format(self.module)
    def sendMail(self, subject='',template='generic/EmailTemplate.html',fromEmail=None,fromContact='',toEmail=[],files=[], content=None):
        connection = get_connection(host=self.host , port=self.port, username=self.username, password=self.password, use_tls=True)
        connection.open()
        if not fromContact:
            fromContact = self.prefix
        context = {
            'MEDIA_URL': settings.STATIC_URL,
            'STATIC_URL': settings.MEDIA_URL,
            'content': content,
            'organization': self.organization,
        }
        render = render_to_string(template, context)
        for mail in toEmail:
            msg = EmailMultiAlternatives(subject=subject,body=render,from_email=fromContact+'<'+self.email+'>',to=[toEmail],connection=connection)
            msg.attach_alternative(render, "text/html")
            for file in files:
                msg.attach_file(file)
            #msg.send(True)
        connection.close()
        return True

########################################################################################
########################################################################################
VARS = {
    'NAME':'PaginasHTML',
    'PLURAL':'PaginasHTML',
    'MODEL':'HTMLPage',
    'NEW':'NUEVO',
    'NEW_GENDER': 'un nuevo',
    'THIS': 'este',
    'APP':APP,
    'EXCLUDE_PERMISSIONS':['all'],
}
class HTMLPage(Model_base):
    organization = models.ForeignKey('Organization', on_delete=models.CASCADE, related_name='+',)
    folder = models.CharField(max_length=250)
    static = models.CharField(max_length=250)
    index = models.CharField(max_length=250)
    VARS = VARS
    class Meta(Model_base.Meta):
        verbose_name = VARS['NAME']
        verbose_name_plural = VARS['PLURAL']
        permissions = permissions(VARS)
    def __str__(self):
        return '{0}'.format(self.organization)