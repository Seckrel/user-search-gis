from __future__ import absolute_import, unicode_literals
from django.conf import settings
import os

from celery import Celery, shared_task

# set the default Django settings module for the 'celery' program.

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'user_search_gis.settings')

app = Celery('user_search_gis', broker="redis://127.0.0.1:6379")

# Using a string here means the worker doesn't have to serialize
# the configuration object to child processes.
# - namespace='CELERY' means all celery-related configuration keys
#   should have a `CELERY_` prefix.
app.config_from_object(settings, namespace='CELERY')

# Load task modules from all registered Django app configs.
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)


@app.task(bind=True)
def debug_task(self):
    print('Request: {0!r}'.format(self.request))


@shared_task(max_retires=3, soft_time_limit=60)
def add(x, y):
    a = x + y
    return a
