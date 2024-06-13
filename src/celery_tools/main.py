# coding: utf-8
from celery import Celery

app = Celery(broker="redis://host.docker.internal:6379/0")
print(app.conf['broker_url'])

if __name__ == '__main__':
    app.start()
