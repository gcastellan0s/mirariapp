from mirari.mirari.urls import *
from .views import *
from .vars import *

app_name = APP

urlpatterns = [
    path('list/Product/', login_required(Product__ListView.as_view()), name='Product__ListView'),
    path('list/InventoryOrder/', login_required(InventoryOrder__ListView.as_view()), name='InventoryOrder__ListView'),
    path('create/InventoryOrder/', login_required(InventoryOrder__CreateView.as_view()), name='InventoryOrder__CreateView'),
    path('update/InventoryOrder/', login_required(InventoryOrder__UpdateView.as_view()), name='InventoryOrder__UpdateView'),
    path('api/InventoryApi/<slug:app>/<slug:model>/', Inventory__ApiView.as_view(), name='Inventory__ApiView'),
]   