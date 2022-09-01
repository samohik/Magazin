from magazine.celery import celery_app
from orders.models import Order


@celery_app.task
def validator(number: str):
    if not int(number) % 2 and str(number)[-1] != 0:
        Order.objects.update(paid=True)
    else:
        Order.objects.update(paid=False, error='Error occur')
