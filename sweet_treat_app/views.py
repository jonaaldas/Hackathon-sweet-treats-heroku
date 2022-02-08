# from django.shortcuts import render, HttpResponse
# from django.contrib import messages
# from .models import *
# # import bcrypt
# import re
# EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate, logout
from django.conf import settings
from django.core.mail import send_mail
from django.shortcuts import render, redirect, HttpResponse

def index(request):
    return render(request, 'sweet_treat_app/index.html')

def sweets(request):
    return render(request,'sweet_treat_app/sweets.html')

def about(request):
    return render(request,'sweet_treat_app/about.html')

def inventory(request):
    return render(request,'sweet_treat_app/inventory.html')


# EMAIL

def signup(request):
    if request.method=="POST":
        username =request.POST["username"]
        password =request.POST["password"]
        email = request.POST["email"]

        user = User.objects.create_user(
                username = username,
                password = password,
                email = email
             )
        login (request,user)
        subject = 'Welcome to Sweet Treats'
        message = f'Hi {user.username}, thank you for signing up to the Sweet Treats mailing list!'
        email_from = settings.EMAIL_HOST_USER
        recipient_list = [user.email, ]
        send_mail( subject, message, email_from, recipient_list )
        return redirect("/dashboard/")
    return render(request, "signup.html")