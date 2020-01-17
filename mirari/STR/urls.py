from mirari.mirari.urls import *
from .views import *
from .vars import *

app_name = APP

urlpatterns = [
    path('InventoryOrderReception/', InventoryOrderReception__TemplateView.as_view(), name='InventoryOrderReception__TemplateView'),
    path('InventoryOrderPicking/', InventoryOrderPicking__TemplateView.as_view(), name='InventoryOrderPicking__TemplateView'),
]   