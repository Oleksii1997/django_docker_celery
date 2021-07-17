from celerytest.celery import app
from django.core.mail import send_mail

from .service import send
from .models import Contact


@app.task
def send_spam_email(user_email):
    send(user_email)


@app.task
def send_beat_email():
    for contact in Contact.objects.all():
        send_mail(
            'Ви підписались на розсилку',
            'Це спам',
            'biz.django@gmail.com',
            [contact.email],
            fail_silently=False,
        )
