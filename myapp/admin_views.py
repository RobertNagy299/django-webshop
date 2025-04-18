# yourapp/admin_views.py
from django.conf import settings
from django.contrib.admin.views.decorators import staff_member_required
from django.shortcuts import render
from django.core.mail import send_mass_mail, send_mail
from .forms import NewsletterEmailForm
from .models import EmailList
from django.template.loader import render_to_string
from django.utils.html import strip_tags


@staff_member_required
def send_newsletter_view(request):
    toast_message = None
    toast_type = None

    if request.method == "POST":
        form = NewsletterEmailForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data["subject"]
            message = form.cleaned_data["message"]
            is_cta = form.cleaned_data["is_call_to_action"]

            
            recipients = EmailList.objects.values()

            for subscriber in recipients:
                email = subscriber.get("email_address")
                name = subscriber.get("first_name")
                unsub_token = subscriber.get("unsubscribe_token")
                unsub_link = f"{settings.DEFAULT_HOST_BASE_URL}/unsubscribe/{unsub_token}" 
                html_message = render_to_string('newsletter-email-template.html',
                                            {'message': message,
                                             "is_cta": is_cta,
                                             "name": name,
                                             "unsubscribe_link": unsub_link})
                plain_message = strip_tags(html_message)
                send_mail(subject, plain_message, settings.DEFAULT_FROM_EMAIL, [email], False, html_message=html_message)
            
            toast_message = "Letter sent to all subscribers!"
            toast_type = "success"
        else:
            toast_message = "Please fill out the required fields!"
            toast_type = "danger"
    else:
        form = NewsletterEmailForm()

    return render(request, "admin/send_newsletter.html",
                  {"form": form,
                   'toast_message': toast_message,
                   'toast_type': toast_type, })
