from django.core.mail import send_mail


def send(user_email):
    send_mail(
        'Ви підписались на розсилку',
        'Ми будемо надсилати багато листів',
        'biz.django@gmail.com',
        [user_email],
        fail_silently=False,
    )
