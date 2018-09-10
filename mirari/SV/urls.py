from mirari.mirari.urls import *
from .views import *
from .vars import *

app_name = APP

urlpatterns = [
    path('api/SetSellpointApiView/<slug:app>/<slug:action>/<slug:model>/', SetSellpoint__ApiView.as_view(), name='SetSellpoint__ApiView'),
]
