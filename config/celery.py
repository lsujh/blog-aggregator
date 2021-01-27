from __future__ import absolute_import
import os
from celery import Celery
from celery.schedules import crontab

from django.conf import settings

os.environ.setdefault('DJANGO_SETTINGS_MODULE','config.settings')
app = Celery('config')
app.conf.timezone = 'UTC'
app.config_from_object("django.conf:settings", namespace="CELERY")
app.autodiscover_tasks(settings.INSTALLED_APPS)

app.conf.beat_schedule = {
    'aggregator-task': {
        'task': 'aggregator.tasks.news_rss',
        'schedule': crontab(minute=0, hour=0), #crontab()
    },
}

@app.task(bind=True)
def debug_task(self):
    print("Request: {0!r}".format(self.request))