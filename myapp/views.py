#pylint: disable=no-member
"""Views.py - this is where we store This function is useds that render templates"""
from django.shortcuts import render
from .models import ShopItem, Concert, BandMember
from .forms import InquiryForm
from django.core.mail import send_mail
from django.conf import settings
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
    toast_message = None
    toast_type = None

    if request.method == 'POST':
        form = InquiryForm(request.POST)
        if form.is_valid():
            inquiry = form.save()
            
             # Send email notification
            subject = f"New business inquiry from {inquiry.email_of_sender}"
            message = f"New business inquiry from: {inquiry.email_of_sender}:\n\n{inquiry.content}"
            from_email = settings.DEFAULT_FROM_EMAIL
            recipient_list = ['lakatosprime420@gmail.com']  # Change this to your email

            try:
                send_mail(subject, message, from_email, recipient_list)
            except Exception as e:
                print("Email sending failed:", e)  # For debugging
            
            toast_message = "Your message has been sent successfully!"
            toast_type = "success"
            form = InquiryForm()  # reset form
        else:
            toast_message = "Please fill in all fields correctly."
            toast_type = "danger"
    else:
        form = InquiryForm()

    return render(request, 'contact.html', {
        'form': form,
        'toast_message': toast_message,
        'toast_type': toast_type,
    })