from django.urls import path
from django.contrib.auth.decorators import login_required, permission_required
from .views import *
from .vars import *

app_name = APP

urlpatterns = [

	path('login/', login__Organization__TemplateView.as_view(), name='login__Organization__TemplateView'),
	path('logout/', logout__Organization__TemplateView.as_view(), name='logout__Organization__TemplateView'),
	path('', dashboard__Organization__TemplateView.as_view(), name='dashboard__Organization__TemplateView'),

	path('list/UserListView/<slug:app>/<slug:model>/', login_required(User__ListView.as_view()), name='User__ListView'),
	path('create/UserCreateView/<slug:app>/<slug:model>/', login_required(User__CreateView.as_view()), name='User__CreateView'),
	path('update/UserUpdateView/<slug:app>/<int:pk>/<slug:model>/', login_required(User__UpdateView.as_view()), name='User__UpdateView'),
	path('delete/UserPasswordUpdateView/<slug:app>/<int:pk>/<slug:model>/', login_required(UserPassword__UpdateView.as_view()), name='UserPassword__UpdateView'),
	path('api/GetUserApiView/<slug:app>/<slug:action>/<slug:model>/', GetUser__ApiView.as_view(), name='GetUser__ApiView'),
	path('api/ChangeOrganizationApiView/<slug:app>/<slug:model>/', ChangeOrganization__ApiView.as_view(), name='ChangeOrganization__ApiView'),

	path('glist/<slug:app>/<slug:model>/', login_required(Generic__ListView.as_view()), name='Generic__ListView'),
	path('gcreate/<slug:app>/<slug:model>/', login_required(Generic__CreateView.as_view()), name='Generic__CreateView'),
	path('gupdate/<slug:app>/<int:pk>/<slug:model>/', login_required(Generic__UpdateView.as_view()), name='Generic__UpdateView'),
	path('gdelete/<slug:app>/<int:pk>/<slug:model>/', login_required(Generic__DeleteView.as_view()), name='Generic__DeleteView'),
	path('gapi/<slug:app>/<slug:action>/<slug:model>/', login_required(Generic__ApiView.as_view()), name='Generic__ApiView'),
	
]
