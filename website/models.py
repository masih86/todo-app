from django.db import models
from django.utils import timezone


class Task(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    is_done = models.BooleanField(default=False)
    author = models.ForeignKey("users.CustomUser", on_delete=models.CASCADE)
    image = models.ImageField(null=True, blank=True)

    deadline_date = models.DateTimeField(null=True, blank=True)

    created_date = models.DateTimeField(auto_now_add=True)
    finished_date = models.DateTimeField(null=True, blank=True)

    def save(self, *args, **kwargs):
        if self.is_done and self.finished_date is None:
            self.finished_date = timezone.now()
        elif not self.is_done:
            self.finished_date = None

        super().save(*args, **kwargs)

    def __str__(self):
        return self.title