import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')

app = Celery('core')

app.config_from_object('django.conf:settings', namespace='CELERY')

app.conf.beat_schedule = {
    'my_task_in_every_2_sec': {
        'task': 'home.tasks.my_task_2',
        'schedule': 2,
        'options': {
            'expires': 10,
        }
    }
}
