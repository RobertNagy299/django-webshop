from django.db import models

# Create your models here.
class ShopItem(models.Model):
    title = models.CharField(max_length=200)
    available = models.BooleanField(default=True)
    price = models.FloatField(default=9.99)
