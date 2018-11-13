from mirari.mirari.urls import *
from .views import *
from .vars import *

app_name = APP

urlpatterns = [
    path('BASE/FunctionName/', FunctionName__TypeView.as_view(), name='FunctionName__TypeView'),
]
