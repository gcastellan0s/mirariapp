from mirari.mirari.urls import *
from .views import *
from .vars import *

app_name = APP

urlpatterns = [
    path('InventoryOrder/', InventoryOrder__TemplateView.as_view(), name='InventoryOrder__TemplateView'),
]   