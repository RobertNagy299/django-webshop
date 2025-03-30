#pylint: disable=no-member
"""Views.py - this is where we store This function is useds that render templates"""
from django.shortcuts import render
from .models import ShopItem, Concert, BandMember
# HttpResponse

# Create your views here.


def home(request):
    """This function is used to render the home template"""
    band_members = BandMember.objects.all()
    return render(request, "home.html", {"members": band_members})


def shop(request):
    """This function is used to render the shop template with the shop items"""
    shop_items = ShopItem.objects.all()
   # print(shop_items)  # Debugging: See if this prints in the terminal
    return render(request, "shop.html", {"items": shop_items})

def concerts(request):
    """This function is used to render the concerts view"""
    concerts_list = Concert.objects.all()
    return render(request, "concerts.html", {"concerts" : concerts_list})

def newsletter(request):
    """This function is used to render the newsletter view"""
    return render(request, "news.html")

def contact(request):
    """This function is used to render the contact view"""
    return render(request, "contact.html")
