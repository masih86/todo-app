from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from django.core.cache import cache
from .models import Task
from .cache_utils import task_list_cache_key
from users.models import CustomUser


@receiver([post_save, post_delete], sender=Task)
def clear_task_cache(sender, instance, **kwargs):
    cache.delete(f"task_list_user_{instance.author_id}")

    cache.delete(f"task_list_role_{CustomUser.Role.ADMIN}")
    cache.delete(f"task_list_role_{CustomUser.Role.TEACHER}")