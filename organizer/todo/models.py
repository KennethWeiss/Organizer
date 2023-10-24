from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Task(models.Model):
    title = models.CharField(max_length=100)
    duration = models.BigIntegerField
    finished = bool
    worked_on = bool
    content = models.TextField()
    notes = models.TextField()
    date_posted = models.DateTimeField(default)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

