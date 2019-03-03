# -*- coding: utf-8 -*-
from mirari.mirari.views import *
from .models import *
from .vars import *

class SellpointSerializer(Base_Serializer):
	class Meta(Basic_Serializer.Meta):
		model = Sellpoint
class MenuSerializer(Base_Serializer):
	class Meta(Basic_Serializer.Meta):
		model = Menu
class ProductSerializer(Base_Serializer):
	class Meta(Basic_Serializer.Meta):
		model = Product
class ProductAttributesSerializer(Base_Serializer):
	class Meta(Basic_Serializer.Meta):
		model = ProductAttributes



class sv__Sellpoint__TemplateView(Generic__TemplateView):
	template_name = "sv__Sellpoint__TemplateView.html"
	


class Sellpoint__ApiView(Generic__ApiView):
    permissions = False
    def get_serializers(self, request):
        class SellpointSerializer(Basic_Serializer):
            class Meta(Basic_Serializer.Meta):
                model = Sellpoint
        sellpoints = Sellpoint.objects.filter(organization=request.user.organization, active=True, is_active=True)
        sellpointserializer = SellpointSerializer( sellpoints , many=True ).data
        class ProductSerializer(Basic_Serializer):
            class Meta(Basic_Serializer.Meta):
                model = Product
        class MenuSerializer(Basic_Serializer):
            class Meta(Basic_Serializer.Meta):
                model = Menu
        class ProductAttributesSerializer(Basic_Serializer):
            product = serializers.SerializerMethodField()
            #menu = serializers.SerializerMethodField()
            class Meta(Basic_Serializer.Meta):
                model = ProductAttributes
            def get_product(self, obj):
                return ProductSerializer(obj.product, read_only=True).data
            #def get_menu(self, obj):
                #return MenuSerializer(obj.product.menu, read_only=True, many=True).data
        productattributes = ProductAttributes.objects.filter( sellpoint__in=sellpoints.all() )
        productattributesserializer = ProductAttributesSerializer( productattributes, many=True ).data
        menu = []
        for productattribute in productattributes:
            for pmenu in productattribute.product.menu.all():
                if not pmenu.pk in menu:
                    menu.append(pmenu.pk)
        menus = Menu.objects.filter(pk__in = menu)
        menuserializer = MenuSerializer( menus, many=True ).data
        return JsonResponse({
            'sellpoints':sellpointserializer,
            'productattributes':productattributesserializer,
            'menus':menuserializer,
        }, safe=False)