from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings
from django.contrib.auth.decorators import login_required

# Create your views here.
def home(request):
    return render(request, 'home.html')


from django.shortcuts import render

def landing_page(request):
    return render(request, 'landing.html')  # Ensure this template exists
