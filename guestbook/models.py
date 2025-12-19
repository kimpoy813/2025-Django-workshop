from django.db import models
from django.utils import timezone
from django.contrib.auth import get_user_model

class Guest(models.Model):
    active = models.BooleanField(default=True)
    owner = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, blank=True, null=True)
    message = models.TextField(blank=True, null=True)
    date_posted = models.DateTimeField(default=timezone.now)
