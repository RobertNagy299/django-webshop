
"""This file contains all the database model classes that the project uses for the SQLite DB"""
#pylint: ignore=no-member
from django.db import models

# Create your models here.


class ShopItem(models.Model):
    """Database model class for a shop item"""
    # item_id = models.BigIntegerField()
    title = models.CharField(max_length=200)
    available = models.BooleanField(default=True)
    price = models.FloatField(default=9.99)
    cover_photo_url = models.CharField(max_length=300, default="")


class Concert(models.Model):
    """Database model class used to model a concert instance"""
    # concert_id = models.BigIntegerField()
    date = models.DateField()
    place = models.CharField(max_length=64)
    description = models.CharField(max_length=400)
    title = models.CharField(max_length=64)
    cover_photo_url = models.CharField(max_length=300, default="")


class BandMember(models.Model):
    """Class for modelling a band member - used to display band info"""
    name = models.CharField(max_length=100)
    role = models.CharField(max_length=100)
    description = models.CharField(max_length=400)
    photo_url = models.CharField(max_length=300, default="")


class EmailList(models.Model):
    """Singleton model - used to store the people subscribed to our email list"""
    email_address = models.EmailField(max_length=100)
    first_name = models.CharField(max_length=32, null=True, blank=True)
