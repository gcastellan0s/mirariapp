# -*- coding: utf-8 -*-
from mirari.mirari.models import *
from .vars import *


VARS = {
	'NAME':'FOTO',
	'PLURAL':'FOTOS',
	'MODEL':'Photo',
	'NEW':'NUEVA',
	'NEW_GENDER': 'una nueva',
	'THIS': 'esta',
	'APP':APP,
}
def path_photo_file(self, filename):
	upload_to = "companys/%s_%s/PHOTO/%s" % (self.organization.id, self.organization.slug, filename)
	return upload_to
class Photo(Model_base):
    organization = models.ForeignKey('mirari.Organization', blank=True, null=True, on_delete=models.CASCADE, related_name='+',)
    file = ProcessedImageField(upload_to=path_system, blank=True, null=True, verbose_name="Fotografía", options={'quality': 100}, help_text="Menor a 12mb")
    description = models.CharField('Descripción de la foto', max_length=250)
    creation_date = models.DateTimeField(auto_now_add=True)
    #is_active = models.BooleanField(default=True)
    VARS = VARS
    class Meta(Model_base.Meta):
        verbose_name = VARS['NAME']
        verbose_name_plural = VARS['PLURAL']
        permissions = permissions(VARS)
        def __str__(self):
            return self.file