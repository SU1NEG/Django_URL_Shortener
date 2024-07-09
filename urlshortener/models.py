# urlshortener/models.py
from django.db import models
from django.utils import timezone

class URL(models.Model):
    original_url = models.URLField()
    short_url = models.CharField(max_length=10, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)

class Click(models.Model):
    url = models.ForeignKey(URL, on_delete=models.CASCADE)
    ip_address = models.GenericIPAddressField()
    user_agent = models.CharField(max_length=255)
    timestamp = models.DateTimeField(default=timezone.now)
