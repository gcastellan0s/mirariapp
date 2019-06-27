from mirari.mirari.urls import *
from django.views.generic.base import RedirectView

from .views import *
from .vars import *

app_name = APP

urlpatterns = [
    path('sv/', sv__Sellpoint__TemplateView.as_view(), name='sv__Sellpoint__TemplateView'),
    path('api/SellpointApiView/<slug:app>/<slug:action>/<slug:model>/', Sellpoint__ApiView.as_view(), name='Sellpoint__ApiView'),
    path('SVbarcodeScanner/', SVbarcodeScanner__TemplateView.as_view(), name='SVbarcodeScanner__TemplateView'),
    path('TicketInvoiceMX/', TicketInvoiceMX__TemplateView.as_view(), name='TicketInvoiceMX__TemplateView'),
    path('GetTicketQR/', GetTicketQR__TemplateView.as_view(), name='GetTicketQR__TemplateView'),
]