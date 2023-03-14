from django.db import models
from datetime import datetime 
from django.utils import timezone

class Product(models.Model):
    manufacturer = models.CharField(max_length=200, null=True)
    model = models.CharField(max_length=200, null=True)
    category = models.CharField(max_length=200, null=True)
    description = models.TextField(null=True)
    price_cents = models.IntegerField(null=True)
    rating = models.FloatField(null=True)
    volume_discount_percent = models.IntegerField(null=True)
    volume_discount_threshold = models.IntegerField(null=True)
    color = models.CharField(max_length=200, null=True)
    created_at = timezone.now
    updated_at = timezone.now
