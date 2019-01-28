# -*- coding: utf-8 -*-
from django import template
from mirari.mirari.vars import *
from mirari.mirari.models import *
from django.conf import settings

from mirari.PHOTO.models import Photo

register = template.Library()

@register.filter
def get_photos(obj):
	return Photo.objects.all()