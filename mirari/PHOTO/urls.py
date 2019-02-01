from mirari.mirari.urls import *
from .views import *
from .vars import *

app_name = APP

urlpatterns = [
    path('search/', Search__TemplateView.as_view(), name='Search__TemplateView'),
]