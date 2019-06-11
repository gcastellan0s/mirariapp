# -*- coding: utf-8 -*-
from mirari.mirari.views import *
from .models import *
from .vars import *

########################################################
class sv__Sellpoint__TemplateView(Generic__TemplateView):
    template_name = "SV__TemplateView.pug"

########################################################
class SVbarcodeScanner__TemplateView(Generic__TemplateView):
    template_name = "BarcodeScanner__TemplateView.pug"
    def proccess_context(self, context):
        context['code'] = self.request.GET.get('code')
        return context

########################################################
class Sellpoint__ApiView(Generic__ApiView):
    permissions = False
    def get_serializers(self, request):
        Action = request.GET.get('api')
        if Action == 'barcodeScanner':
            ticket = Ticket.objects.filter(key=request.POST.get('barcode'),sellpoint__organization__code=request.POST.get('code')).first()
            if ticket:
                ticket = ticket.scanner()
            return JsonResponse({'ticket': TicketSerializer(ticket).data}, safe=False)
        if Action == 'getBarCode':
            return JsonResponse({'ticket':TicketSerializer(Ticket().new(ticket=json.loads(request.POST.get('ticket')))).data}, safe=False)
        if Action == 'getStates':
            sellpoints = Sellpoint().getMySellpoints(request.user)
            productattributes = ProductAttributes.objects.filter(sellpoint__in=sellpoints.filter(vendors=request.user).all(),active=True,is_active=True,product__menu__active=True,product__menu__is_active=True,product__is_active=True,product__active=True).distinct().order_by('price')
            menu = []
            for productattribute in productattributes:
                for pmenu in productattribute.product.menu.all():
                    for menuAncestors in pmenu.get_ancestors(ascending=False, include_self=True):
                        if not menuAncestors.pk in menu:
                            menu.append(menuAncestors.pk)
            return JsonResponse({
                'sellpoints':SellpointSerializer(sellpoints,many=True).data,
                'productAttributes':ProductAttributesSerializer(productattributes,many=True).data,
                'menus':MenuSerializer(Menu.objects.filter(pk__in=menu).order_by('tree_id', 'level'),many=True).data ,
                'offers':OfferSerializer(Offer.objects.filter(organization=request.user.organization,active=True,is_active=True),many=True).data,
                'tickets':TicketSerializer(Ticket.objects.filter(cut__final_time__isnull=True, sellpoint__in=Sellpoint().getMySellpointsCasher(request.user).all()),many=True).data,
            }, safe=False)
        if Action == 'getTicket':
            return JsonResponse({'ticket':TicketSerializer(Ticket.objects.get(id=request.POST.get('ticket')), read_only=True).data}, safe=False)
        if Action == 'makeCut':
            cut = Sellpoint.objects.get(id=json.loads(request.POST.get('sellpoint'))['id']).getCut()
            #cut = cut.makeCut()
            cut = Cut.objects.get(id=2539)
            if cut:
                return JsonResponse({'cut': CutSerializer(cut).data}, safe=False)
            else:
                return JsonResponse({'cut': CutSerializer(Sellpoint.objects.get(id=json.loads(request.POST.get('sellpoint'))['id']).lastCut()).data}, safe=False)
        if Action == 'getCut':
            return JsonResponse({'cut': CutSerializer(Cut.objects.get(id=request.POST.get('cut')), read_only=True).data}, safe=False)
        if Action == 'getClients':
            return JsonResponse({'clients':ClientSerializer(Client.objects.filter(organization=request.user.organization,active=True,is_active=True).filter(Q(name__icontains=request.GET.get('query'))|Q(phone__icontains=request.GET.get('query'))|Q(rfc__icontains=request.GET.get('query'))|Q(email__icontains=request.GET.get('query'))|Q(uid__icontains=request.GET.get('query'))).distinct()[0:50],many=True).data},safe=False)
        if Action == 'getClient':
            return JsonResponse({'client':ClientDetailsSerializer(Client.objects.get(organization=request.user.organization,active=True,is_active=True,id=request.POST.get('id'))).data,},safe=False)
        if Action == 'changeStatusTicket':
            Ticket.objects.filter(id=request.POST.get('id')).update(status=request.POST.get('status'))
            return JsonResponse({'ticket':TicketSerializer(Ticket.objects.get(id=request.POST.get('id')), read_only=True).data},safe=False)
        if Action == 'changeRasuradoCut':
            cuts = Cut.objects.filter(id__in=json.loads(request.POST.get('cutsIds')))
            for cut in cuts:
                cut.makeRasurado(request.POST.get('rasurado'))
            return JsonResponse({'rasurado':True})