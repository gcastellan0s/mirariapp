# -*- coding: utf-8 -*-
from mirari.mirari.views import *
from .models import *
from .vars import *

########################################################
class sv__Sellpoint__TemplateView(Generic__TemplateView):
	template_name = "SV__TemplateView.pug"

########################################################
class TicketInvoiceMX__TemplateView(Generic__TemplateView):
	template_name = "TicketInvoiceMX__TemplateView.pug"

########################################################
class GetTicketQR__TemplateView(Generic__TemplateView):
	template_name = "GetTicketQR__TemplateView.pug"

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
		if Action == 'getOnlineStatus':
			return JsonResponse({'api':'ok'}, safe=False)
		elif Action == 'getReport':
			sellpointgroup = SellpointGroups.objects.get(pk=request.POST.get('sellpointgroup'))
			cut = Cut.objects.filter(sellpoint__in=sellpointgroup.sellpoints.all(), final_time__year=request.POST.get('year'), final_time__month=request.POST.get('month'), final_time__day=request.POST.get('day'))
			return JsonResponse({'day':request.POST.get('day'), 'cuts':CutReportSerializer(cut, many=True).data}, safe=False)
		elif Action == 'barcodeScanner':
			ticket = Ticket.objects.filter(key=request.POST.get('barcode'),sellpoint__organization__code=request.POST.get('code')).first()
			if ticket:
				ticket = ticket.scanner()
			return JsonResponse({'ticket': TicketSerializer(ticket).data}, safe=False)
		elif Action == 'getBarCode':
			return JsonResponse({'ticket':TicketSerializer(Ticket().new(ticket=json.loads(request.POST.get('ticket')))).data}, safe=False)
		elif Action == 'getStates':
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
				'tickets':TicketSerializer(Ticket.objects.filter(cut__final_time__isnull=True, sellpoint__in=Sellpoint().getMySellpoints(request.user).all()).exclude(cut__isnull=True), many=True).data,
			}, safe=False)
		elif Action == 'getTicket':
			return JsonResponse({'ticket':TicketSerializer(Ticket.objects.get(id=request.POST.get('ticket')), read_only=True).data}, safe=False)
		elif Action == 'getProductAttribute':
			return JsonResponse({'getProductAttribute':ProductAttributesSerializer(ProductAttributes.objects.get(id=request.POST.get('productAttribute')), read_only=True).data}, safe=False)
		elif Action == 'saveProductAttribute':
			productAttributes = ProductAttributes.objects.get(id=request.POST.get('id'))
			productAttributes.price = request.POST.get('price')
			productAttributes.quantity = request.POST.get('quantity')
			productAttributes.bar_code = request.POST.get('bar_code')
			if request.POST.get('iva') == 'true':
				productAttributes.iva = True
			else: 
				productAttributes.iva = False
			if request.POST.get('ieps') == 'true':
				productAttributes.ieps = True
			else: 
				productAttributes.ieps = False
			if request.POST.get('is_favorite') == 'true':
				productAttributes.is_favorite = True
			else: 
				productAttributes.is_favorite = False
			if request.POST.get('is_active') == 'true':
				productAttributes.is_active =  True
			else: 
				productAttributes.is_active =  False
			productAttributes.save()
			return JsonResponse({'ProductAttributes':ProductAttributesSerializer(productAttributes, read_only=True).data}, safe=False)
		elif Action == 'makeCut':
			#return JsonResponse({'cut': CutSerializer(Cut.objects.get(id=2691)).data}, safe=False)
			if not request.POST.get('cutID') == 'Actual':
				return JsonResponse({'cut': CutSerializer(Cut.objects.get(id=request.POST.get('cutID'))).data}, safe=False)
			cut = Sellpoint.objects.get(id=json.loads(request.POST.get('sellpoint'))['id']).getCut()
			cut = cut.makeCut()
			if cut:
				return JsonResponse({'cut': CutSerializer(cut).data}, safe=False)
			else:
				return JsonResponse({'cut': CutSerializer(Sellpoint.objects.get(id=json.loads(request.POST.get('sellpoint'))['id']).lastCut()).data}, safe=False)
		elif Action == 'getRangeCuts':
			cuts = Cut.objects.filter(sellpoint__organization__code=request.POST.get('organization'), id__range=(request.POST.get('init'), request.POST.get('final'))).exclude(sellpoint__id__in=[14,18]).order_by('sellpoint','id')
			return JsonResponse({'cuts': CutIDSerializer(cuts, many=True).data}, safe=False)
		elif Action == 'getCut':
			return JsonResponse({'cut': CutSerializer(Cut.objects.get(id=request.POST.get('cut')), read_only=True).data}, safe=False)
		elif Action == 'getClients':
			return JsonResponse({'clients':ClientSerializer(Client.objects.filter(organization=request.user.organization,active=True,is_active=True).filter(Q(name__icontains=request.GET.get('query'))|Q(phone__icontains=request.GET.get('query'))|Q(uid__icontains=request.GET.get('query'))).distinct()[0:10],many=True).data},safe=False)
		elif Action == 'getClient':
			return JsonResponse({'client':ClientDetailsSerializer(Client.objects.get(organization=request.user.organization,active=True,is_active=True,id=request.POST.get('id'))).data,},safe=False)
		elif Action == 'changeStatusTicket':
			Ticket.objects.filter(id=request.POST.get('id')).update(status=request.POST.get('status'))
			return JsonResponse({'ticket':TicketSerializer(Ticket.objects.get(id=request.POST.get('id')), read_only=True).data},safe=False)
		elif Action == 'changeRasuradoCut':
			cuts = Cut.objects.filter(id__in=json.loads(request.POST.get('cutsIds')))
			for cut in cuts:
				cut.makeRasurado(request.POST.get('rasurado'))
			return JsonResponse({'rasurado':True})
		elif Action == 'makeInvoiceTicket':
			ticket = Ticket.objects.filter(key = request.POST.get('ticket')).first()
			if not ticket:
				return JsonResponse({'message':'No se encontro el ticket'}, status=500)
			filename = ticket.stampTicket(cfdiReceptorRfc=request.POST.get('rfc'), cfdiReceptorNombre=request.POST.get('razonSocial'), cfdiReceptorUsocfdi=request.POST.get('usoCFDI','G03'))
			if not filename:
				return JsonResponse({'message':'Ocurrió un error en el servidor, contacta al administrador'}, status=500)
			hostEmail = HostEmail.objects.filter(module__code=APP, organization=ticket.sellpoint.organization).first()
			if not hostEmail:
				return JsonResponse({'message':'No es posible enviar los archivos por correos, pero se facturó correctamente'}, status=500)
			hostEmail.sendMail(
					subject='RECIBISTE TU FACTURA!', 
					fromEmail=ticket.sellpoint.fiscalDataTickets.contactEmail,
					fromContact=ticket.sellpoint.fiscalDataTickets.contactName,
					toEmail=[request.POST.get('email')], 
					files=[filename+'.xml', filename+'.pdf'], 
					content=mark_safe("""<h5>Recibiste exitosamente tu factura</h5>""")
				)
			return JsonResponse({'message':'Enviamos tu factura a: '+request.POST.get('email')})
		elif Action == 'ChangeTotalTicket':
			ticket = Ticket.objects.get(pk = request.POST.get('ticket'))
			client = ticket.client
			client.balance += ticket.total
			ticket.difference = float(request.POST.get('total')) - ticket.total
			ticket.total = float(request.POST.get('total'))
			client.balance -= ticket.total
			client.save()
			ticket.save()
			return JsonResponse({'message':'ok'})
		return JsonResponse({'message':'Ocurrió un error en el servidor'}, status=500)
