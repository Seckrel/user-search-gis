from __future__ import absolute_import, unicode_literals
import os
from celery import Celery, shared_task
from celery.utils.log import get_task_logger
from celery.schedules import crontab
from django.conf import settings

# set the default Django settings module for the 'celery' program.

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'user_search_gis.settings')

app = Celery('user_search_gis', broker="redis://127.0.0.1:6379")
app.conf.enable_utc = False

# Using a string here means the worker doesn't have to serialize
# the configuration object to child processes.
# - namespace='CELERY' means all celery-related configuration keys
#   should have a `CELERY_` prefix.
app.config_from_object('django.conf:settings', namespace='CELERY')

# Load task modules from all registered Django app configs.
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)
logger = get_task_logger(__name__)

app.conf.beat_schedule = {
    'wish_birthday_to_users': {
        'task': 'user.tasks.wish_by_email',
        'schedule': crontab(hour=11, minute=16),
    },
}


@app.task(bind=True)
def debug_task(self):
    print('Request: {0!r}'.format(self.request))


@shared_task(max_retires=3, soft_time_limit=60)
def add(x, y):
    a = x + y
    return a
