from mirari.mirari.urls import *
from .views import *
from .vars import *

app_name = APP

urlpatterns = [
    path('detail/NotificationDetailView/<slug:uuid>/', login_required(Notification__DetailView.as_view()), name='Notification__DetailView'),

    path('list/EmployeDirectoryListView/', login_required(EmployeDirectory__ListView.as_view()), name='EmployeDirectory__ListView'),
]