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
class CutProductSerializer(serializers.Serializer):
    product = serializers.IntegerField()
    productName = serializers.CharField(max_length=250)
    quantity = serializers.IntegerField()
    price = serializers.FloatField()
    total = serializers.FloatField()
    iva = serializers.FloatField()
    ieps = serializers.FloatField()
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
########################################################
class CutSerializer(Base_Serializer):
    propertyGetTotalMoney = serializers.ReadOnlyField(source='getTotalMoney')
    propertyGetIvaMoney = serializers.ReadOnlyField(source='getIvaMoney')
    propertyGetIepsMoney = serializers.ReadOnlyField(source='getIepsMoney')
    propertyGetSubtotalMoney = serializers.ReadOnlyField(source='getSubtotalMoney')
    propertyGetLenTickets = serializers.ReadOnlyField(source='getLenTickets')
    propertyGetFaltanteMoney = serializers.ReadOnlyField(source='getFaltanteMoney')
    propertyGetLenFaltante = serializers.ReadOnlyField(source='getLenFaltante')
    products = serializers.SerializerMethodField()
    class Meta(Basic_Serializer.Meta):
        model = Cut
    def get_products(self, obj):
        return CutProductSerializer(obj.getCutProducts(), many=True, read_only=True).data
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
class ClientProfileSerializer(Base_Serializer):
    class Meta(Basic_Serializer.Meta):
        model = ClientProfile
########################################################
class ClientSerializer(Base_Serializer):
    clientProfile = serializers.SerializerMethodField()
    class Meta(Basic_Serializer.Meta):
        model = Client
    def get_clientProfile(self, obj):
        return ClientProfileSerializer(obj.clientProfile, read_only=True).data
########################################################
class TicketsSerializer(Base_Serializer):
    class Meta(Basic_Serializer.Meta):
        model = Ticket
class ClientDetailsSerializer(Base_Serializer):
    clientProfile = serializers.SerializerMethodField()
    tickets = serializers.SerializerMethodField()
    class Meta(Basic_Serializer.Meta):
        model = Client
    def get_clientProfile(self, obj):
        return ClientProfileSerializer(obj.clientProfile, read_only=True).data
    def get_tickets(self, obj):
        return TicketsSerializer(obj.getTickets(), many=True).data

########################################################
########################################################
class sv__Sellpoint__TemplateView(Generic__TemplateView):
    template_name = "sv__Sellpoint__TemplateView.html"

########################################################
########################################################
class Sellpoint__ApiView(Generic__ApiView):
    permissions = False
    def get_serializers(self, request):
        #try:
            if request.GET.get('api') == 'barcodeScanner':
                ticket = Ticket.objects.filter(key=request.POST.get('barcode'), sellpoint__organization__code=request.POST.get('code')).first()
                if ticket:
                    ticket = ticket.scanner()
                return JsonResponse({'ticket': TicketSerializer(ticket).data}, safe=False)
            if request.GET.get('api') == 'getStates':
                sellpoints = Sellpoint().getMySellpointsVendor(request.user)
                productattributes = ProductAttributes.objects.filter( sellpoint__in=sellpoints.all(), active=True, is_active=True, product__menu__active=True, product__menu__is_active=True ).distinct().order_by('price')
                menu = []
                for productattribute in productattributes:
                    for pmenu in productattribute.product.menu.all():
                        if not pmenu.pk in menu:
                            menu.append(pmenu.pk)
                return JsonResponse({
                    'sellpoints': SellpointSerializer( sellpoints , many=True ).data,
                    'productAttributes': ProductAttributesSerializer( productattributes, many=True ).data,
                    'menus': MenuSerializer( Menu.objects.filter(pk__in = menu).order_by('name'), many=True ).data ,
                    'offers': OfferSerializer( Offer.objects.filter( organization = request.user.organization, active=True, is_active=True ), many=True ).data,
                    'tickets': TicketSerializer( Ticket.objects.filter(cut__final_time__isnull=True, sellpoint__in=Sellpoint().getMySellpointsCasher(request.user).all() ), many=True ).data,
                }, safe=False)
            if request.GET.get('api') == 'getClients':
                return JsonResponse({'clients': ClientSerializer(Client.objects.filter(organization=request.user.organization,active=True,is_active=True).filter(Q(name__icontains=request.GET.get('query'))|Q(phone__icontains=request.GET.get('query'))|Q(rfc__icontains=request.GET.get('query'))|Q(email__icontains=request.GET.get('query'))).distinct()[0:50], many=True ).data}, safe=False)
            if request.GET.get('api') == 'getClient':
                client = Client.objects.get(organization=request.user.organization, active=True, is_active=True, id=request.POST.get('id'))
                return JsonResponse({
                    'client': ClientDetailsSerializer(client).data,
                }, safe=False)
            if request.GET.get('api') == 'getBarCode':
                return JsonResponse({'ticket': TicketSerializer(Ticket().new( ticket = json.loads(request.POST.get('ticket')) )).data}, safe=False)
            if request.GET.get('api') == 'makeCut':
                cut = Sellpoint.objects.get(id=json.loads(request.POST.get('sellpoint'))['id']).getCut().makeCut()
                return JsonResponse({'cut': CutSerializer(cut).data})
        #except Exception as e:
            #print(str(e))
            #return JsonResponse({'error':str(e)})

########################################################
########################################################
class SVbarcodeScanner__TemplateView(Generic__TemplateView):
    template_name = "SVbarcodeScanner__TemplateView.html"
    def proccess_context(self, context):
        context['code'] = self.request.GET.get('code')
        return context

########################################################
class Cut__DetailView(Generic__DetailView):
    template_name = "Cut__DetailView.html"