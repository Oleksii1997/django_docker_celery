import os
from celery import Celery
# для періодичної відправки листів
from celery.schedules import crontab

# вказуємо де знаходяться налаштування django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'celerytest.settings')

app = Celery('celerytest')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()

# таска яка буде виконуватися кожні 5 хвилин
app.conf.beat_schedule = {
    'send-spam-email-5-minute':{
        'task': 'send_email.tasks.send_beat_email',
        'schedule': crontab(minute='*/5'),
    },
}