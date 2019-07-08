from mirari.mirari.urls import *
from .views import *
from .vars import *

app_name = APP

urlpatterns = [
    path('prices/', prices__TemplateView.as_view(), name='prices__TemplateView'),
]