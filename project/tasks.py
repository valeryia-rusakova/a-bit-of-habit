from django.core.mail import send_mail
from development.celery import app


@app.task
def send_email_task(email):
    send_mail(
        'Congratulations!',
        'You have received a new achievement!',
        'support@bh.com',
        [email]
    )

    return None
