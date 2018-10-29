from __future__ import absolute_import, unicode_literals
from celery import shared_task

@shared_task
def send_mail_task(instance):
	instance.send_mail()
	return 'send_mail_task OK'