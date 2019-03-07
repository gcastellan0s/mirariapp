from mirari.mirari.urls import *
from .views import *
from .vars import *

app_name = APP

urlpatterns = [
    path('SiebelUnblock/', SiebelUnblock__SiebelUnblock__TemplateView.as_view(), name='SiebelUnblock__SiebelUnblock__TemplateView'),
    path('WalletCredit/<slug:app>/<slug:model>/', WalletCredit__TemplateView.as_view(), name='WalletCredit__TemplateView'),
    path('TablaAmortizacion/<slug:app>/<int:pk>/<slug:model>/', TablaAmortizacion__TemplateView.as_view(), name='TablaAmortizacion__TemplateView'),
]
