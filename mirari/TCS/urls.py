from mirari.mirari.urls import *
from .views import *
from .vars import *

app_name = APP

urlpatterns = [
    path('api/OrderServiceApiView/<slug:app>/<slug:action>/<slug:model>/', OrderService__ApiView.as_view(), name='OrderService__ApiView'),
]
