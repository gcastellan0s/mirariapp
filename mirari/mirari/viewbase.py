  # -*- coding: utf-8 -*-
from django.views import View
from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.base import TemplateView
from django.views.generic.detail import DetailView
from django.template.loader import render_to_string
from django.shortcuts import get_object_or_404, get_list_or_404, render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.sites.shortcuts import get_current_site
from django.contrib.contenttypes.models import ContentType
from django.contrib import messages
from django.http import HttpResponseRedirect, JsonResponse
from django.core.exceptions import PermissionDenied
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.utils.translation import gettext as _
from django.utils import timezone
from django.urls import reverse
from django.http import Http404
from django.db.models import Q
from django.contrib import messages
from django.apps import apps
from django.conf import settings
from django.core.paginator import Paginator
from django.forms import widgets
from django import forms

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework_jwt.serializers import VerifyJSONWebTokenSerializer

from crispy_forms.helper import FormHelper
from crispy_forms.layout import *

import requests
import json

from rest_framework import serializers
from validate_email import validate_email

from .models import *
from .vars import *

#raise ValueError('xxx')

################################################################################################################
######### BASES ################################################################################################
################################################################################################################
######### RETURN ###############################################################################################
def return_site(request):
    site = get_current_site(request)
    if site == 'localhost:8000':
        return Site.objects.get(domain=settings.DEFAULT_DOMAIN)
    return site
######### VARIABLES ############################################################################################
def get_variables(class_view):
    site = return_site(class_view.request)
    if class_view.permissions:
        check_permissions(class_view)
    try:
        organization = Organization.objects.get(pk=class_view.request.session['organization'])
    except:
        organization = Organization.objects.filter(sites=site).first()
    return {
        'ORGANIZATION': organization,
        'SITE': site,
        'MEDIA': settings.MEDIA_URL,
    }
def check_permissions(class_view):
    def check_owner(owner, object):
        if not owner == object:
            raise Http404()
    if not class_view.permissions == True:
        for permission in class_view.permissions:
            if not class_view.request.user.has_perm(permission):
                raise PermissionDenied
    else:
        if class_view.model:
            perm = ''
            if not class_view.model.VARS['APP'] in class_view.request.user.organization.get_modules_code():
                raise PermissionDenied
            if '__ListView' in class_view.__class__.__name__:
                perm = '.Can_View__'
            elif '__DetailView' in class_view.__class__.__name__:
                perm = '.Can_View__'
                check_owner(class_view.request.user.organization, class_view.object.my_organization())
            elif '__CreateView' in class_view.__class__.__name__:
                perm = '.Can_Create__'
            elif '__UpdateView' in class_view.__class__.__name__:
                perm = '.Can_Update__'
                check_owner(class_view.request.user.organization, class_view.object.my_organization())
            elif '__DeleteView' in class_view.__class__.__name__:
                perm = '.Can_Delete__'
                check_owner(class_view.request.user.organization, class_view.get_object().my_organization())
            if perm:
                if not class_view.request.user.has_perm(class_view.model.VARS['APP']+perm+class_view.model.VARS['MODEL']):
                    raise PermissionDenied
    return True

################################################################################################################
#########  SERIALIZER  #########################################################################################
################################################################################################################
class Basic_Serializer(serializers.ModelSerializer):
    class Meta:
        model = None
        fields = ('__all__')
        exclude = ()
class Base_Serializer(Basic_Serializer):
    property_url_list = serializers.ReadOnlyField(source='url_list')
    property_url_add = serializers.ReadOnlyField(source='url_add')
    property_url_update = serializers.ReadOnlyField(source='url_update')
    property_url_delete = serializers.ReadOnlyField(source='url_delete')
    property_url_detail = serializers.ReadOnlyField(source='url_detail')
    property_str_obj = serializers.ReadOnlyField(source='str_obj')
    class Meta(Basic_Serializer.Meta):
        model = None
        fields = ('__all__')
def Select2Serializer(self):
    class SerializerSelect2(Basic_Serializer):
        class Meta(Basic_Serializer.Meta):
            fields = ('str_select2', 'id')
    model = apps.get_model(self.model.VARS['SELECTQ'][self.request.GET.get('field')]['model'][0], self.model.VARS['SELECTQ'][self.request.GET.get('field')]['model'][1])
    query = model.objects.all()
    if 'query' in self.model.VARS['SELECTQ'][self.request.GET.get('field')]:
        if self.model.VARS['SELECTQ'][self.request.GET.get('field')]['query'] == 'all':
            query = query
        elif self.model.VARS['SELECTQ'][self.request.GET.get('field')]['query'] == 'none':
            query = query
        else:
            q = Q()
            for attributes in self.model.VARS['SELECTQ'][self.request.GET.get('field')]['query']:
                params = {}
                for attribute in attributes:
                    params.update({attribute[0]: eval(attribute[1])})
                q.add(Q(**params), Q.OR)
            query = model.objects.filter(q)
    if 'sercheable' in self.model.VARS['SELECTQ'][self.request.GET.get('field')]:
        if 'minimumInputLength' in self.model.VARS['SELECTQ'][self.request.GET.get('field')]:
            minimumInputLength = self.model.VARS['SELECTQ'][self.request.GET.get('field')]['minimumInputLength']
        else:
            minimumInputLength = '1'
        if not self.request.GET.get('search') and minimumInputLength == '0':
            query = query
        else:
            q = Q()
            for element in self.model.VARS['SELECTQ'][self.request.GET.get('field')]['sercheable']:
                q.add(Q(**{element: self.request.GET.get('search')}), Q.OR)
            query = query.filter(q)
    query = self.select2filter(query)
    try:
        query = query.filter(active=True)
    except:
        query = query.none()
    if 'order_by' in self.model.VARS['SELECTQ'][self.request.GET.get('field')]:
        query = query.order_by(self.model.VARS['SELECTQ'][self.request.GET.get('field')]['order_by'])
    if 'limits' in self.model.VARS['SELECTQ'][self.request.GET.get('field')]:
        query = query[0:self.model.VARS['SELECTQ'][self.request.GET.get('field')]['limits']]
    SerializerSelect2.Meta.model = model
    return SerializerSelect2(query, many=True).data



################################################################################################################
#########  FORM  ###############################################################################################
################################################################################################################
class Basic_Form(forms.ModelForm):
    class Meta:
        model = None
        fields = ('__all__')
    def AddKwargs(self, kwargs):
        return kwargs
class Base_Form(Basic_Form):
    class Meta(Basic_Form.Meta):
        pass
    def __init__(self, *args, **kwargs):
        fields_select = {}
        if 'SELECTQ' in self.Meta.model.VARS:
            if self.Meta.model.VARS['SELECTQ']:
                for key, value in self.Meta.model.VARS['SELECTQ'].items():
                    fields_select.update({key: kwargs.pop(key)})
                    #try:
                        #getattr(self.Meta.model(), 'SELECTQ__' + key)()
                        #fields_select.update({key: kwargs.pop(key)})
                    #except Exception as e:
                        #fields_select.update({key: kwargs.pop(key)})
        super().__init__(*args, **kwargs)
        if fields_select:
            for key, value in fields_select.items():
                self.fields[key].queryset = value
    def AddKwargs(self, kwargs):
        if 'SELECTQ' in self.model.VARS:
            if self.model.VARS['SELECTQ']:
                for key, value in self.model.VARS['SELECTQ'].items():
                    try:
                        kwargs[key] = getattr(self.model(), 'SELECTQ__' + key)(model=self.model._meta.get_field(key).remote_field.model, view=self)
                    except Exception as e:
                        if 'model' in value:
                            model = apps.get_model(value['model'][0], value['model'][1])
                        else:
                            model = self.model._meta.get_field(key).remote_field.model
                        query = model.objects.all()
                        if 'query' in value:
                            if value['query'] == 'all':
                                query = model.objects.all()
                            elif value['query'] == 'none':
                                query = model.objects.none()
                            else:
                                q = Q()
                                for attributes in value['query']:
                                    params = {}
                                    for attribute in attributes:
                                        params.update({attribute[0]: eval(attribute[1])})
                                    q.add(Q(**params), Q.OR)
                                query = model.objects.filter(q)
                        if 'order_by' in value:
                            query = query.order_by(value['order_by'])
                        if 'limits' in value:
                            query = query[0:value['limits']]
                        try:
                            query = query.filter(organization__pk=self.request.session.get('organization'))
                        except:
                            pass
                        try:
                            query = query.filter(is_active=True)
                        except:
                            pass
                        try:
                            query = query.filter(active=True)
                        except:
                            pass
                        if self.request.method == 'POST':
                            if self.request.POST.get(key):
                                query = model.objects.filter(**{'pk': self.request.POST.get(key)}) | query
                        try:
                            query = model.objects.filter(**{'pk': getattr(self.object, key).pk}) | query
                        except:
                            pass
                        kwargs[key] = query
        return kwargs

################################################################################################################
######### TEMPLATE #############################################################################################
################################################################################################################
class Base_Template(object):
    template_name = 'generic/TemplateView.html'
    model= None
    permissions = None
    HTMLPage=None
    ############################################################################################################
    #dispatch()
    #http_method_not_allowed()
    #get_context_data()
    ############################################################################################################
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context = self.proccess_context(context)
        context['HTMLPage'] = self.HTMLPage
        context['model'], context['G'] = self.model, get_variables(self)
        return context
    ############################################################################################################
    def proccess_context(self, context):
        return context
    def get_default_serializer(self):
        class Serializer(Base_Serializer):
            class Meta(Base_Serializer.Meta):
                model = self.model
        return Serializer


################################################################################################################
######### TEMPLATE #############################################################################################
################################################################################################################
class Base_Detail(object):
    permissions = None
    model= None
    template_name = 'generic/DetailView.html'
    ############################################################################################################
    #dispatch()
    #http_method_not_allowed()
    #get_template_names()
    #get_slug_field()
    #get_queryset()
    #get_object()
    #get_context_object_name()
    #get_context_data()
    #get()
    #render_to_response()
    ############################################################################################################
    def dispatch(self, request, *args, **kwargs):
        self.initialize(request, *args, **kwargs)
        return super().dispatch(request, *args, **kwargs)
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context = self.proccess_context(context)
        context['model'], context['G'] = self.model, get_variables(self)
        return context
    ############################################################################################################
    def initialize(self, request, *args, **kwargs):
        self.model = apps.get_model(kwargs['app'], kwargs['model'])
        return True
    def proccess_context(self, context):
        return context
        

################################################################################################################
#########  LIST  ###############################################################################################
################################################################################################################
class Base_List(object):
    template_name = 'generic/ListView.html'
    paginator_size = settings.PAGINATOR_SIZE
    permissions = True
    model = None
    verbose_name = None
    verbose_name_plural = None
    ############################################################################################################
    LIST = []
    SERIALIZER = []
    SEARCH = []
    SORTEABLE = []
    FILTERS = []
    QUERY = []
    EXCLUDE_SERIALIZER = []
    BASEMODEL = []
    ############################################################################################################
    # dispatch()
    # http_method_not_allowed()
    # get_template_names()
    # get_queryset()
    # get_context_object_name()
    # get_context_data()
    # get()
    # render_to_response()
    ############################################################################################################
    def dispatch(self, request, *args, **kwargs):
        self.initialize(request, *args, **kwargs)
        if request.GET.get('action') == 'list':
            try:
                query_list = self.query_list()
                query = request.GET.get('query[generalSearch]')
                if query:
                    query_list = self.query_search(query_list, query)
                query_list = self.query_filter(request, query_list)
                field = request.GET.get('sort[field]')
                sort = request.GET.get('sort[sort]')
                if sort == 'desc' or sort == 'asc':
                    query_list = self.sort(query_list, field, sort)
                page = request.GET.get('pagination[page]', 1)
                perpage = request.GET.get('pagination[perpage]', self.paginator_size)
                paginator = Paginator(query_list, perpage)
                return JsonResponse({'data': self.get_default_serializer()(paginator.page(page), many=True).data, 'meta': {'page': page, 'pages': paginator.num_pages, 'perpage': perpage, 'total': len(query_list), 'sort': sort, 'field': field, }})
            except Exception, e:
                return JsonResponse({'data': str(e)})
        return super().dispatch(request, *args, **kwargs)
    def get_queryset(self):
        return None
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['model'], context['G'] = self.model, get_variables(self)
        context['paginator_size'] = self.paginator_size
        context['list'] = self.list()
        context['q'] = self.request.GET.get('q')
        context['filters'] = self.filters()
        context['verbose_name'] = self.verbose_name
        context['verbose_name_plural'] = self.verbose_name_plural
        context = self.proccess_context(context)
        return context
    #############################################################################################################
    def get_default_serializer(self):
        class Serializer(Base_Serializer):
            for field in self.LIST:
                if field['field'][0:9] == 'property_':
                    vars()[field['field']] = eval("serializers.ReadOnlyField(source='"+field['field'][9:len(field['field'])]+"')")
            for field in self.SERIALIZER:
                vars()['property_'+field] = eval("serializers.ReadOnlyField(source='"+field+"')")
            class Meta(Base_Serializer.Meta):
                model = self.model
        serializer = Serializer
        if self.EXCLUDE_SERIALIZER:
            serializer.Meta.fields = None
            serializer.Meta.exclude = self.EXCLUDE_SERIALIZER
        return Serializer
    def initialize(self, request, *args, **kwargs):
        if not self.model:
            try:
                self.model = apps.get_model(kwargs['app'], kwargs['model'])
            except:
                pass
        self.initialize_list(request, *args, **kwargs)
        return True
    def initialize_list(self, request, *args, **kwargs):
        if not self.LIST:
            if 'LIST' in self.model.VARS:
                self.LIST = self.model.VARS['LIST']
            else:
                self.LIST = [{'field': 'property_str_obj', 'title': self.model.VARS['PLURAL'], 'url': 'property_url_update', },]
        if not self.SERIALIZER:  
            if 'SERIALIZER' in self.model.VARS:
                self.SERIALIZER = self.model.VARS['SERIALIZER']
        if not self.SEARCH:  
            if 'SEARCH' in self.model.VARS:
                self.SEARCH = self.model.VARS['SEARCH']
        if not self.SORTEABLE:  
            if 'SORTEABLE' in self.model.VARS:
                self.SORTEABLE = self.model.VARS['SORTEABLE']
        if not self.QUERY:  
            if 'QUERY' in self.model.VARS:
                self.QUERY = self.model.VARS['QUERY']
        if not self.EXCLUDE_SERIALIZER:  
            if 'EXCLUDE_SERIALIZER' in self.model.VARS:
                self.EXCLUDE_SERIALIZER = self.model.VARS['EXCLUDE_SERIALIZER']
        return True
    def proccess_context(self, context):
        return context
    def list(self):
        return self.render_list()
    def query_list(self):
        try: 
            return self.model().QUERY(self)
        except Exception as e:
            if self.QUERY:
                if self.QUERY['query'] == 'ALL':
                    query = self.model.objects.all()
                elif self.QUERY['query'] == 'NONE':
                    query = self.model.objects.none()
                else:
                    q = Q()
                    for attributes in self.QUERY['query']:
                        params = {}
                        for attribute in attributes:
                            params.update({attribute[0]: eval(attribute[1])})
                        q.add(Q(**params), Q.OR)
                    query = self.model.objects.filter(q)
                if 'order_by' in self.QUERY:
                    query = query.order_by(self.QUERY['order_by'])
                return query.distinct()
            else:
                try:
                    return self.model.objects.filter(organization__pk=self.request.session.get('organization'), active=True)
                except:
                    return self.model.objects.none()
    def query_search(self, query_list, query):
        if not self.SEARCH:
            return query_list
        q = Q()
        for attribute in self.SEARCH:
            q.add(Q(**{attribute+'__icontains': query}), Q.OR)
        return query_list.filter(q)
    def query_filter(self, request, query_list):
        filters = self.filters()
        for value in filters:
            if request.GET.get('query['+value['key']+']'):
                query_list = query_list.filter(**{value['key']: request.GET.get('query['+value['key']+']')})
        return query_list
    def sort(self, query_list, field, sort):
        if sort == 'asc':
            field = '-' + field
        return query_list.order_by(field)
    def render_list(self, btn_update='property_url_update', btn_delete='property_url_delete', btn_checkbox=True, extrabuttons='',):
        dictionary_datatable = []
        if not 'HIDE_CHECKBOX_LIST' in self.model.VARS:
            if btn_checkbox and self.request.user.has_perm(self.model.VARS['APP']+'.Can_Delete__'+self.model.VARS['MODEL']) and not 'delete' in self.model().exclude_permissions():
                dictionary_datatable.append({'field': "property_url_delete", 'title': "#", 'locked': '{left: "xl"}','sortable': 'false', 'width': 40, 'selector': '{class: "m-checkbox--solid m-checkbox--brand"}'})
        for item in self.LIST:
            item_dictionary = {}
            item_dictionary['field'] = item['field']
            item_dictionary['title'] = item['title'].upper()
            if not item['field'] in self.SORTEABLE:
                item_dictionary['sortable'] = 'false'
            if 'sortable' in item:
                item_dictionary['sortable'] = item['sortable']
            if 'template' in item:
                item_dictionary['template'] = item['template']
            else:
                item_dictionary['template'] = '{{'+item['field']+'}}'
            if 'url' in item:
                if item['url'] == 'property_url_update':
                    if self.request.user.has_perm(self.model.VARS['APP']+'.Can_Update__'+self.model.VARS['MODEL']):
                        item_dictionary['template'] = '<a href="{{'+item['url']+'}}" class="a-no">'+item_dictionary['template']+'</a>'
                else:
                    item_dictionary['template'] = '<a href="{{'+item['url']+'}}" class="a-no">'+item_dictionary['template']+'</a>'
            if 'width' in item:
                item_dictionary['width'] = item['width']
            dictionary_datatable.append(item_dictionary)
        btn_update = self.get_btn_update(btn_update)
        btn_delete = self.get_btn_delete(btn_delete)
        if not 'HIDE_BUTTONS_LIST' in self.model.VARS:
            if btn_update or btn_delete or extrabuttons:
                dictionary_datatable.append({'field': '', 'title': '', 'width': 150, 'template': extrabuttons + btn_update + btn_delete})
        return dictionary_datatable
    def get_btn_update(self, btn_update):
        if btn_update and self.request.user.has_perm(self.model.VARS['APP']+'.Can_Update__'+self.model.VARS['MODEL']) and not 'update' in self.model().exclude_permissions():
            btn_update = '<a href="{{'+btn_update+'}}" class="btn btn-outline-brand m-btn m-btn--icon m-btn--icon-only m-btn--custom m-btn--pill btn-sm m--margin-right-25" title="Editar"><i class="la la-edit"></i></a>'
        else:
            btn_update = ''
        return btn_update
    def get_btn_delete(self, btn_delete):
        if btn_delete and self.request.user.has_perm(self.model.VARS['APP']+'.Can_Delete__'+self.model.VARS['MODEL']) and not 'delete' in self.model().exclude_permissions():
            btn_delete = '<a href="" value="{{'+btn_delete+'}}" text="'+self.model().delete_text()[3]+'" class="btn btn-outline-danger m-btn m-btn--icon m-btn--icon-only m-btn--custom m-btn--pill btn-sm delete_row" title="Borrar"><i class="la la-trash"></i></a>'
        else:
            btn_delete = ''
        return btn_delete
    def filters(self):
        filters = []
        if self.FILTERS:
            for key, value in self.FILTERS.items():
                options = []
                if 'list' in value:
                    for object in value['list']:
                        options.append([object[0], object[1]])
                if 'query' in value:
                    q = Q()
                    for attributes in value['query']:
                        params = {}
                        for attribute in attributes:
                            params.update({attribute[0]: eval(attribute[1])})
                        q.add(Q(**params), Q.OR)
                    for object in apps.get_model(value['model'][0], value['model'][1]).objects.filter(q):
                        options.append([object.pk, object.str_obj()])
                item_dictionary = {
                    'key': key,
                    'size': value['size'],
                    'label': value['label'],
                    'options': options,
                }
                filters.append(item_dictionary)
        return filters



################################################################################################################
######### CREATE ###############################################################################################
################################################################################################################
class Base_Create(object):
    template_name = 'generic/CreateView.html'
    permissions = True
    model = None
    formhelper = None
    ############################################################################################################
    #as_view()
    #dispatch()
    #form_invalid()
    #form_valid()
    #get()
    #get_context_data()
    #get_form()
    #get_form_kwargs()
    #get_object()
    #head()
    #http_method_not_allowed()
    #post()
    #put()
    #render_to_response()
    ############################################################################################################
    def dispatch(self, request, *args, **kwargs):
        self.initialize(request, *args, **kwargs)
        return super().dispatch(request, *args, **kwargs)
    def form_valid(self, form):
        try:
            form.instance.organization = self.request.user.organization
        except:
            pass
        form = form.instance.FORM_VALID(self, form)
        return super().form_valid(form)
    def form_invalid(self, form):
        return super().form_invalid(form)
    def get(self, request, *args, **kwargs):
        response = super().get(request, *args, **kwargs)
        extra_response = self.extra_response(request)
        if extra_response:
            return extra_response
        if self.request.GET.get('action') == 'select2':
            return self.select2_response()
        return response
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['model'], context['G'] = self.model, get_variables(self)
        if 'REDIRECT_MODEL' in self.model.VARS:
            context['redirect_model'] = apps.get_model(self.model.VARS['REDIRECT_MODEL'][0], self.model.VARS['REDIRECT_MODEL'][1])
        context = self.proccess_context(context)
        return context
    def get_form_kwargs(self):
        return self.get_form_class().AddKwargs(self, super().get_form_kwargs())
    ############################################################################################################
    def initialize(self, request, *args, **kwargs):
        self.model = apps.get_model(kwargs['app'], kwargs['model'])
        if 'TEMPLATE_NAME' in self.model.VARS:
            if 'CREATEVIEW' in self.model.VARS['TEMPLATE_NAME']:
                self.template_name = self.model.VARS['TEMPLATE_NAME']['CREATEVIEW']
        return True
    def get_success_url(self):
        if 'save' in self.request.POST:
            return self.model().url_list()
        elif 'save__edit' in self.request.POST:
            messages.add_message(self.request, messages.SUCCESS, 'Registro guardado con éxito.')
            return self.object.url_update()
        elif 'save__other' in self.request.POST:
            messages.add_message(self.request, messages.SUCCESS, 'Registro guardado con éxito.')
            return self.model().url_add()
        return self.model().url_list()
    def proccess_context(self, context):
        return context
    def get_form_class(self):
        class Form(Base_Form):
            class Meta(Base_Form.Meta):
                model = self.model
                fields = []
                exclude = []
                if 'FORM' in model.VARS:
                    for field in model.VARS['FORM']:
                        if type(field) == str:
                            fields.append(field)
                        else:
                            for field_name in field.get_field_names():
                                fields.append(field_name[1])
                else:
                    fields = '__all__'
                if 'EXCLUDE_FORM' in model.VARS:
                    exclude.append(model.VARS['EXCLUDE_FORM'])
                else:
                    if 'FORM' in model.VARS:
                        if not 'active' in model.VARS['FORM']:
                            exclude.append('active')
                        if not 'organization' in model.VARS['FORM']:
                            exclude.append('organization')
                    else:
                        exclude.append('active')
                        exclude.append('organization')
            def __init__(self, *args, **kwargs):
                super().__init__(*args, **kwargs)
                self.helper = FormHelper()
                self.helper.layout = Layout()
                self.helper.layout.append(HTML(FORMTEMPLATE1))
                if 'FORM_ID' in self._meta.model.VARS:
                    self.helper.form_id = self._meta.model.VARS['FORM_ID']
                else:	
                    self.helper.form_id = 'form'
                if 'FORM_CLASS' in self._meta.model.VARS:
                    self.helper.form_class = self._meta.model.VARS['FORM_CLASS']
                else:
                    self.helper.form_class = 'm-form m-form--label-align-left- m-form--state- form-horizontal'
                div = Div(css_class="form-group m-form__group")
                if 'FORM' in self._meta.model.VARS:
                    is_crispy_helper = False
                    for field in self._meta.model.VARS['FORM']:
                        if type(field) == str:
                            div.append(field)
                        else:
                            self.helper.layout.append(field)
                            is_crispy_helper = True
                    if not is_crispy_helper:
                        self.helper.layout.append(div)
                else:
                    for field in self._meta.model._meta.get_fields():
                        exclude_from_form = False
                        if 'EXCLUDE_FORM' in self._meta.model.VARS:
                            if field.name in self._meta.model.VARS['EXCLUDE_FORM']:
                                exclude_from_form = True
                        if field.name == 'active' or field.name == 'organization':
                            if not self._meta.fields:
                                exclude_from_form = True
                            else:
                                if field.name in self._meta.fields:
                                    exclude_from_form = True
                        if not exclude_from_form:
                            div.append(field.name)
                    self.helper.layout.append(div)
                self.helper.layout.append(HTML(FORMTEMPLATE2))
        return Form
    def extra_response(self, request):
        return self.model.EXTRA_RESPONSE(self, request)
    def select2_response(self):
        return JsonResponse({'items': Select2Serializer(self)})
    def select2filter(self, query):
        return self.model.select2filter(self, query)



################################################################################################################
######### UPDATE ###############################################################################################
################################################################################################################
class Base_Update(Base_Create):
    ############################################################################################################
    #as_view()
    #dispatch()
    #form_invalid()
    #form_valid()
    #get()
    #get_context_data()
    #get_form()
    #get_form_kwargs()
    #get_object()
    #head()
    #http_method_not_allowed()
    #post()
    #put()
    #render_to_response()
    ############################################################################################################
    def get_success_url(self):
        if 'save' in self.request.POST:
            if 'REDIRECT_MODEL' in self.model.VARS:
                redirect_model = apps.get_model(self.model.VARS['REDIRECT_MODEL'][0], self.model.VARS['REDIRECT_MODEL'][1])
                return redirect_model().url_list()
            return self.model().url_list()
        elif 'save__edit' in self.request.POST:
            messages.add_message(self.request, messages.SUCCESS, 'Registro actualizado con éxito')
            return self.object.url_update()
        elif 'delete' in self.request.POST:
            return self.object.url_delete()
        return self.model().url_list()



################################################################################################################
######### DELETE ###############################################################################################
################################################################################################################
class Base_Delete(object):
    permissions = True
    model = None
    ############################################################################################################
    #as_view()
    #delete()
    #dispatch()
    #get()
    #get_context_data()
    #get_object()
    #head()
    #http_method_not_allowed()
    #post()
    #render_to_response()
    ############################################################################################################
    def delete(self, request, *args, **kwargs):
        self.initialize(request, *args, **kwargs)
        object = self.get_object()
        self.delete_actions(object)
        if request.method == 'POST':
            return JsonResponse({'data' :self.get_success_url()})
        return HttpResponseRedirect(self.get_success_url())
    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)
    ############################################################################################################
    def delete_actions(self, object):
        object.active = False
        return object.save()
    def get_success_url(self):
        return self.model().url_list()
    def initialize(self, request, *args, **kwargs):
        self.model = apps.get_model(kwargs['app'], kwargs['model'])
        return True


class Base_Api(object):
    model = None
    permissions = None
    serializer = None
    def dispatch(self, request, *args, **kwargs):
        self.initialize(request, *args, **kwargs)
        if request.method == "POST" or request.method == "GET":
            return self.get_serializers(request)
        return super().dispatch(request, *args, **kwargs)
    ############################################################################################################
    def initialize(self, request, *args, **kwargs):
        self.model = apps.get_model(kwargs['app'], kwargs['model'])
        self.have_permissions(request)
    def have_permissions(self, request):
        if self.permissions:
            try:
                valid_data = VerifyJSONWebTokenSerializer().validate({'token': request.META.get('HTTP_AUTHORIZATION', " ").split(' ')[1]})
                self.request.user = valid_data['user']
            except Exception as e:
                raise PermissionDenied
            return True
    def actions(self, request):
        return True
    def get_serializers(self, request):
        objects = self.get_objects().data
        self.actions(request)
        return JsonResponse(objects)
    def get_objects(self):
        pk = self.get_pk()
        if pk:
            try:
                class ApiSerializer(Base_Serializer):
                    class Meta(Basic_Serializer.Meta):
                        pass
                ApiSerializer.Meta.model = self.model
                return ApiSerializer(self.get_object(pk))
            except self.model.DoesNotExist:
                raise Http404
        else:
            pass
    def get_object(self, pk):
        self.object = self.model.objects.get(pk=pk)
        return self.object
    def get_pk(self):
        if 'pk' in self.request.GET:
            return self.request.GET['pk']
        else:
            return None

class View400(TemplateView):
    template_name = "generic/errors/400.html"

class View403(TemplateView):
    template_name = "generic/errors/403.html"

class View404(TemplateView):
    template_name = "generic/errors/404.html"

class View500(TemplateView):
    template_name = "generic/errors/500.html"