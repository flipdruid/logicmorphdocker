from __future__ import absolute_import, unicode_literals
import os

from celery import Celery
from django.conf import settings

os.environ.setdefault('DJANGO_SETTINGS_MODULE','core.settings.dev')
app = Celery('core')
app.conf.enable_utc=True

app.conf.update(timezone='UTC')

app.config_from_object(settings, namespace='CELERY')

#CELERY BEAT SETTINGS
app.conf.beat_schedule= {
    
}


app.autodiscover_tasks()

@app.task(bind=True)
def debug_task(self):
    print(f'Request: {self.request!r}')

# @app.task(bind=True)
# def email_task(self,first_name,  last_name, email, entity_name, details):
#     print(f'Request: {self.request!r}')
