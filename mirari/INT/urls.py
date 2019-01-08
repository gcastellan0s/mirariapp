from mirari.mirari.urls import *
from .views import *
from .vars import *

app_name = APP

urlpatterns = [
    path('detail/NotificationDetailView/<slug:uuid>/', login_required(Notification__DetailView.as_view()), name='Notification__DetailView'),
    path('list/EmployeDirectoryListView/', login_required(EmployeDirectory__ListView.as_view()), name='EmployeDirectory__ListView'),
    path('create/InternalMailBox_MailCreateView/<int:pk>/<slug:slug>/<slug:app>/<slug:model>/', login_required(InternalMailBox_Mail__CreateView.as_view()), name='InternalMailBox_Mail__CreateView'),
]