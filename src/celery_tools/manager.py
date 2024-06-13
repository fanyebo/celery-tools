# coding: utf-8
from celery import Celery


class Manager(object):
    def __init__(self, broker: str = None, app: Celery = None):
        assert broker is not None or app is not None, "broker and app both are None"
        self.broker = broker or app.conf.get('broker_url')
        self.inspect = app.control.inspect()

    def get_current_executing_tasks(self):
        """ 获取当前正在执行的任务信息 """
        return self.inspect.active()

    def get_current_consuming_from_queues(self):
        """ 获取worker当前运行中的任务队列 """
        return self.inspect.active_queues()

    def ping_worker(self, destination=None):
        """ 向对应的worker发送心跳包 """
        return self.inspect.ping(destination=destination)


def main():
    from main import app
    manage = Manager(app=app)
    print(manage.get_current_executing_tasks())
    print(manage.get_current_consuming_from_queues())
    print(manage.ping_worker(['celery@8fe8b9b7eb4e']))


if __name__ == '__main__':
    main()
