from django.db import models


# Create your models here.
class Task(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    is_done = models.BooleanField()
    # image
    # author
    # deadline_date
    created_date = models.DateTimeField(auto_now_add=True)
    finished_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
