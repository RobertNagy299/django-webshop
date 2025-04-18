"""This file contains the form models"""
from django import forms
from .models import Inquiry


class InquiryForm(forms.ModelForm):
    """This class models the 'Contact Us' form"""
    class Meta:
        model = Inquiry
        fields = ['email_of_sender', 'content']
        widgets = {
            'email_of_sender': forms.EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter your email',
                'required': 'required',
            }),
            'content': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Enter your message',
                'rows': 4,
                'required': 'required',
            }),
        }

    def clean_email_of_sender(self):
        email = self.cleaned_data.get('email_of_sender')
        if not email:
            raise forms.ValidationError("Email is required.")
        return email

    def clean_content(self):
        content = self.cleaned_data.get('content')
        if not content:
            raise forms.ValidationError("Message content is required.")
        return content
