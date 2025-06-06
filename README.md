# Github
https://github.com/RobertNagy299/django-webshop

# PyPi

https://pypi.org/project/band-landing-page-webshop/

# Demo Video

https://youtu.be/7nax_fFP0wk


# Test coverage
I used the `coverage` package and Django's built in testing framework to
achieve at least 50% test coverage for all major python files.

Coverage report can be seen in the demo video 

# Code quality

I used `Flake8` and `bandit` to assure that my code follows Pythonic coding standards, and that it doesn't contain any vulnerabilities.
The results of the code analysis can be seen in the demo video.

# Features
The website includes a dark/light mode switch, and every page is responsive and looks great on any device!

The site consists of the following pages: 
- <b>Homepage</b>
  - Jumbotron with a 'contact us' call-to-action button
  - A grid view of the band members, with images and short descriptions
- <b>Shop</b>
  - Grid view of the items
  - "Add to cart" buttons
  - Users can change the quantity of the items
- <b>Contact</b>
  - Contact form, where users can enter their email and their message
- <b>Concerts</b>
  - A Bootstrap Carousel element contains images and short descriptions of concerts
- <b>News</b>
  - This page contains a form, that users can use to subscribe to the newsletter
- <b>Cart</b>
  - The cart page contains the items the user has put in their shopping cart
  - Users can remove items, or proceed to checkout
  - Clicking the checkout button will open the Stripe Checkout page.

- <b>Custom admin page for composing a letter</b>
  - This page is only available for site admins
  - This page contains a form, which admins can use to send an email to everyone who is subscribed to the newsletter
  - Admins can include a call-to-action button
  - Furthermore, they can include unique discounts with the CTA button
  - The discounts work as unique llinks, only available if the user clicks on the button.
- ## Newsletter
  - Users can subscribe
  - Users can unsubscribe (each email contains the unsubscribe link which is based on a UUID token)
  - The site admin can send a letter to all subscribers with a simple form on a custom admin view
  - It is not possible to subscribe with the same email address multiple times
  - All form fields are validated on the backend
  - The sent emails are based on an html template to make them look good, but there is also a fallback in case the html couldn't be rendered in the email
  - Users cannot reach the admin site
  - Subscribed users are stored in a database
  - Unsubscribed users are deleted from the database
- ## Contact form
  - Users can fill out a contact form
  - The form is validated on the backend
  - The form is saved in a database
  - An email is sent to the site admin containing the contents of the contact form upon a successful submission
- ## Shop
  - Webshop with Stripe (third party payment processor integration)
  - Real payments simulated using Stripe's checkout page using the Stripe API
  - Real discount coupons and promo codes implemented with Stripe API (These can be
  created and sent from the custom admin page - send-newsletter.html - just tick the "include CTA button" checkbox
  and then specify the percentage and duration)
  - Coupon expiration handled on the UI and backend
  
# Installation notes:
1. Create a virtual environment (recommended)

    - `python -m venv venv`<br>
    - `source venv/bin/activate`<br>
    On Windows: `venv\Scripts\activate`<br>

2. Install the package
    - Run the installation command (Can be found on PyPi)<br>

3. Set up environment variables

    - Create a .env file in your project root:
    - Create all environment variables (see below)

4. Run migrations

    - `run-myproject migrate`

5. Create a superuser - also known as an admin (optional)

    - `run-myproject createsuperuser`

6. Run the development server

    - `run-myproject runserver`

7. Then open your browser and go to `http://127.0.0.1:8000`

## Environment variables:
### SECURITY WARNING: keep the secret key used in production secret!
### SECURITY WARNING: don't run with debug turned on in production!
SECRET_KEY = config("SECRET_KEY")    
DEBUG = config("DEBUG", cast=bool)  
DEFAULT_HOST_BASE_URL = config("DEFAULT_HOST_BASE_URL")  

## Email config
EMAIL_BACKEND = config("EMAIL_BACKEND")
EMAIL_HOST = config("EMAIL_HOST")
EMAIL_PORT = config("EMAIL_PORT")
EMAIL_USE_TLS = config("EMAIL_USE_TLS", cast=bool)
EMAIL_HOST_USER = config("EMAIL_HOST_USER")

### Not your actual Gmail password! Use an App Password.
EMAIL_HOST_PASSWORD = config("EMAIL_HOST_PASSWORD")  
DEFAULT_FROM_EMAIL = EMAIL_HOST_USER  
SYSADMIN_DEFAULT_EMAIL_RECIPIENT = config("SYSADMIN_DEFAULT_EMAIL_RECIPIENT")  

## Stripe setup

STRIPE_SECRET_KEY = config("STRIPE_SECRET_KEY")  
STRIPE_PUBLISHABLE_KEY = config("STRIPE_PUBLISHABLE_KEY")  

# Example .env file:

SECRET_KEY='asd'  
EMAIL_BACKEND='youremailbackend'  
EMAIL_HOST='yourhost.example.com'  
EMAIL_PORT=1521  
EMAIL_USE_TLS=True  
EMAIL_HOST_USER='yourname@gmail.com'  
EMAIL_HOST_PASSWORD='acde efgh ijkl mnop'  
SYSADMIN_DEFAULT_EMAIL_RECIPIENT='admin@gmail.com'  
DEBUG=False  
DEFAULT_HOST_BASE_URL="http://127.0.0.1:8000"  
DB_ENGINE='dbengine'  
DB_NAME='dbname'  
STRIPE_SECRET_KEY='stripe_secret_key'  
STRIPE_PUBLISHABLE_KEY='stripe_publishable_key'  
