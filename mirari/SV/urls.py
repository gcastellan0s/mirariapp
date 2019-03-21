from mirari.mirari.urls import *
from .views import *
from .vars import *

app_name = APP

urlpatterns = [
    path('sv/', sv__Sellpoint__TemplateView.as_view(), name='sv__Sellpoint__TemplateView'),
    path('api/SellpointApiView/<slug:app>/<slug:action>/<slug:model>/', Sellpoint__ApiView.as_view(), name='Sellpoint__ApiView'),
    path('CutDetailView/<slug:app>/<int:pk>/<slug:model>/', Cut__DetailView.as_view(), name='Cut__DetailView'),
    path('SVbarcodeScanner/', SVbarcodeScanner__TemplateView.as_view(), name='SVbarcodeScanner__TemplateView'),
]
