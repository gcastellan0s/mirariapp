from mirari.mirari.urls import *
from .views import *
from .vars import *

app_name = APP

urlpatterns = [
    path('sv/', sv__Sellpoint__TemplateView.as_view(), name='sv__Sellpoint__TemplateView'),
    path('api/SellpointApiView/<slug:app>/<slug:action>/<slug:model>/', Sellpoint__ApiView.as_view(), name='Sellpoint__ApiView'),
]
