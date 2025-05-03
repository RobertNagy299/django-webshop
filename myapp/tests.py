"""This file contains the unit tests. 50% coverage is required. 
Use the 'coverage' python package for verification"""
from django.test import TestCase
import unittest

from .templatetags.discount_tags import discounted_price
from .models import EmailList

#region template tag tests

class DiscountTemplateTagTest(TestCase):
    """This class is responsible for testing the discount template tag.
    The template tag dynamically calculates the discounted price
    of an item given the original item's price, and a discount percentage"""
    def test_discounted_price_math(self):
        """Testing with whole numbers, works fine"""
        result = discounted_price(100, 20)
        self.assertEqual(result, "80.00")
        
    def test_discounted_price_wrong_input(self):
        """If the input is interpreted as a string, it should stay untouched"""
        result = discounted_price("14.99", 25)
        self.assertEqual(result, "14.99")
    
    def test_discounted_price_float(self):
        """Test for rounding errors"""
        result = discounted_price(1299.99, 50)
        self.assertNotEqual(result, 650.00)
        
    def test_discounted_price_exception(self):
        """Test if TypeError exception is thrown for incorrect price type"""
        self.assertRaises(TypeError, discounted_price, price=None)

#endregion

#region Model tests

class EmailListModelTest(TestCase):
    """This class holds the tests for the creation of an email list subscriber object"""
    def test_email_list_subscriber_creation(self):
        """Test if the email is set correctly"""
        email = EmailList.objects.create(email_address="test@example.com", first_name="Test")
        self.assertEqual(email.email_address, "test@example.com")
    def test_first_name_setting(self):
        """Test if the first_name is set correctly"""
        subscriber = EmailList.objects.create(email_address="johndoe@asd.com", first_name="Arthur")
        self.assertEqual(subscriber.first_name, "Arthur")

#endregion
