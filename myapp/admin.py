"""In this file, we register our models for the admin page"""
from django.contrib import admin
from .models import ShopItem, EmailList, BandMember, Concert, Inquiry
from django.urls import path
from django.shortcuts import render, redirect
from django.core.mail import send_mass_mail
from django.contrib import messages
from .forms import NewsletterEmailForm
from django.conf import settings


# Register your models here.
admin.site.register(ShopItem)
admin.site.register(EmailList)
admin.site.register(BandMember)
admin.site.register(Concert)
admin.site.register(Inquiry)



