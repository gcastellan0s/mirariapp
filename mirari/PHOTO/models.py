# -*- coding: utf-8 -*-
from mirari.mirari.models import *
from .vars import *


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
}
def path_photo_file(self, filename):
	upload_to = "companys/%s_%s/PHOTO/%s" % (self.organization.id, self.organization.code, filename)
	return upload_to
class Photo(Model_base):
	organization = models.ForeignKey('mirari.Organization', blank=True, null=True, on_delete=models.CASCADE, related_name='+',)
	file = ProcessedImageField(upload_to=path_photo_file, blank=True, null=True, verbose_name="Fotografía", options={'quality': 100}, help_text="Menor a 12mb")
	description = models.CharField('Descripción de la foto', max_length=250)
	creation_date = models.DateTimeField(auto_now_add=True)
	#is_active = models.BooleanField(default=True)
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