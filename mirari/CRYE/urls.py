from mirari.mirari.urls import *
from .views import *
from .vars import *

app_name = APP

urlpatterns = [
    path('CRYE/SiebelUnblock/', SiebelUnblock__SiebelUnblock__TemplateView.as_view(), name='SiebelUnblock__SiebelUnblock__TemplateView'),
]
