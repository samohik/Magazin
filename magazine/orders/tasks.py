import random

from magazine.celery import celery_app
from orders.models import Order


@celery_app.task
def validator(number: str):
    if not int(number) % 2 and str(number)[-1] != 0:
        Order.objects.update(paid=True, error='')
    else:
        Order.objects.update(
            paid=False,
            error=f'Error occur: {random.randint(1000, 9999)}'
        )
