from __future__ import absolute_import, unicode_literals
from celery import shared_task
from django.apps import apps

@shared_task
def send_mail_task(app=None, model=None):
	instance = apps.get_model(app, model)
	instance().send_mail()
	return 'send_mail_task OK'