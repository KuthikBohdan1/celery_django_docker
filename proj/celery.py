import os
from celery import Celery
from celery.schedules import crontab
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'proj.settings')

# app = Celery('send_email')
# app.config_from_object('django.conf:settings', namespace='CELERY')
# app.autodiscover_tasks()
app = Celery('proj')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()

app.conf.beat_schedule = {
    'add-every-30-seconds': {
        'task': 'src.main.tasks.send_spam_email',
        'schedule': 30.0,
        'kwargs': {
            'user_email': 'bkuzik7@gmail.com',
            'text': str('Привіт, це спам!')
        }
    },
}

app.conf.timezone = 'UTC'