# coding: utf-8
from celery import shared_task


@shared_task
def add(*args):
    return sum(*args)
