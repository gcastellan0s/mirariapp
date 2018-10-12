# -*- coding: utf-8 -*-
from mirari.mirari.templatetags.mirari_tags import *
from mirari.INT.models import Notification

@register.filter
def get_user_notifications(user):
	return Notification().get_user_notification(user)