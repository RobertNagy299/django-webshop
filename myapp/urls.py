"""This file is where we define the routing inside my app"""
from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("shop/", views.shop, name="shop"),
    path("contact/", views.contact, name="contact"),
    path("news/", views.newsletter, name="newsletter"),
    path("concerts/", views.concerts, name="concerts")
]
