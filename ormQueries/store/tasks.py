from __future__ import absolute_import, unicode_literals

from celery import shared_task

from .models import SalesOrder

from django.db.models import F
from datetime import timedelta
#from dateutil.relativedelta import *


@shared_task
def increase_days_by(num_of_days: int):
    return SalesOrder.objects.all().update(order_date=F('order_date')+timedelta(days=num_of_days))


@shared_task
def increase_months_by(num_of_months: int):
    #return SalesOrder.objects.all().update(order_date=F('order_date')+relativedelta(months=num_of_months))
    return SalesOrder.objects.all().update(order_date=F('order_date')+timedelta(months=num_of_months))


# https://docs.python.org/3/library/datetime.html#datetime.timedelta

# https://stackoverflow.com/q/35066588/3790620