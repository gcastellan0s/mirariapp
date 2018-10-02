from mirari.mirari.urls import *
from .views import *
from .vars import *

app_name = APP

urlpatterns = [
    path('notification/<slug:uuid>/', Notification__TemplateView.as_view(), name='Notification__TemplateView'),
]