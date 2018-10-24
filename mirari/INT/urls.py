from mirari.mirari.urls import *
from .views import *
from .vars import *

app_name = APP

urlpatterns = [
    path('detail/NotificationDetailView/<slug:uuid>/', Notification__DetailView.as_view(), name='Notification__DetailView'),

    path('list/EmployeDirectoryListView/', EmployeDirectory__ListView.as_view(), name='EmployeDirectory__ListView'),
]