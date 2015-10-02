from __future__ import absolute_import
import os

from celery import Celery
from django.conf import settings


# Indicate Celery to use the default Django settings module
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'expense_manager.settings')

app = Celery('expense_manager', backend='amqp', broker='amqp://')
app.config_from_object('django.conf:settings')
# This line will tell Celery to autodiscover all your tasks.py that are in your app folders
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)