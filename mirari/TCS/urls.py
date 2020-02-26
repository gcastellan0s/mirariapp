from mirari.mirari.urls import *
from .views import *
from .vars import *

app_name = APP

urlpatterns = [
    path('calendar/', calendar__OrderService__TemplateView.as_view(), name='calendar__OrderService__TemplateView'),
    path('manuales-usuario/', manuales_usuario__OrderService__TemplateView.as_view(), name='manuales_usuario__OrderService__TemplateView'),
    path('manuales-iconfield/', manuales_iconfield__OrderService__TemplateView.as_view(), name='manuales_iconfield__OrderService__TemplateView'),
    path('order-service-report/', OrderServiceReport__TemplateView.as_view(), name='OrderServiceReport__TemplateView'),
]
