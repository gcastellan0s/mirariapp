from mirari.mirari.urls import *
from .views import *
from .vars import *

app_name = APP

urlpatterns = [
    path('Receipts/', Receipts__TemplateView.as_view(), name='Receipts__TemplateView'),
]