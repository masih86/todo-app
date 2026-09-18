from celery import shared_task
from django.core.mail import send_mail
from django.conf import settings


@shared_task
def send_verification_email_task(user_email: str, token: str):
    verification_link = f"{settings.BACKEND_URL}/users/api/v1/verify-email/?token={token}"

    subject = "activating your account"
    message = f"in order to activate your account click here :\n{verification_link}\n\this link is valid for 15 mins."

    send_mail(
        subject,
        message,
        settings.DEFAULT_FROM_EMAIL,
        [user_email],
    )