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
    'FORM': ('name','canBySell','canByBuy','typeProduct','category','sellPrice','costPrice','notes','codebar','uid','minimumQuantity','maximumQuantity','deliveryTerm',),
}
class Product(Model_base):
    PRODUCTTYPE = (
        ('Consumible','Consumible'),
        ('Servicio','Servicio'),
        ('Almacenaje','Almacenaje'),
    )
    organization = models.ForeignKey('mirari.Organization', blank=True, null=True, on_delete=models.CASCADE, related_name='+',)
    name = models.CharField('Nombre del modelo', max_length=250)
    canBySell = models.BooleanField(default=True)
    canByBuy = models.BooleanField(default=True)
    typeProduct = models.CharField('Forma de generar el descuento', choices=PRODUCTTYPE, max_length=250, default="productQuantity")
    category = models.ForeignKey('mirari.CategoryProduct', blank=True, null=True, on_delete=models.SET_NULL, related_name='+',)
    sellPrice = models.FloatField(blank=True, null=True)
    costPrice = models.FloatField(blank=True, null=True)
    notes = models.TextField(blank=True, verbose_name="Notas del producto")
    codebar = models.CharField('Nombre del modelo', max_length=30)
    uid = models.CharField('Nombre del modelo', max_length=30)
    minimumQuantity = models.IntegerField(blank=True, null=True)
    maximumQuantity = models.IntegerField(blank=True, null=True)
    deliveryTerm = models.IntegerField(blank=True, null=True)
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
    def my_organization(self):
        return self.brand.organization


