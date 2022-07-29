"""
Celery config file

https://docs.celeryproject.org/en/stable/django/first-steps-with-django.html

"""
from __future__ import absolute_import
import os
from celery import Celery

# this code copied from manage.py
# set the default Django settings module for the 'celery' app.
from django.conf import settings

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'svfoundation.settings')

# you change change the name here
app = Celery("svfoundation")

# read config from Django settings, the CELERY namespace would make celery
# config keys has `CELERY` prefix
app.config_from_object('django.conf:settings', namespace='CELERY')

# load tasks.py in django apps
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)
