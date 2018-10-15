# -*- coding: utf-8 -*-
from django import template
from django.conf import settings

from mirari.INT.models import Notification

register = template.Library()

@register.filter
def get_user_notifications(user):
	return Notification().get_user_notification(user)