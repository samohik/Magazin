from django.http import HttpResponse
from celery import shared_task

from magazine.celery import celery_app


@celery_app.task
def make_thumbnails(number, model):
    if not int(number) % 2 and str(number)[-1] != 0:
        model.update(paid=True)
    else:
        model.update(paid=False, error='Error occur')
