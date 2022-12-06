from __future__ import absolute_import

import os

from celery import Celery
from celery.schedules import crontab
from django.conf import settings

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "core.settings.dev")
app = Celery("core")
app.conf.enable_utc = True

app.conf.update(timezone="UTC")

app.config_from_object(settings, namespace="CELERY")

# CELERY BEAT SETTINGS
app.conf.beat_schedule = {
    'send-mail-everyday-at-8' : {
        'task' : 'app.tasks.send_all_user_mail.send_all_user_mail',
        'schedule': crontab(hour=14, minute=53),
    }
}

app.autodiscover_tasks()


@app.task(bind=True)
def debug_task(self):
    print(f"Request: {self.request!r}")
