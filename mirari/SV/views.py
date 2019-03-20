# -*- coding: utf-8 -*-
from mirari.mirari.views import *
from .models import *
from .vars import *

########################################################
########################################################
class SellpointSerializer(Base_Serializer):
    class Meta(Basic_Serializer.Meta):
        model = Sellpoint
########################################################	
class MenuSerializer(Base_Serializer):
    class Meta(Basic_Serializer.Meta):
        model = Menu
########################################################
class ProductSerializer(Base_Serializer):
    class Meta(Basic_Serializer.Meta):
        model = Product
########################################################
class ProductAttributesSerializer(Base_Serializer):
    product = serializers.SerializerMethodField()
    class Meta(Basic_Serializer.Meta):
        model = ProductAttributes
    def get_product(self, obj):
        return ProductSerializer(obj.product, read_only=True).data
########################################################
class TicketSerializer(Base_Serializer):
    sellpoint = serializers.SerializerMethodField()
    class Meta(Basic_Serializer.Meta):
        model = Ticket
    def get_sellpoint(self, obj):
        return SellpointSerializer(obj.sellpoint, read_only=True).data
########################################################
class CutSerializer(Base_Serializer):
    propertyGetTotalMoney = serializers.ReadOnlyField(source='getTotalMoney')
    propertyGetIvaMoney = serializers.ReadOnlyField(source='getIvaMoney')
    propertyGetIepsMoney = serializers.ReadOnlyField(source='getIepsMoney')
    propertyGetSubtotalMoney = serializers.ReadOnlyField(source='getSubtotalMoney')
    class Meta(Basic_Serializer.Meta):
        model = Cut
########################################################
class OfferSerializer(Base_Serializer):
    mySellpoints = serializers.ReadOnlyField(source='get_sellpointsId')
    myDiscountProducts = serializers.ReadOnlyField(source='get_discountProductsId')
    myConditionProducts = serializers.ReadOnlyField(source='get_conditionProductsId')
    #allDiscountProducts = serializers.SerializerMethodField()
    #allConditionProducts = serializers.SerializerMethodField()
    #allsellpoints = serializers.SerializerMethodField()
    class Meta(Basic_Serializer.Meta):
        model = Offer
    #def get_allDiscountProducts(self, obj):
        #return ProductSerializer(obj.get_discountProducts(), many=True).data
    #def get_allConditionProducts(self, obj):
        #return ProductSerializer(obj.get_conditionProducts(), many=True).data
    #def get_allsellpoints(self, obj):
        #return SellpointSerializer(obj.get_sellpoints(), many=True).data



########################################################
########################################################
class sv__Sellpoint__TemplateView(Generic__TemplateView):
    template_name = "sv__Sellpoint__TemplateView.html"


########################################################
########################################################
class Sellpoint__ApiView(Generic__ApiView):
    permissions = False
    def get_serializers(self, request):
        if request.GET.get('api') == 'barcodeScanner':
            key = request.POST.get('BarCode')
            ticket = Ticket.objects.filter(key=request.POST.get('key'), status='PENDIENTE').first()
            if ticket:
                ticket.scanner()
            return JsonResponse({
                'ticket': TicketSerializer(ticket).data,
            }, safe=False)
        if request.GET.get('api') == 'getStates':
            sellpoints = Sellpoint().getMySellpoints(request.user)
            productattributes = ProductAttributes.objects.filter( sellpoint__in=sellpoints.all(), active=True, is_active=True, product__menu__active=True, product__menu__is_active=True ).distinct()
            menu = []
            for productattribute in productattributes:
                for pmenu in productattribute.product.menu.all():
                    if not pmenu.pk in menu:
                        menu.append(pmenu.pk)
            return JsonResponse({
                'sellpoints': SellpointSerializer( sellpoints , many=True ).data,
                'productAttributes': ProductAttributesSerializer( productattributes, many=True ).data,
                'menus': MenuSerializer( Menu.objects.filter(pk__in = menu), many=True ).data ,
                'offers': OfferSerializer( Offer.objects.filter( organization = request.user.organization, active=True, is_active=True ), many=True ).data,
                'tickets': TicketSerializer(  Ticket.objects.filter(cut__final_time__isnull=True, sellpoint__in=sellpoints.all() ), many=True ).data
            }, safe=False)
        if request.GET.get('api') == 'getBarCode':
            return JsonResponse({'ticket': TicketSerializer(Ticket().new( ticket = json.loads(request.POST.get('ticket')) )).data}, safe=False)
        if request.GET.get('api') == 'makeCut':
            cut = Sellpoint.objects.get(id=json.loads(request.POST.get('sellpoint'))['id']).getCut().makeCut()
            return JsonResponse({'cut': CutSerializer(cut).data})


########################################################
########################################################
class SVbarcodeScanner__TemplateView(Generic__TemplateView):
    template_name = "SVbarcodeScanner__TemplateView.html"
