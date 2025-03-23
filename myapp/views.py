"""Views.py - this is where we store functions that render templates"""
# pylint: disable=no-member

from django.shortcuts import render

from .models import ShopItem
# HttpResponse

# Create your views here.


def home(request):
    """Function to render the home template"""
    return render(request, "home.html")


def shop(request):
    """Function to render the shop template with the shop items"""
    shop_items = ShopItem.objects.all()
    print(shop_items)  # Debugging: See if this prints in the terminal
    return render(request, "shop.html", {"items": shop_items})
