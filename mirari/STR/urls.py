from mirari.mirari.urls import *
from .views import *
from .vars import *

app_name = APP

urlpatterns = [
    path('list/InventoryOrder/', login_required(InventoryOrder__ListView.as_view()), name='InventoryOrder__ListView'),
]   