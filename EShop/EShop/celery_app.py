from __future__ import absolute_import, unicode_literals
import os
from celery import Celery
# from EShop.EShop.celery_app import Celery



os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'EShop.settings')

app = Celery('EShop')

app.config_from_object('django.conf:settings', namespace='CELERY')

app.autodiscover_tasks()

@app.task(bind=True)
def debug_task(self):
    print('Request: {0!r}'.format(self.request))
