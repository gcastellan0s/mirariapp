# -*- coding: utf-8 -*-
from django.utils.translation import gettext as _
from .viewbase import *

###############################################################################################
###############################################################################################
######### TEMPLATE ################################################################################
class Generic__TemplateView(Base_Template, TemplateView):
    pass
######### Detail ################################################################################
class Generic__DetailView(Base_Detail, DetailView):
    pass
######### LIST ################################################################################
class Generic__ListView(Base_List, ListView):
    pass
######### CREATE ##############################################################################
class Generic__CreateView(Base_Create, CreateView):
    pass
######### UPDATE ##############################################################################
class Generic__UpdateView(Base_Update, UpdateView):
    pass
######### DELETE ##############################################################################
class Generic__DeleteView(Base_Delete, DeleteView):
    pass
######### API ##############################################################################
class Generic__ApiView(Base_Api, APIView):
	pass

###############################################################################################
###############################################################################################
######### AUTH ################################################################################
class login__Organization__TemplateView(Generic__TemplateView):
	template_name = "app/login.html"
	@method_decorator(csrf_exempt)
	def dispatch(self, request, *args, **kwargs):
		if request.user.is_authenticated:
			request.session['organization'] = request.user.organization.pk
			return HttpResponseRedirect(reverse('mirari:dashboard__Organization__TemplateView', args=[]))
		if request.method == 'POST':
			message, token = False, False
			username, password = request.POST.get('username'), request.POST.get('password')
			if validate_email(username):
				user = User.objects.filter(email=username).first()
				if user:
					username = user.username
				else:
					message = 'Usuario o contraseña incorrectos'
			else:
				username = request.POST.get('code') + '__' + username
			if not message:
				access = authenticate(username=username, password=password)
				if access:
					if access.is_active and access.active:
						login(request, access)
					else:
						message = 'Usuario desactivado'
				else:
					message = 'Usuario o contraseña incorrectos'
			return JsonResponse({'message':message,'token':token})
		return super().dispatch(request, *args, **kwargs)

class logout__Organization__TemplateView(Generic__TemplateView):
	def dispatch(self, request, *args, **kwargs):
		logout(self.request)
		return HttpResponseRedirect('/')

###############################################################################################
###############################################################################################
######### DASHBOARD ###########################################################################
class dashboard__Organization__TemplateView(Generic__TemplateView):
	template_name = "app/dashboard.html"
	def dispatch(self, request, *args, **kwargs):
		if not request.user.is_authenticated:
			organization = get_variables(self)['ORGANIZATION']
			self.HTMLPage = HTMLPage.objects.get(organization=organization)
			if self.HTMLPage:
				self.template_name = self.HTMLPage.folder + self.HTMLPage.index
		return super().dispatch(request, *args, **kwargs)
################################################################################################
################################################################################################
########## LIST ################################################################################
class User__ListView(Generic__ListView):
	def list(self):
		extrabuttons = ''
		if self.request.user.has_perm('mirari.Can_Change__Password'):
			extrabuttons = '<a href="{{property_url_password}}" class="btn btn-outline-brand m-btn m-btn--icon m-btn--icon-only m-btn--custom m-btn--pill btn-sm m--margin-right-10" title="Cambiar contraseña"><i class="la la-key"></i></a>'
		return self.render_list(extrabuttons = extrabuttons)
################################################################################################
################################################################################################
########## CREATE ##############################################################################
class User__CreateView(Generic__CreateView):
	def form_valid(self, form):
		form.instance.organization = Organization.objects.get(pk=self.request.session.get('organization'))
		if form.instance.organization.is_root_node():
			code = form.instance.organization.code
		else:
			code = form.instance.organization.get_root().code
		form.instance.username = code + '__' + form.instance.visible_username
		form.instance.set_password(form.instance.visible_username)
		form.save()
		return super().form_valid(form)
################################################################################################
################################################################################################
########## UPDATE ##############################################################################
class User__UpdateView(Generic__UpdateView):
	def form_valid(self, form):
		form.instance.organization = Organization.objects.get(pk=self.request.session.get('organization'))
		if form.instance.organization.is_root_node():
			code = form.instance.organization.code
		else:
			code = form.instance.organization.get_root().code
		form.instance.username = code + '__' + form.instance.visible_username
		form.save()
		return super().form_valid(form)
class UserPassword__UpdateView(Generic__UpdateView):
	def get_form_class(self):
		class Form(Basic_Form):
			new_password = forms.CharField(widget=forms.PasswordInput(), label='Nueva contraseña', help_text='Ingresa una nueva contraseña')
			class Meta(Basic_Form.Meta):
				model = self.model
				fields = ('new_password',)
		return Form
	def form_valid(self, form):
		form.instance.set_password(form.cleaned_data['new_password'])
		form.save()
		return super().form_valid(form)
	def get_success_url(self):
		if self.request.user.has_perm('mirari.Can_Change__Password'):
			return self.model().url_list()
		else:
			return HttpResponseRedirect('/')
	def proccess_context(self, context):
		if not self.request.user.has_perm('mirari.Can_Change__Password'):
			if not self.request.user.pk == self.kwargs['pk']:
				raise PermissionDenied
			context['breadcrumbs'] = ' '
		context['hide_extra_submmit'] = True
		context['rules'] = """
			new_password: {
				required: 1,
				minlength: 6,
			},
		"""
		return context

class GetUser__ApiView(Generic__ApiView):
	def get_objects(self):
		class ApiSerializer(Base_Serializer):
			pass
		ApiSerializer.Meta.model = self.model
		return ApiSerializer(self.request.user)

class ChangeOrganization__ApiView(Generic__ApiView):
	def actions(self, request, *args, **kwargs):
		request.session['organization'] = self.object.pk
		if request.user.is_superuser:
			request.user.organization = self.object
			request.user.save()
		return True
