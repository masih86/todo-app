from celery import shared_task
from django.core.mail import send_mail
from django.conf import settings
from celery.utils.log import get_task_logger
from django.utils import timezone
from rest_framework_simplejwt.token_blacklist.models import OutstandingToken
from users.models import CustomUser

logger = get_task_logger(__name__)


@shared_task(name='send_verification_email_task')
def send_verification_email_task(user_email: str, token: str):
    verification_link = f"{settings.BACKEND_URL}/users/api/v1/verify-email/?token={token}"

    subject = "activating your account"
    message = f"in order to activate your account click here :\n{verification_link}\n\ this link is valid for 15 mins."

    send_mail(
        subject,
        message,
        settings.DEFAULT_FROM_EMAIL,
        [user_email],
    )
    
    
@shared_task(name="cleanup_expired_items", ignore_result=True)
def cleanup_expired_items():
    now = timezone.now()
    
    _, token_detail = OutstandingToken.objects.filter(expires_at__lte=now).delete()
    
    cutoff = now - settings.UNVERIFIED_USER_RETENTION
    _, user_detail = CustomUser.objects.filter(
        is_active=False,
        is_staff=False,           
        is_superuser=False,
        last_login__isnull=True, 
        created_date__lt=cutoff,
        task__isnull=True, 
    ).delete()
    
    result = {
        "expired_tokens": token_detail.get("token_blacklist.OutstandingToken", 0),
        "unverified_users": user_detail.get("users.CustomUser", 0),
    
    }
    logger.info("cleanup_expired_items done: %s", result)
    return result