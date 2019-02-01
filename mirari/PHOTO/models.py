# -*- coding: utf-8 -*-
from mirari.mirari.models import *
from .vars import *

from taggit.managers import TaggableManager

VARS = {
	'NAME':'Categoría',
	'PLURAL':'Categorías',
	'MODEL':'Category',
	'NEW':'NUEVA',
	'NEW_GENDER': 'una nueva',
	'THIS': 'esta',
	'APP':APP,
	'LIST': [
		{
			'field': 'name',
			'title': 'Nombre de la categoria',
		},
	],
}
class Category(Model_base):
	organization = models.ForeignKey('mirari.Organization', blank=True, null=True, on_delete=models.CASCADE, related_name='+',)
	name = models.CharField('Nombre de la categoria', max_length=250)
	VARS = VARS
	class Meta(Model_base.Meta):
		verbose_name = VARS['NAME']
		verbose_name_plural = VARS['PLURAL']
		permissions = permissions(VARS)
	def __str__(self):
		return str(self.name)



VARS = {
	'NAME':'Foto',
	'PLURAL':'Fotos',
	'MODEL':'Photo',
	'NEW':'NUEVA',
	'NEW_GENDER': 'una nueva',
	'THIS': 'esta',
	'APP':APP,
	'LIST': [
		{
			'field': 'property_get_file',
			'title': 'Imagen',
		},
		{
			'field': 'property_get_description',
			'title': 'Descripcion',
		},
		{
			'field': 'property_get_creation_date',
			'title': 'Fecha de creación',
		},
	],
	'SELECTQ': {
		'categories': {
			'model': ['PHOTO', 'Category'],
			'plugin': 'select2',
			'query': [
				(
					('organization__pk', 'self.request.session.get("organization")'),
				),
			],
		},
	},
}
def path_photo_file(self, filename):
	upload_to = "companys/%s_%s/PHOTO/%s" % (self.organization.id, self.organization.code, filename)
	return upload_to
class Photo(Model_base):
	organization = models.ForeignKey('mirari.Organization', blank=True, null=True, on_delete=models.CASCADE, related_name='+',)
	file = ProcessedImageField(upload_to=path_photo_file, blank=True, null=True, verbose_name="Imagen", options={'quality': 65}, help_text="Menor a 12mb")
	categories = models.ManyToManyField('Category', verbose_name="Categorias")
	description = models.CharField('Descripción de la foto', max_length=250, help_text="Menos de 250 caracteres")
	creation_date = models.DateTimeField(auto_now_add=True)
	tags = TaggableManager(verbose_name='Tags', blank=True)
	is_active = models.BooleanField(default=True, editable=False)
	publica = models.BooleanField(default=False, help_text="Indica si tu imagen tendra una marca de agua que evite que la roben.")
	VARS = VARS
	class Meta(Model_base.Meta):
		verbose_name = VARS['NAME']
		verbose_name_plural = VARS['PLURAL']
		permissions = permissions(VARS)
	def __str__(self):
		return str(self.pk)
	#######
	def get_description(self):
		return self.description
	def get_creation_date(self):
		return self.render_datetime(self.creation_date)
	def get_file(self):
		return 'Ya casi lo termino'


VARS = {
	'NAME':'Busqueda',
	'PLURAL':'Busquedas',
	'MODEL':'Search',
	'NEW':'NUEVA',
	'NEW_GENDER': 'una nueva',
	'THIS': 'esta',
	'APP':APP,
	'EXCLUDE_PERMISSIONS':['all',],
}
class Search(Model_base):
    VARS = VARS
    class Meta(Model_base.Meta):
        verbose_name = VARS['NAME']
        verbose_name_plural = VARS['PLURAL']
        permissions = permissions(VARS)
    def __str__(self):
        return '{0}'.format(self.VARS['NAME'])
