import os
from celery import Celery

# Set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'magazine.settings')

celery_app = Celery('magazine')
celery_app.config_from_object('django.conf:settings', namespace='CELERY')

celery_app.autodiscover_tasks()
