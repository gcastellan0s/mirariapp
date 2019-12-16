# -*- coding: utf-8 -*-
from rest_framework import serializers
from mirari.mirari.models import *
from .vars import *


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
            'title': 'NOMBRE DEL PROVEEDOR',
        },
    ],
    'FORM': ('name',),
}
class Provider(Model_base):
    organization = models.ForeignKey('mirari.Organization', blank=True, null=True, on_delete=models.CASCADE, related_name='+',)
    name = models.CharField('Nombre del proveedor', max_length=250)
    VARS = VARS
    class Meta(Model_base.Meta):
        verbose_name = VARS['NAME']
        verbose_name_plural = VARS['PLURAL']
        permissions = permissions(VARS)
    def __str__(self):
        return self.name


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
    ],
    'FORM_CLASS': 'kt-form kt-form--fit kt-form--label-right form-horizontal small_form',
    'FORM': [
        Div(
            Div('name', css_class="col-md-12"),
            css_class="form-group m-form__group row mt-3"
        ),
        Div('canBySell', css_class="col-md-12"),
        Div('canByBuy', css_class="col-md-12"),
        Div(
            Div(
                Div('typeProduct', css_class="col-md-12"),
                Div('category', css_class="col-md-12"),
                Div('uid', css_class="col-md-12"),
                Div('codebar', css_class="col-md-12"),
                css_class="col-md-7"
            ),
            Div(
                Div('sellPrice', css_class="col-md-12"),
                Div('costPrice', css_class="col-md-12"),
                css_class="col-md-5"
            ),
            css_class="form-group m-form__group row"
        ),
        Div('notes', css_class="col-md-12"),
    ],
    #'SELECTQ': {
        #'technical': {
            #'model': ['STR', 'CategoryProduct'],
            #'plugin': 'select2',
            #'query': [
                #(
                    #('organization__pk', 'self.request.session.get("organization")'),
                #),
            #],
            #'sercheable': ('name__icontains'),
            #'limits': 50,
            #'placeholder': 'Elige una categoría',
            #'minimumInputLength': '0',
        #},
    #},
}

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
    typeProduct = models.CharField('Tipo de producto', choices=PRODUCTTYPE, max_length=250, default="productQuantity")
    category = models.ForeignKey('STR.CategoryProduct', blank=True, null=True, on_delete=models.SET_NULL, verbose_name="Categoría del producto", related_name  ='+',)
    uid = models.CharField('Referencia interna (PKU)', max_length=30)
    codebar = models.CharField('Código de barras', max_length=30)
    sellPrice = models.FloatField('Venta $', blank=True, null=True)
    costPrice = models.FloatField('Costo $', blank=True, null=True)
    notes = models.TextField(blank=True, verbose_name="NOTAS INTERNAS")
    weight = models.FloatField('Peso', blank=True, null=True)
    volume = models.FloatField('Volumen', blank=True, null=True)
    deliveryTerm = models.IntegerField('Plazo de entrega', blank=True, null=True)
    users = models.ManyToManyField('mirari.User', verbose_name="Responsables")
    deliveryDescription = models.TextField(blank=True, verbose_name="Descripción para pedidos de entrega")
    receptionsDescription = models.TextField(blank=True, verbose_name="Descripción para recepciones")
    minimumQuantity = models.IntegerField(blank=True, null=True)
    maximumQuantity = models.IntegerField(blank=True, null=True)
    id_bckp = models.IntegerField(blank=True, null=True)
    VARS = VARS
    class Meta(Model_base.Meta):
        verbose_name = VARS['NAME']
        verbose_name_plural = VARS['PLURAL']
        permissions = permissions(VARS)
    def __str__(self):
        return self.name

class ProductHistory(Model_base):
    HISTORYTYPE = (
        ('ENTRADA','ENTRADA'),
        ('SALIDA','SALIDA'),
        ('ACTUALIZACION','ACTUALIZACION'),
    )
    user = models.ForeignKey('mirari.User', blank=True, null=True, on_delete=models.SET_NULL)
    historyType = models.CharField('Tipo de producto', choices=HISTORYTYPE, max_length=250, default="productQuantity")
    datetime = models.DateTimeField(auto_now_add=True)
    product = models.ForeignKey('STR.Product', blank=True, null=True, on_delete=models.SET_NULL)
    id_bckp = models.IntegerField(blank=True, null=True)
    class Meta(Model_base.Meta):
        verbose_name = VARS['NAME']
        verbose_name_plural = VARS['PLURAL']
        permissions = permissions(VARS)
    def __str__(self):
        return self.name
    def QUERY(self, view):
        return ProductHistory.filter(product__organization__pk=view.request.session.get('organization'))