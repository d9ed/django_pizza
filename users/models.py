from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    age = models.PositiveIntegerField(null=True, blank=True)
    phone = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.username


class FeedbackRequest(models.Model):
    STATUS_CHOICES = [
        ('UNREAD', 'Unread'),
        ('READ', 'Read'),
    ]
    name = models.CharField(max_length=255, null=False, blank=False)
    email = models.EmailField(max_length=255, null=False, blank=False)
    subject = models.CharField(max_length=200, null=False, blank=False)
    message = models.TextField(max_length=600, null=False, blank=False)
    status = models.CharField(max_length=6, null=False, blank=False, choices=STATUS_CHOICES,
                              default=STATUS_CHOICES[0][1])
